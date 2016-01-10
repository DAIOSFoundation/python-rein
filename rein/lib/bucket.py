from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Bucket(Base):
    __tablename__ = 'bucket'

    id = Column(Integer, primary_key=True)
    identity = Column(Integer, nullable=False)
    remote_id = Column(String(250))
    date_created = Column(DateTime)
    url = Column(String(250), nullable=False)
    bytes_free = Column(Integer)
    expires = Column(DateTime)

    def __init__(self, url, identity, remote_id, bytes_free, date_created):
        self.url = url
        self.identity = identity
        self.remote_id = remote_id
        self.bytes_free = bytes_free
        self.date_created = date_created

    def update(self, url=None, remote_id=None, bytes_free=None, expires=None):
        if url: self.url = url
        if remote_id: self.remote_id
        if bytes_free: self.bytes_free
        if expires: self.expires


def create_buckets(engine):
    Base.metadata.create_all(engine)