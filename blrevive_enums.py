
from enum import Enum


class Gear(Enum):
    P1 = 0
    S1 = 1
    P2 = 2
    S2 = 3
    P3 = 4
    S3 = 5


class UIGear(Enum):
    m_bmToggleBtnPrimary1 = 0
    m_bmToggleBtnSecondary1 = 1
    m_bmToggleBtnPrimary2 = 2
    m_bmToggleBtnSecondary2 = 3
    m_bmToggleBtnPrimary3 = 4
    m_bmToggleBtnSecondary3 = 5


class UIAttachment(Enum):
    RECEIVER = 0
    MUZZLE = 1
    BARREL = 2
    GRIP = 3
    MAGAZINE = 4
    SCOPE = 5
    STOCK = 6
    TAG = 7
    CAMO = 8
