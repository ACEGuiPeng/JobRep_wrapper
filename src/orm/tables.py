# -*- coding:utf-8 -*-
from sqlalchemy import Column, String, Integer
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Material(Base):
    __tablename__ = 'product_materials'

    asin = Column(String(32), primary_key=True)
    uid = Column(String(32))
    update_time = Column(String(32))
    name = Column(String(1024))
    price = Column(String(32))
    title = Column(String(1024))
    ad_text = Column(String(2048))
    links = Column(String(2048))
    keywords = Column(String(2048))


class MaterialRecord(Base):
    __tablename__ = 'material_record'

    id = Column(String(32), primary_key=True, autoincrement=True)
    asin = Column(String(32))
    record_time = Column(String(32))
    resource = Column(String(32))
    title = Column(String(1024))
    ad_text = Column(String(2048))
    type = Column(String(2048))
    link = Column(String(2048))


class Resources(Base):
    __tablename__ = 'resource'

    id = Column(String(32), primary_key=True, autoincrement=True)
    uid = Column(String(32))
    asin = Column(String(32))
    update_time = Column(String(32))
    type = Column(String(16))
    keywords = Column(String(2048))
    addr = Column(String(2048))


class ResourceRecord(Base):
    __tablename__ = 'resource_record'

    id = Column(String(32), primary_key=True, autoincrement=True)
    depot_id = Column(String(32))
    uid = Column(String(32))
    asin = Column(String(32))
    case_id = Column(String(32))


class LandingPage(Base):
    __tablename__ = 'landing_page'

    id = Column(String(32), primary_key=True, autoincrement=True)
    uid = Column(String(32))
    update_time = Column(String(32))
    template_id = Column(String(32))
    attributes = Column(String(2048))


class LandingPageRecord(Base):
    __tablename__ = 'landing_page_record'

    id = Column(String(32), primary_key=True, autoincrement=True)
    depot_id = Column(String(32))
    uid = Column(String(32))
    asins = Column(String(32))
    update_time = Column(String(32))
    template_id = Column(String(32))
    attributes = Column(String(2048))


class AdCase(Base):
    __tablename__ = 'case'

    id = Column(String(32), primary_key=True, autoincrement=True)
    uid = Column(String(32))
    type = Column(String(32))
    ad_records = Column(String(32))
    target_id = Column(String(32))
    status = Column(String(32))
    bidding = Column(String(2048))
