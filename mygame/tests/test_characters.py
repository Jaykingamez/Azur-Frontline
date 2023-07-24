from evennia.utils import create
from evennia.utils.test_resources import BaseEvenniaTest 

from characters import AzurCharacter 

class TestCharacters(BaseEvenniaTest):
    def setUp(self):
        super().setUp()
        self.character = create.create_object(AzurCharacter, key="testchar")

    def test_heal(self):
        self.character.hp = 0 
        self.character.hp_max = 14 
        
        self.character.heal(1)
        self.assertEqual(self.character.hp, 1)
        # make sure we can't heal more than max
        self.character.heal(100)
        self.assertEqual(self.character.hp, self.character.hp_max)
    
    def test_hurt_level(self):
        self.assertEqual(self.character.hurt_level, "|gPerfect|n")

        self.character.hp = 12
        self.assertEqual(self.character.hurt_level, "|gScraped|n")

        self.character.hp = 10
        self.assertEqual(self.character.hurt_level, "|GBruised|n")

        self.character.hp = 8
        self.assertEqual(self.character.hurt_level, "|yHurt|n")

        self.character.hp = 6
        self.assertEqual(self.character.hurt_level, "|yWounded|n")

        self.character.hp = 4
        self.assertEqual(self.character.hurt_level, "|rBadly wounded|n")

        self.character.hp = 2
        self.assertEqual(self.character.hurt_level, "|rBarely hanging on|n")

        self.character.hp = 0
        self.assertEqual(self.character.hurt_level, "|RCollapsed!|n")
    
    def test_carrying_capacity(self):
        self.assertEqual(self.character.carrying_capacity, 30)
        
    def test_at_pay(self):
        self.character.credits = 100 
        
        result = self.character.at_pay(60)
        self.assertEqual(result, 60) 
        self.assertEqual(self.character.credits, 40)
        
        # can't get more credits than we have 
        result = self.character.at_pay(100)
        self.assertEqual(result, 40)
        self.assertEqual(self.character.credits, 0)