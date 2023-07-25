from enum import Enum

class WeaponType(Enum):
    """
    Reliable: Weapons with the Reliable quality are less likely to jam. This can be a major advantage in combat, as a jammed weapon is essentially useless.
    Overheats: Weapons with the Overheats quality can overheat if they are fired too quickly. This can cause damage to the weapon and the user, so it is important to be careful when using these weapons.
    Power Field: Weapons with the Power Field quality are surrounded by a field of energy that increases their damage and penetration. This can make them very effective against heavily armored targets.
    Primitive: Weapons with the Primitive quality are less effective against modern armor. However, they are still deadly against unarmored targets.
    Special: Weapons with the Special quality have unique abilities that set them apart from other weapons. For example, some special weapons can fire special ammunition, while others can create area-of-effect effects.
    """
    RELIABLE = "reliable"
    OVERHEATS = "overheats"
    POWER_FIELD = "power_field"
    PRIMITIVE = "primitive"
    SPECIAL = "special"

class WeaponDurability(Enum):
    """
    Standard: This is the most common type of weapon durability. Standard weapons can withstand a moderate amount of wear and tear, but they are not as durable as Durable weapons.
    Durable: Durable weapons are made with higher-quality materials and construction, making them more resistant to wear and tear. Durable weapons are a good choice for characters who expect to be in heavy combat.
    Fragile: Fragile weapons are made with low-quality materials and construction, making them more susceptible to damage. Fragile weapons are not a good choice for characters who expect to be in heavy combat.
    """
    STANDARD = "standard" # Durability 10, 10% chance of jamming
    DURABLE = "durable"   # Durability 15, 5% chance of jamming
    FRAGILE = "fragile"   # Durability 5,  20% chance of jamming