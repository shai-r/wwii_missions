from sqlalchemy import Column, Integer, ForeignKey, String, DECIMAL
from sqlalchemy.orm import relationship
from config.base import Base

class City(Base):
    __tablename__ = "cities"
    city_id = Column(Integer, primary_key=True, autoincrement=True)
    city_name = Column(String(100), nullable=False, unique=True)
    country_id = Column(Integer, ForeignKey("countries.country_id"), nullable=False)
    latitude = Column(DECIMAL)
    longitude = Column(DECIMAL)

    country = relationship("Country", back_populates="cities")

    targets = relationship("Target",
        lazy="joined",
        back_populates="city",
        cascade='all, delete-orphan'
    )


    def __repr__(self):
        return (f"<City(id={self.city_id}, name={self.city_name}, "
                f"country id={self.country_id}, latitude={self.latitude}, "
                f"longitude={self.longitude})>")
