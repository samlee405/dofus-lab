from enum import auto, Enum
import sqlalchemy


class Stat(Enum):
    VITALITY = auto()
    AP = auto()
    MP = auto()
    INITIATIVE = auto()
    PROSPECTING = auto()
    RANGE = auto()
    SUMMON = auto()
    WISDOM = auto()
    STRENGTH = auto()
    INTELLIGENCE = auto()
    CHANCE = auto()
    AGILITY = auto()
    AP_PARRY = auto()
    AP_REDUCTION = auto()
    MP_PARRY = auto()
    MP_REDUCTION = auto()
    CRITICAL = auto()
    HEALS = auto()
    LOCK = auto()
    DODGE = auto()
    PCT_FINAL_DAMAGE = auto()
    POWER = auto()
    CRITICAL_DAMAGE = auto()
    NEUTRAL_DAMAGE = auto()
    EARTH_DAMAGE = auto()
    FIRE_DAMAGE = auto()
    WATER_DAMAGE = auto()
    AIR_DAMAGE = auto()
    REFLECT = auto()
    TRAP_DAMAGE = auto()
    TRAP_POWER = auto()
    PUSHBACK_DAMAGE = auto()
    PCT_SPELL_DAMAGE = auto()
    PCT_WEAPON_DAMAGE = auto()
    PCT_RANGED_DAMAGE = auto()
    PCT_MELEE_DAMAGE = auto()
    NEUTRAL_RES = auto()
    PCT_NEUTRAL_RES = auto()
    EARTH_RES = auto()
    PCT_EARTH_RES = auto()
    FIRE_RES = auto()
    PCT_FIRE_RES = auto()
    WATER_RES = auto()
    PCT_WATER_RES = auto()
    AIR_RES = auto()
    PCT_AIR_RES = auto()
    CRITICAL_RES = auto()
    PUSHBACK_RES = auto()
    PCT_RANGED_RES = auto()
    PCT_MELEE_RES = auto()


class Element(Enum):
    NEUTRAL = auto()
    EARTH = auto()
    FIRE = auto()
    WATER = auto()
    AIR = auto()


StatEnum = sqlalchemy.Enum(Stat)
