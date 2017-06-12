#!/usr/bin/python2

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Sequence
from sqlalchemy.orm import sessionmaker


engine = create_engine('sqlite:///testdb.sqlite', echo=True)
Base = declarative_base()

class User(Base):
	__tablename__ = 'user'
	
	id = Column(Integer,Sequence('user_id_seq'), primary_key=True)
	name = Column(String)
	fullname = Column(String)
	password = Column(String)

	def __repr__(self):
		return "<User(name='%s', fullname='%s', password='%s')>" % (self.name, self.fullname, self.password)




def main():
#	engine = create_engine('sqlite:///:memory:', echo=True)
#	Base = declarative_base()
	Base.metadata.create_all(engine)	
	print User.__table__
	ed_user = User(name='ed', fullname='Ed Jones', password='edspassword')
	print ed_user.name
	Session = sessionmaker(bind=engine)
	session = Session()
	session.add(ed_user)
	our_user = session.query(User).filter_by(name='ed').first()
	print our_user


if __name__ == '__main__':
	print "Start"
	main()
	print "End"
