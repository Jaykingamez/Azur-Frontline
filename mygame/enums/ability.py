from enum import Enum

class Ability(Enum):
    """
    The five base ability-bonuses and other
    abilities

    Weapon Skill (WS): Hand-to-hand and melee proficiency.
    Ballistic Skill (BS): Governs all projectile and ranged attacks.
    Strength (S): Physical strength of a character.
    Toughness (T): Resistance to physical punishment.
    Agility (Ag): Governs how quickly an individual can move as well as how well they can dodge.
    Intelligence (Int): Used to work technology and understand languages and writings.
    Perception (Per): How quickly you notice things and in how much detail.
    Will Power (WP): Your resistance to horrors and used to manifest psychic abilities.
    Fellowship (Fel): Used for interaction with other people.

    """

    PRE = "precision"       # Weapon Skill and Ballistic Skill
    BOD = "body"            # Strength and Toughness
    DEX = "dexterity"       # Agility
    MIN = "mind"            # Intelligence and Perception
    IND = "individuality"   # Will Power and Fellowship

    ARMOR = "armor"
    
    CRITICAL_FAILURE = "critical_failure"
    CRITICAL_SUCCESS = "critical_success"
    
    ALLEGIANCE_HOSTILE = "hostile"
    ALLEGIANCE_NEUTRAL = "neutral"
    ALLEGIANCE_FRIENDLY = "friendly"

ABILITY_REVERSE_MAP =  {
    "pre": Ability.PRE, 
    "bod": Ability.BOD,
    "dex": Ability.DEX,
    "min": Ability.MIN,
    "ind": Ability.IND,
}