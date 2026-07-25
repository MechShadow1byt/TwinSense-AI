from fastapi import FastAPI
from app.models import Factory, Machine, Sensor

# Temporary storage
factories = {}
next_factory_id = 1

machines = {}
next_machine_id = 1

app = FastAPI(
    title="Environmental Digital Twin",
    description="AI-powered Environmental Digital Twin Backend",
    version="1.0.0"
)


# ---------------- HOME ----------------

@app.get("/")
def home():
    return {
        "project": "Environmental Digital Twin",
        "status": "Running",
        "version": "1.0.0"
    }

@app.get("/system/health")
def system_health():
    return {
        "database": "Connected",
        "digital_twin": "Running",
        "ai": "Online",
        "sensors": "23/25 Active"
    }

@app.post("/factory")
def create_factory(factory: Factory):
    global next_factory_id
    
    current_id = next_factory_id
    factories[current_id] = factory
    next_factory_id += 1

    return {
        "message": "Factory created successfully!",
        "factory_id": current_id,
        "factory": factory
    }

# ---------------- FACTORY APIs ----------------

@app.get("/factory/{factory_id}")
def get_factory(factory_id: int):

    if factory_id not in factories:
        return {
            "error": "Factory not found"
        }

    return {
        "factory_id": factory_id,
        "factory": factories[factory_id]
    }


# ---------------- MACHINE APIs ----------------

@app.post("/factory/{factory_id}/machine")
def add_machine(factory_id: int, machine: Machine):

    if factory_id not in factories:
        return {
            "error": "Factory not found"
        }

    factories[factory_id].machines.append(machine)

    return {
        "message": "Machine added successfully!",
        "factory_id": factory_id,
        "machine": machine
    }




@app.post("/machine")
def create_machine(machine: Machine):
    global next_machine_id

    current_id = next_machine_id
    machines[current_id] = machine
    next_machine_id += 1

    return {
        "message": "Machine created successfully!",
        "machine_id": current_id,
        "machine": machine
    }

# ---------------- SENSOR APIs ----------------

@app.post("/factory/{factory_id}/machine/{machine_index}/sensor")
def add_sensor(factory_id: int, machine_index: int, sensor: Sensor):

    if factory_id not in factories:
        return {
            "error": "Factory not found"
        }

    factory = factories[factory_id]

    if machine_index >= len(factory.machines):
        return {
            "error": "Machine not found"
        }

    factory.machines[machine_index].sensors.append(sensor)

    return {
        "message": "Sensor added successfully!",
        "sensor": sensor
    }