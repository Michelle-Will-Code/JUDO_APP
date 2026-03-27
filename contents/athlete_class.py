#--------------------------------------#
#             ATHLETE CLASS            #
#--------------------------------------#

""" 
This module defines the Athlete class, that represents an athlete with their attributes and 
functions. This gives an example of how to use a class to encapsulate data and its related functionality 
in an object-oriented way.

Currently the Athlete class shows only the attributes and not behaviours tied to them. These functions 
are in calculations.py to help demonstrate functional programming. Outside of assignment parameters, I 
would have placed most of the calculations within this class.
"""

class Athlete:
    #initiliases class with given attibutes and sets default values
    def __init__(
            self, 
            name: str, 
            gender: str, 
            current_weight_kg: float, 
            training_plan: str, 
            competitions_entered: int, 
            private_coaching_hours: float = 0.0
    ):
            
        # Inputs for the athlete class, set by user input in main.py     
        self.name = name
        self.gender = gender
        self.current_weight_kg = current_weight_kg
        self.training_plan = training_plan
        self.competitions_entered = competitions_entered
        self.private_coaching_hours = private_coaching_hours

        # Calculations set by the calculations.py module, default values set to 0 or None
        self.weight_category = None
        self.plan_fee = 0.0
        self.competition_cost = 0.0
        self.coaching_cost = 0.0
        self.total_cost = 0.0