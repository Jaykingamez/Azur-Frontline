from enum import Enum

class WieldLocation(Enum):
    BACKPACK = "backpack"               # Carry more stuff
    LEFT_HAND = "LEFT_HAND"               # One-handed Weapons
    RIGHT_HAND = "RIGHT_HAND"             # One-handed Weapons
    TWO_HANDS = "two_handed_weapons"    # Assault Rifles
    UPPER_BODY = "upper_body"           # Body Armour
    LOWER_BODY = "lower_body"           # Pants/Skirts
    HEAD = "head"                       # helmets/hats