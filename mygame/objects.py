from evennia import AttributeProperty, DefaultObject 
from evennia.utils.utils import make_iter
from utils.utils import get_obj_stats 
from enums.wield_location import WieldLocation
from enums.object_type import ObjType


class AzurObject(DefaultObject): 
    """ 
    Base for all Azur Frontline objects. 
    
    """ 
    inventory_use_slot = WieldLocation.BACKPACK
    size = AttributeProperty(1, autocreate=False)
    value = AttributeProperty(0, autocreate=False)
    
    # this can be either a single type or a list of types (for objects able to be 
    # act as multiple). This is used to tag this object during creation.
    obj_type = ObjType.GEAR

    # default evennia hooks

    def at_object_creation(self): 
        """Called when this object is first created. We convert the .obj_type 
        property to a database tag."""
        
        for obj_type in make_iter(self.obj_type):
            self.tags.add(self.obj_type.value, category="obj_type")

    def get_display_header(self, looker, **kwargs):
        """The top of the description""" 
        return "" 

    def get_display_desc(self, looker, **kwargs):
        """The main display - show object stats""" 
        return get_obj_stats(self, owner=looker)
    
    # custom evadventure methods

    def has_obj_type(self, objtype): 
        """Check if object is of a certain type""" 
        return objtype.value in make_iter(self.obj_type)

    def at_pre_use(self, *args, **kwargs): 
        """Called before use. If returning False, can't be used""" 
        return True 

    def use(self, *args, **kwargs): 
        """Use this object, whatever that means""" 
        pass 

    def post_use(self, *args, **kwargs): 
        """Always called after use.""" 
        pass

    def get_help(self):
        """Get any help text for this item"""
        return "No help for this item"