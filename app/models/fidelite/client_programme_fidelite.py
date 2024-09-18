from sqlalchemy import Table, Column, Integer, ForeignKey
from app.database import Base

client_programme_fidelite = Table(
    'client_programme_fidelite', Base.metadata,
    Column('client_id', Integer, ForeignKey('client.codcli'), primary_key=True),
    Column('programme_fidelite_id', Integer, ForeignKey('programme_fidelite.id'), primary_key=True)
)