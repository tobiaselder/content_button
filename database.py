from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.schema import MetaData, Table
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine, Column, Integer, String

Base = declarative_base()

def createSession(path):
   engine = create_engine(path)
   smaker = sessionmaker(bind=engine)
   return smaker(), engine, MetaData(bind=engine)

sdd, sdd_engine, sdd_md = createSession('sqlite:///universeDataDx.db')

# SDDSystemConnection = Table('mapSolarSystemJumps', sdd_md, autoload=True, autoload_with=sdd_engine)

class SDDSystemConnection(Base):
   __table__ = Table('mapSolarSystemJumps', sdd_md,
         Column('fromSolarSystemID', Integer, primary_key=True),
         Column('fromConstellationID', Integer),
         Column('fromRegionID', Integer),
         Column('toSolarSystemID', Integer, primary_key=True),
         Column('toConstellationID', Integer),
         Column('toRegionID', Integer),
         autoload=True, autoload_with=sdd_engine)

   # __tablename__ = 'mapSolarSystemJumps'

   # fromRegionID = Column(Integer)
   # fromConstellationID = Column(Integer)
   # fromSolarSystemID = Column(Integer)
   # toRegionID = Column(Integer)
   # toConstellationID = Column(Integer)
   # toSolarSystemID = Column(Integer)

   # def __repr__(self):
   #    print "<SDDSystemConnection(from=({}, {}, {}), to=({}, {}, {}))>".format(
   #       self.fromRegionID,
   #       self.fromConstellationID,
   #       self.fromSolarSystemID,
   #       self.toRegionID,
   #       self.toConstellationID,
   #       self.toSolarSystemID
   #    )

