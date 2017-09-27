# -*- coding:utf-8 -*-
from sqlalchemy import Column, String, Integer
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Material(Base):
    __tablename__ = 'fbad_material'

    sid = Column(String(128), primary_key=True)
    timestamp = Column(String(128), primary_key=True)
    content = Column(String(2048))


class AdCase(Base):

    __tablename__ = 'fbad_case'

    sid = Column(String(128), primary_key=True)
    timestamp = Column(String(64), primary_key=True)
    case_name = Column(String(256))
    target_id = Column(String(128))
    material_timestamp = Column(String(128))
    status = Column(String(128))
    bidding = Column(String(2048))

class LandingPage(Base):
    __tablename__ = 'fbad_landing_page'

    url = Column(String(128), primary_key=True)
    template = Column(String(128))
    photo_addrs = Column(String(1024))
    link = Column(String(1024))
    ad_text = Column(String(2048))
    discount = Column(Integer())
    keywords = Column(String(128))
