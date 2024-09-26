from sqlalchemy import Column, Integer, ForeignKey, Float, String, DECIMAL
from sqlalchemy.orm import relationship
from config.base import Base

class Target(Base):
    __tablename__ = "targets"
    target_id = Column(Integer, primary_key=True, autoincrement=True)
    target_industry = Column(String(255), nullable=False)
    city_id = Column(Integer, ForeignKey("cities.id"), nullable=False)
    target_type_id = Column(Integer, ForeignKey("TargetTypes.id"), nullable=False)
    target_priority =  Column(Integer)
    latitude = Column(DECIMAL)
    longitude = Column(DECIMAL)

    country = relationship("Country", back_populates="cities")
    cities = relationship("City",
        lazy="joined",
        back_populates="targets",
        cascade='all, delete-orphan'
    )

    target_types = relationship("TargetType",
        lazy="joined",
        back_populates="targets",
        cascade='all, delete-orphan'
    )


    def __repr__(self):
        return (f"<City(id={self.city_id}, name={self.city_name}, "
                f"country id={self.country_id}, latitude={self.latitude}, "
                f"longitude={self.longitude})>")
