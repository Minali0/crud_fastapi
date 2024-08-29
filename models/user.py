from sqlalchemy import Table,Column,DateTime
from sqlalchemy.sql.sqltypes import Integer,String
from config.db import meta
from datetime import datetime


users = Table(
    'users',meta,
    Column('id',Integer,primary_key=True),
    Column('name',String(255)),
    Column('email',String(255)),
    Column('password',String(255)),
    Column("created_at", DateTime, default=datetime.utcnow),
    Column("updated_at", DateTime, default=datetime.utcnow),
    extend_existing=True


)