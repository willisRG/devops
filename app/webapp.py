import math

# user_bodyweight = input("Enter bodyweight: ")
# user_testweight = input("Enter workout weight: ")
# user_testreps = input("Enter workout reps: ")
user_testreps = 5
user_testweight = 150
user_age = 24
user_height = 174
user_sex = "M"
user_backsquat = 225
user_deadlift = 315
user_benchpress = 135
user_overheadpress = 95

print("Your one rep max: ", 100 * (user_testweight / (48.8 + (53.8 * math.exp(-0.075 * user_testreps)))))

def calc_onerep(in_weight, in_reps):
    one_repmax = 100*(in_weight/(48.8+(53.8*math.exp(-0.075*in_reps))))
    return one_repmax

print(calc_onerep(150, 5))
