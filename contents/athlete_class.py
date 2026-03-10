#--------------------------------------#
#             ATHLETE CLASS            #
#--------------------------------------#

""" 
This module defines the Athlete class, that represents an athlete with their attributes and 
costs. This gives an example of how to use a class to encapsulate data and its related functionality 
in an object-oriented way.
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