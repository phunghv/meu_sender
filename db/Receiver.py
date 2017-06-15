from sqlalchemy import Column, Integer, String, Sequence
from Config import Base

class Receiver(Base):
	__tablename__ = 'receiver'
	id = Column(Integer,Sequence('receiver_id_seq'), primary_key=True)
	first_name = Column(String)
	last_name = Column(String)
	status = Column(Integer, server_default='0')


	def __repr__(self):
		return "<Receiver(first_name='%s', last_name='%s', status='%d')>" % (self.first_name, self.last_name, self.status)