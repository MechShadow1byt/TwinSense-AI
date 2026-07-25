from pydantic import BaseModel
from typing import List

class Factory(BaseModel):
    factory_name: str
    location: str
    industry: str
    area: float
    number_of_machines: int
    machines: List[dict] = []


class Machine(BaseModel):
    machine_name: str
    machine_type: str
    power_rating: float
    status: str
    sensors: List[dict] = []

class Sensor(BaseModel):
    sensor_name: str
    sensor_type: str
    value: float
    unit: str