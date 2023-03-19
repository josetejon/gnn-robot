from enum import Enum

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
