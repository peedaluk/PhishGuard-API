from database import Base
from sqlalchemy import Column, Integer , String , Float , DateTime
from sqlalchemy.sql import func

class ScanResult(Base):
    __tablename__ = "scan_results"

    id = Column(Integer , primary_key = True, index = True)
    url = Column(String , index = True)
    prediction = Column(String)
    confidence = Column(Float)
    timestamp = Column(DateTime(timezone = True), server_default = func.now())

