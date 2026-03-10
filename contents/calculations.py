#-------------------------------------------------#
#                   Calculations                  #
#-------------------------------------------------#

import contents.data

def lookup_training_plan(training_plan):
    return contents.data.TRAINING_PLAN_COSTS [training_plan]

def lookup_category_table(gender):
    mapped_gender = contents.data.GENDER_MAP[gender]
    return contents.data.WEIGHT_CATEGORIES[mapped_gender]

def determine_weight_category(category_table, current_weight_kg):
    for category_name, max_weight in category_table.items():
        if current_weight_kg <= max_weight:
            return category_name
        
def calculate_competition_cost(competitions_entered):
    return competitions_entered * contents.data.COMPETITION_FEE

def calculate_private_coaching(private_coaching_hours):
    return private_coaching_hours * contents.data.PRIVATE_HOURLY_RATE

def calculate_total_cost(plan_fee, competition_cost, coaching_cost):
    return plan_fee + competition_cost + coaching_cost



