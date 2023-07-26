"""
Test the EvAdventure equipment handler.

"""

from evennia.utils.test_resources import BaseEvenniaTest
from evennia.utils import create 

from enums.ability import Ability
from enums.wield_location import WieldLocation
from objects import AzurWeapon, AzurArmor
from characters import AzurCharacter
from enums.object_type import ObjType
#from equipment import EquipmentError
#from mixins import EvAdventureMixin


class TestEquipment(BaseEvenniaTest):
    def setUp(self):
        super().setUp()
        self.character = create.create_object(AzurCharacter, key='testchar')
        self.helmet = create.create_object(AzurArmor, key="helmet")
        self.helmet.inventory_use_slot = WieldLocation.HEAD
        self.weapon = create.create_object(AzurWeapon, key="weapon") 

    def test_count_slots(self):
        self.assertEqual(self.character.equipment.count_slots(), 0)

    def test_max_slots(self):
        self.assertEqual(self.character.equipment.max_slots, 30)
        setattr(self.character, Ability.BOD.value, 50)
        self.assertEqual(self.character.equipment.max_slots, 75)

    def test_add_remove(self):
        self.character.equipment.add(self.helmet)
        self.assertEqual(self.character.equipment.slots[WieldLocation.BACKPACK], [self.helmet])
        self.character.equipment.remove(self.helmet)
        self.assertEqual(self.character.equipment.slots[WieldLocation.BACKPACK], [])

    def test_move_get_current_slot(self):
        self.character.equipment.add(self.helmet)
        self.assertEqual(
            self.character.equipment.get_current_slot(self.helmet), WieldLocation.BACKPACK
        )
        self.character.equipment.move(self.helmet)
        self.assertEqual(self.character.equipment.get_current_slot(self.helmet), WieldLocation.HEAD)

    """
    def test_get_wearable_or_wieldable_objects_from_backpack(self):
        self.character.equipment.add(self.helmet)
        self.character.equipment.add(self.weapon)

        self.assertEqual(
            self.character.equipment.get_wieldable_objects_from_backpack(), [self.weapon]
        )
        self.assertEqual(
            self.character.equipment.get_wearable_objects_from_backpack(), [self.helmet]
        )

        self.assertEqual(
            self.character.equipment.all(),
            [
                (None, WieldLocation.LEFT_HAND),
                (None, WieldLocation.RIGHT_HAND),
                (None, WieldLocation.TWO_HANDS),
                (None, WieldLocation.UPPER_BODY),
                (None, WieldLocation.LOWER_BODY),
                (None, WieldLocation.HEAD),
                (self.helmet, WieldLocation.BACKPACK),
                (self.weapon, WieldLocation.BACKPACK),
            ],
        )
        """

    def _get_empty_slot(self):
        return {
            WieldLocation.BACKPACK: [],
            WieldLocation.LEFT_HAND: None,
            WieldLocation.RIGHT_HAND: None,
            WieldLocation.TWO_HANDS: None,
            WieldLocation.UPPER_BODY: None,
            WieldLocation.LOWER_BODY: None,
            WieldLocation.HEAD: None,
        }