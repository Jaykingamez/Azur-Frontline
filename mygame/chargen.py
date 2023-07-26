from evennia import EvMenu
from menu_text import Background
from enums.job import Job
from enums.race import Race

class DollCreator:
    def __init__(self):
        self.precision = 20
        self.body = 20
        self.dexterity = 20
        self.mind = 20
        self.individuality = 20

        self.hp = 12 + (self.body / 10)
        self.hp_max = 12 + (self.body / 10)

        self.armor = 2
        self.movement_speed = self.dexterity / 10
        self.fate_points = self.individuality / 1
        
        self.xp = 0
        self.level = 1
        self.credits = 0

        self.char_class = Job.AR
        self.char_race = Race.DOLL

    def update_precision(self, precision):
        self.precision = precision

    def update_body(self, body):
        self.body = body
        self.hp = 12 + (self.body / 10)
        self.hp_max = 12 + (self.body / 10)
    
    def update_dexterity(self, dexterity):
        self.dexterity = dexterity
        self.movement_speed = self.dexterity / 10
    
    def update_mind(self, mind):
        self.mind = mind
    
    def update_individuality(self, individuality):
        self.individuality = individuality
        self.fate_points = self.individuality / 1

def node_appearance(caller, raw_string, **kwargs):
    pass

def _set_gun_type(caller, raw_string, **kwargs):
    choice = kwargs["choice"]
    tmp_character = kwargs["tmp_character"]

    if choice is Job.AR:
        tmp_character.char_class = Job.AR
    elif choice is Job.SMG:
        tmp_character.char_class = Job.SMG
    elif choice is Job.RF:
        tmp_character.char_class = Job.RF
    elif choice is Job.HG:
        tmp_character.char_class = Job.HG
    elif choice is Job.MG:
        tmp_character.char_class = Job.MG
    elif choice is Job.SG:
        tmp_character.char_class = Job.SG
    else:
        return ("node_select_gun", kwargs) # Something is very wrong
    return ("node_appearance", kwargs)

def node_select_gun(caller, raw_string, **kwargs):
    text = "What's your favourite type of firearm?"

    options = [
        {
            "desc": "Assault Rifle",
            "goto": ("_set_gun_type", {"tmp_character" : kwargs["tmp_character"],
                                       "choice" : Job.AR})
        },
        {
            "desc": "Submachine Gun",
            "goto": ("_set_gun_type", {"tmp_character" : kwargs["tmp_character"],
                                       "choice" : Job.SMG})
        },
        {
            "desc": "Rifle",
            "goto": ("_set_gun_type", {"tmp_character" : kwargs["tmp_character"],
                                       "choice" : Job.RF})
        },
        {
            "desc": "Handgun",
            "goto": ("_set_gun_type", {"tmp_character" : kwargs["tmp_character"],
                                       "choice" : Job.HG})
        },
        {
            "desc": "Machine Gun",
            "goto": ("_set_gun_type", {"tmp_character" : kwargs["tmp_character"],
                                       "choice" : Job.MG})
        },
        {
            "desc": "Shotgun",
            "goto": ("_set_gun_type", {"tmp_character" : kwargs["tmp_character"],
                                       "choice" : Job.SG})
        }
    ]

    return text, options

def _set_background(caller, raw_string, **kwargs):
    tmp_character = kwargs["tmp_character"]
    choice = kwargs["choice"]

    if choice is "Corporate Member":
        tmp_character.update_mind(tmp_character.mind + 20)
        tmp_character.update_individuality(tmp_character.individuality + 20)
    elif choice is "Emergency Worker":
        tmp_character.update_mind(tmp_character.mind + 20)
        tmp_character.update_dexterity(tmp_character.dexterity + 20)
    elif choice is "Hazard Worker":
        tmp_character.update_body(tmp_character.body + 20)
        tmp_character.update_mind(tmp_character.mind + 20)
    elif choice is "IOP Elite":
        tmp_character.update_precision(tmp_character.precision + 20)
        tmp_character.update_individuality(tmp_character.individuality + 20)

    return "node_select_gun", kwargs

def node_confirm_background(caller, raw_string, **kwargs):
    choice = kwargs["choice"]
    text = "This is a placeholder background"

    if choice is "Corporate Member":
        text = Background.CORPORATE_MEMBER
    elif choice is "Emergency Worker":
        text = Background.EMERGENCY_WORKER
    elif choice is "Hazard Worker":
        text = Background.HAZARD_WORKER
    elif choice is "IOP Elite":
        text = Background.IOP_ELITE
    else:
        text = Background.NEW

    options = [
        {
            "desc": "Confirm Choice",
            "goto": (_set_background, kwargs)
        },
        {
            "desc": "I want to pick something else",
            "goto": ("node_background", kwargs)
        }
    ]
    
    
    return text, options


def node_background(caller, raw_string, **kwargs): 

    tmp_character = kwargs["tmp_character"]

    text = ("Welcome to this hellhole. Who were you before you came here?",
            "Do pick an option! Why did you type help?")

    options = [
        {
           "desc": "Corporate Member", 
           "goto": ("node_confirm_background", {"tmp_character" : tmp_character, 
                                           "choice" : "Corporate Member"})
        },
        {
            "desc": "Emergency Worker",
            "goto": ("node_confirm_background", {"tmp_character" : tmp_character, 
                                           "choice" : "Emergency Worker"})
        },
        {
            "desc": "Hazard Worker",
            "goto": ("Node_confirm_background", {"tmp_character" : tmp_character, 
                                           "choice" : "Hazard Worker"})
        },
        {
            "desc": "IOP Elite",
            "goto": ("Node_confirm_background", {"tmp_character" : tmp_character, 
                                           "choice" : "IOP Elite"})
        },
    ]

    return text, options

def start_chargen(caller, session=None):
    """
    This is a start point for spinning up the chargen from a command later.

    """

    menutree = {}  # TODO!

    # this generates all random components of the character
    tmp_character = DollCreator()

    EvMenu(caller, menutree, session=session, tmp_character=tmp_character)


        
