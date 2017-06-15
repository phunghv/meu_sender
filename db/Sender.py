from sqlalchemy import Column, Integer, String, Sequence
from Config import Base

class Sender(Base):
	__tablename__ = 'sender'
	id = Column(Integer,Sequence('sender_id_seq'), primary_key=True)
	email = Column(String, nullable=False)
	api_key = Column(String, nullable=False)
	count = Column(Integer, server_default='0')
	status = Column(Integer, server_default='0')


	def __repr__(self):
		return "<Sender(email='%s', api_key='%s', status='%d')>" % (self.email, self.api_key, self.status)