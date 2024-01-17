from enum import Enum

class DevStatus(Enum):
    NOT_READY_FOR_USE_IN_BUILD = -1
    NOT_READY_FOR_PRODUCTION_NOT_SAFE_USAGE = 0
    READY_FOR_PRODUCTION_AND_USE = 1