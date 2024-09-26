from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from config.base import Base

class TargetType(Base):
    __tablename__ = "TargetTypes"
    target_type_id = Column(Integer, primary_key=True, autoincrement=True)
    target_type_name = Column(String(255), nullable=False, unique=True)

    targets = relationship(
        "Target",
        lazy="joined",
        back_populates="target_type",
        cascade='all, delete-orphan',
    )

    def __repr__(self):
        return f"<TargetType(id={self.target_type_id}, name={self.target_type_name})>"