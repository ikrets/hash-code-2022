from dataclasses import dataclass
from typing import TextIO, List, Dict

@dataclass
class Service:
    name: str
    binary_id: int

@dataclass
class Binary:
    services: List[Service]

@dataclass
class Feature:
    name: str
    difficulty: int
    daily_users: int
    services: List[Service]

@dataclass
class Problem:
    num_days: int
    num_engineers: int
    services: Dict[str, Service]
    binaries: List[Binary]
    features: Dict[str, Feature]
    create_binary_days: int


def read_int_line(fp: TextIO):
    return [int(s) for s in fp.readline().strip("\n").split(" ")]

def read_file(fp) -> Problem:
    days, engineers, num_services, num_binaries, num_features, N = read_int_line(fp)

    services = {}
    binaries = [Binary(services=[]) for _ in range(num_binaries)]

    for _ in range(num_services):
        name, binary_id = fp.readline().strip("\n").split(" ")
        s = Service(name=name, binary_id=int(binary_id))
        services[name] = s
        binaries[int(binary_id)].services.append(s)

    features = {}
    for _ in range(num_features):
        name, _, difficulty, daily_users = fp.readline().strip("\n").split(" ")
        f = Feature(name, int(difficulty), int(daily_users), [])

        service_names = fp.readline().strip("\n").split(" ")
        f.services = [services[service_name] for service_name in service_names]
        features[name] = f

    return Problem(
        num_days=days,
        num_engineers=engineers,
        services=services,
        binaries=binaries,
        features=features,
        create_binary_days=N
    )




    