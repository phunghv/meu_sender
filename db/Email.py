import datetime
from sqlalchemy import Column, Integer, String, Sequence, ForeignKey, UnicodeText, DateTime
from Config import Base
from Receiver import Receiver
from Sender import Sender

class Email(Base):
	__tablename__ = 'email'
	id = Column(Integer,Sequence('email_id_seq'), primary_key=True)
	sender = Column(Integer, ForeignKey(Sender.id))
	receiver=Column(Integer, ForeignKey(Receiver.id))
	content = Column(UnicodeText, nullable=False)
	send_date = Column(DateTime)
	status = Column(Integer, server_default='0')

	def __repr__(self):
		return "<Email(sender='%d', receiver='%d', content='%s' status='%d')>" % (self.sender, self.receiver, self.content, self.status)