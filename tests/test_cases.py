#-------------------------------#
#           TEST CASES          #
#-------------------------------#

"""
This module contains test cases that I performed on data as it was created to ensure that it worked correctly
before moving on.
Includes tests:
1. To ascertain if the dictionary look ups were working as expected.
2. That calculations worked as expected.
3. That the Athlete class initialised and updated with new data.
"""

from contents.athlete_class import Athlete
from contents.data import GENDER_MAP, WEIGHT_CATEGORIES
import contents.calculations

# Test Case 1: Dictionary calls correct category
weight = 75
gender = "Male"

gender_key = GENDER_MAP[gender]
for category, limit in WEIGHT_CATEGORIES[gender_key].items():
    if weight <= limit:
        print(gender_key)
        print(category)
        break

# Test Case 2: Dictionary calls correct category
weight = 100.01
gender = "Trans-male"

gender_key = GENDER_MAP[gender]
for category, limit in WEIGHT_CATEGORIES[gender_key].items():
    if weight <= limit:
        print(gender_key)
        print(category)
        break

# Test Case 3: Dictionary calls correct category
weight = 57
gender = "Female"

gender_key = GENDER_MAP[gender]
for category, limit in WEIGHT_CATEGORIES[gender_key].items():
    if weight <= limit:
        print(gender_key)
        print(category)
        break

# Test Case 4: Dictionary calls correct category
weight = 47
gender = "Trans-female"

gender_key = GENDER_MAP[gender]
for category, limit in WEIGHT_CATEGORIES[gender_key].items():
    if weight <= limit:
        print(gender_key)
        print(category)
        break

# Test Case 5: Dictionary calls correct category
weight = 100
gender = "Male"

gender_key = GENDER_MAP[gender]
for category, limit in WEIGHT_CATEGORIES[gender_key].items():
    if weight <= limit:
        print(gender_key)
        print(category)
        break

# Test Case 6: Dictionary calls correct category
weight = 69.90
gender = "Trans-female"

gender_key = GENDER_MAP[gender]
for category, limit in WEIGHT_CATEGORIES[gender_key].items():
    if weight <= limit:
        print(gender_key)
        print(category)
        break

#Test Case 7 - Calculate total cost with all components
plan_fee = 40
competition_cost = 45
coaching_cost = 125
total_cost = plan_fee + competition_cost + coaching_cost
print(total_cost)  # Output: 210

#Test Case 8 - Test calculation functions with sample data
plan_fee = contents.calculations.lookup_training_plan("Advanced")
competition_cost = contents.calculations.calculate_competition_cost(1)
coaching_cost = contents.calculations.calculate_private_coaching(2)
total_cost = contents.calculations.calculate_total_cost(plan_fee, competition_cost, coaching_cost)
print(total_cost)  # Output: 120

#Test Case 5: Athlete class initialisation
athlete1 = Athlete(
    name="John Doe",
    gender="Male",
    current_weight_kg=75.0,
    training_plan="Intermediate",
    competitions_entered=3,
    private_coaching_hours=5.0
)
print(athlete1.name)  # Output: John Doe
print(athlete1.gender)  # Output: Male
print(athlete1.current_weight_kg)  # Output: 75.0
print(athlete1.training_plan)  # Output: Intermediate
print(athlete1.competitions_entered)  # Output: 3
print(athlete1.private_coaching_hours)  # Output: 5.0
print(athlete1.weight_category)  # Output: None
print(athlete1.plan_fee)  # Output: 0.0
print(athlete1.competition_cost)  # Output: 0.0
print(athlete1.coaching_cost)  # Output: 0.0
print(athlete1.total_cost)  # Output: 0.0   

#Test Case 6: Athlete class initialisation with default private coaching hours
athlete2 = Athlete(
    name="Jane Smith",
    gender="    Female",
    current_weight_kg=60.0,
    training_plan="Advanced",
    competitions_entered=5
)
print(athlete2.name)  # Output: Jane Smith
print(athlete2.gender)  # Output: Female
print(athlete2.current_weight_kg)  # Output: 60.0
print(athlete2.training_plan)  # Output: Advanced
print(athlete2.competitions_entered)  # Output: 5
print(athlete2.private_coaching_hours)  # Output: 0.0 (default value)
print(athlete2.weight_category)  # Output: None
print(athlete2.plan_fee)  # Output: 0.0
print(athlete2.competition_cost)  # Output: 0.0
print(athlete2.coaching_cost)  # Output: 0.0
print(athlete2.total_cost)  # Output: 0.0
