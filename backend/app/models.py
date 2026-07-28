from __future__ import annotations

from pydantic import BaseModel, Field
from typing import List


class Sensor(BaseModel):
    sensor_name: str
    sensor_type: str
    value: float
    unit: str


class Machine(BaseModel):
    machine_name: str
    machine_type: str
    power_rating: float
    status: str
    operating_hours: float
    sensors: List[Sensor] = Field(default_factory=list)


class Factory(BaseModel):
    factory_name: str
    location: str
    industry: str
    area: float
    number_of_machines: int
    machines: List[Machine] = Field(default_factory=list)