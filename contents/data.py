#--------------------------------------#
#  CONSTANTS, DICTIONARIES AND LISTS.  #
#--------------------------------------#

"""This file contains all the constants, dictionaries and lists used in the 
Judo App. It serves as a central location for all static data, making it easier 
to manage and update as needed. By keeping this information separate from the 
main logic of the application, we can ensure that the code remains clean and 
organised.

Do not change key names as they are used in the calculations and test cases. """

# -- CONSTANTS -- #

COMPETITION_FEE = 15
PRIVATE_HOURLY_RATE = 25

# -- LISTS -- #

GENDER = ["Male", "Female", "Trans-male", "Trans-female"]
TRAINING_PLANS = ["Beginner", "Intermediate", "Advanced", "Professional"]

# -- DICTIONARIES -- #

TRAINING_PLAN_COSTS = {
    "Beginner": 20,
    "Intermediate": 40,
    "Advanced": 65,
    "Professional": 90
}

GENDER_MAP = {
    "Male": "Male",
    "Female": "Female",
    "Trans-male": "Male",
    "Trans-female": "Female"
}

# NOTE:
# Weight categories must remain in ascending order of weight as algorithms
# rely on this to determine the correct category.

WEIGHT_CATEGORIES = {
        "Male": {
            "Extra Lightweight" : 60,
            "Half Lightweight" : 66,
            "Lightweight" : 73,
            "Half Middleweight" : 81,
            "Middleweight" : 90,
            "Half Heavyweight" : 100,
            "Heavyweight" : float("inf")
        },
                 
        "Female": {
            "Extra Lightweight" : 48,
            "Half Lightweight" : 52,
            "Lightweight" : 57,
            "Half Middleweight" : 63,
            "Middleweight" : 70,
            "Half Heavyweight" : 78,
            "Heavyweight" : float("inf")
        }
}
