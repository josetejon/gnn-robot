from enum import Enum
from typing import Optional

class DSREdgeType(Enum):
    RT=1
    reachable=2
    in=3
    knows=4
    transitable=5
    visible=6
    accessible=7
    graspable=8
    talking=9
    looking_at=10
    sitting=11
    standing=12
    close_to=13
    has=14
    blocked=15
    is_blocking=16
    is_near=17
    front=18
    interacting=19
    interactive=20
    thinks=21
    goto_action=22
    attention_a=23
    following_a=24
    lost=25
    testtype_e=26
    is_not_waiting=27
    stopped=28
    is_charging=29
    is_not=30
    has_not=31
    is_in=32
    is_performing=33
    wants_talking=34
    navigating = 35


class ProjectId:
    id: str

class Exists:
    show: bool

class Person(ProjectId, Exists):
    name: str

class Position:
    x: float
    y: float

class Battery(ProjectId, Exists):
    level: float

class Server(ProjectId, Exists):
    action: str

class Joystick(ProjectId, Exists):
    connected: bool

class Navigation:
    running: bool
    x_target: bool
    y_target: bool

class speaking(ProjectId, Exists):
    running: bool

class Answer(ProjectId, Exists):
    waiting: bool

class World(ProjectId, Exists):
    id: str

class Transform(ProjectId, Exists):
    id: str

class Room(ProjectId, Exists):
    id: str
    name: Optional[str]

class DifferentialRobot(ProjectId, Exists):
    id: str

class OmniRobot(ProjectId, Exists):
    id: str

class Robot(ProjectId, Exists):
    id: str

class PathToTarget(ProjectId, Exists):
    id: str

class intention(ProjectId, Exists):
    id: str
    action: str

class rgbd(ProjectId, Exists):
    id: str
    action: str

class State(Enum):
    pending: 0
    active: 1

class Action(Enum):
    CHARGING_BATERY_IN_HOSPITAL: 0
    GOING_TO_PATIENT_ROOM_TO_CONNECT_WITH_RELATIVE: 1

class KnownPlaces(Enum):
    Consulta1: 0
