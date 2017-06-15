#!/usr/bin/python2

from sqlalchemy.orm import sessionmaker

from db.Config import Base
from db.Config import engine
from db.Sender import Sender
from db.Receiver import Receiver
from db.Email import Email

def main():
	Base.metadata.create_all(engine,checkfirst=True)	
	print Sender.__table__
	Session = sessionmaker(bind=engine)
	session = Session()
	for i in range(1,10,1):
		sender = Sender(email='root@email.com', api_key='Vy2FQzBcheiw6It4pzqraeTvR_LEuQok8TI', status=i)
		print sender.email	
		session.add(sender)
		
	got_senders = session.query(Sender).filter_by(email='root@email.com')
	#got_senders = session.query(Sender).all()
	for s in got_senders:
		print s


if __name__ == '__main__':
	print "Start"
	main()
	print "End"
