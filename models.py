from sqlalchemy import Column, String, Integer, TIMESTAMP, text
from database import Base

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    email = Column(String, nullable=False)
    password = Column(String, nullable=False)
    token = Column(Integer, nullable=False, server_default='10')
    time = Column(TIMESTAMP, nullable=False, server_default=text("NOW() + INTERVAL '10 days'"))