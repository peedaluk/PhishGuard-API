from pydantic import BaseModel
from datetime import datetime 

class Url(BaseModel):
    url : str

class UrlResponse(BaseModel):
    id : int
    url : str
    prediction : str
    confidence : float
    timestamp : datetime
    
    class Config:
        from_attributes = True

