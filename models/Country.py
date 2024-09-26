from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from config.base import Base

class Country(Base):
    __tablename__ = "countries"
    country_id = Column(Integer, primary_key=True, autoincrement=True)
    country_name = Column(String(100), nullable=False, unique=True)

    cities = relationship(
        "City",
        lazy="joined",
        back_populates="country",
        cascade='all, delete-orphan'
    )

    def __repr__(self):
        return f"<Country(id={self.country_id}, name={self.country_name})>"