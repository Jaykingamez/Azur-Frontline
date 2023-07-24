from enums.ability import Ability, ABILITY_REVERSE_MAP
import unittest

class TestAbility(unittest.TestCase):
    def test_ability(self):
        self.assertEqual(Ability.PRE.value, "precision")
        self.assertEqual(Ability.BOD.value, "body")
        self.assertEqual(Ability.DEX.value, "dexterity")
        self.assertEqual(Ability.MIN.value, "mind")
        self.assertEqual(Ability.IND.value, "individuality")

        self.assertEqual(Ability.ARMOR.value, "armor")
        
        self.assertEqual(Ability.CRITICAL_FAILURE.value, "critical_failure")
        self.assertEqual(Ability.CRITICAL_SUCCESS.value, "critical_success")
        self.assertEqual(Ability.ALLEGIANCE_HOSTILE.value, "hostile")
        self.assertEqual(Ability.ALLEGIANCE_NEUTRAL.value, "neutral")
        self.assertEqual(Ability.ALLEGIANCE_FRIENDLY.value, "friendly")

    def test_ability_reverse_map(self):
        self.assertEqual(ABILITY_REVERSE_MAP.get("pre"), Ability.PRE)
        self.assertEqual(ABILITY_REVERSE_MAP.get("bod"), Ability.BOD)
        self.assertEqual(ABILITY_REVERSE_MAP.get("dex"), Ability.DEX)
        self.assertEqual(ABILITY_REVERSE_MAP.get("min"), Ability.MIN)
        self.assertEqual(ABILITY_REVERSE_MAP.get("ind"), Ability.IND)



