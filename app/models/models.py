from sqlalchemy import Column, Integer, String, Text
from app.database.db import Base

class Memory(Base):
    __tablename__ = "memories"

    id = Column(Integer, primary_key=True, index=True)
    content = Column(Text)
    category = Column(String, default="general")