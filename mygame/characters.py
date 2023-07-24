
from evennia import DefaultCharacter, AttributeProperty
from evennia.contrib.rpg.dice import roll
from utils.rules import DeathSystem

class LivingMixin:

    # makes it easy for mobs to know to attack PCs
    is_pc = False  

    @property
    def hurt_level(self):
        """
        String describing how hurt this character is.
        """
        percent = max(0, min(100, 100 * (self.hp / self.hp_max)))
        if 95 < percent <= 100:
            return "|gPerfect|n"
        elif 80 < percent <= 95:
            return "|gScraped|n"
        elif 60 < percent <= 80:
            return "|GBruised|n"
        elif 45 < percent <= 60:
            return "|yHurt|n"
        elif 30 < percent <= 45:
            return "|yWounded|n"
        elif 15 < percent <= 30:
            return "|rBadly wounded|n"
        elif 1 < percent <= 15:
            return "|rBarely hanging on|n"
        elif percent == 0:
            return "|RCollapsed!|n"

    def heal(self, hp): 
        """ 
        Heal hp amount of health, not allowing to exceed our max hp
         
        """ 
        damage = self.hp_max - self.hp 
        healed = min(damage, hp) 
        self.hp += healed 
        
        self.msg(f"You heal for {healed} HP.") 
        
    def at_pay(self, amount):
        """When paying credits, make sure to never detract more than we have"""
        amount = min(amount, self.credits)
        self.credits -= amount
        return amount
        
    def at_attacked(self, attacker, **kwargs): 
        """Called when being attacked and combat starts."""
        pass
    
    def at_damage(self, damage, attacker=None):
        """Called when attacked and taking damage."""
        self.hp -= damage  
        
    def at_defeat(self): 
        """Called when defeated. By default this means death."""
        self.at_death()
        
    def at_death(self):
        """Called when this thing dies."""
        # this will mean different things for different living things
        pass 
        
    def at_do_loot(self, looted):
        """Called when looting another entity""" 
        looted.at_looted(self)
        
    def at_looted(self, looter):
        """Called when looted by another entity""" 
        
        # default to stealing some credits 
        max_steal = roll("1d10") 
        stolen = self.at_pay(max_steal)
        looter.credits += stolen

class AzurCharacter(LivingMixin, DefaultCharacter):
    """ 
    A character to use for Azur Frontline 
    """
    is_pc = True 

    precision = AttributeProperty(20) 
    body = AttributeProperty(20)
    dexterity = AttributeProperty(20)
    mind = AttributeProperty(20)
    individuality = AttributeProperty(20)
    
    hp = AttributeProperty(12 + 2) 
    hp_max = AttributeProperty(12 + 2)

    movement_speed = 2
    armor = 2
    fate_points = 2

    charclass = AttributeProperty("Assault Rifle")
    charrace = AttributeProperty("Doll")

    background = ""
    knowledge_dict = {}
    
    level = AttributeProperty(1)
    xp = AttributeProperty(0)
    credits = AttributeProperty(0)

    def at_defeat(self):
        """Characters roll on the death table"""
        if self.location.allow_death:
            # this allow rooms to have non-lethal battles
            DeathSystem.roll_death(self)
        else:
            self.location.msg_contents(
                "$You() $conj(collapse) in a heap, alive but beaten.",
                from_obj=self)
            self.heal(self.hp_max)
            
    def at_death(self):
        """We rolled 'dead' on the death table."""
        self.location.msg_contents(
            "$You() collapse in a heap, embraced by death.",
            from_obj=self) 
        # TODO - go back into chargen to make a new character!      
