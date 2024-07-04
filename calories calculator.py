def calculate_bmi(weight, height):
    bmi = weight / (height ** 2)
    return bmi


def calculate_calories(weight, bmi, activity_level):
    if bmi < 18.5:
        calories = 30 * weight
    elif 18.5 <= bmi < 24.9:
        calories = 35 * weight
    elif 24.9 <= bmi < 29.9:
        calories = 40 * weight
    else:
        calories = 45 * weight

    if activity_level == 'low':
        calories *= 1.2
    elif activity_level == 'moderate':
        calories *= 1.5
    elif activity_level == 'high':
        calories *= 1.8

    return calories


def suggest_diet(calories):
    suggestion = ""
    if calories < 1500:
        suggestion = "You should consume a balanced diet with sufficient calories to meet your energy needs."
    elif 1500 <= calories < 1800:
        suggestion = "Increase your calorie intake by adding nutrient-dense foods like whole grains, lean proteins, and healthy fats."
    elif 1800 <= calories < 2200:
        suggestion = "Maintain a well-balanced diet with a variety of fruits, vegetables, lean proteins, and whole grains."
    else:
        suggestion = "Ensure you are getting enough calories from healthy sources and consider adding strength training exercises to your routine."

    return suggestion


def suggest_exercise(calories):
    suggestion = ""
    if calories < 1500:
        suggestion = "Focus on incorporating regular aerobic exercises like walking, cycling, or swimming into your routine."
    elif 1500 <= calories < 1800:
        suggestion = "Include a mix of aerobic exercises and strength training to improve overall fitness."
    elif 1800 <= calories < 2200:
        suggestion = "Engage in regular cardiovascular exercises and strength training to maintain a healthy weight."
    else:
        suggestion = "Maintain a regular exercise routine that includes both aerobic exercises and strength training."

    return suggestion


# Main program
weight = float(input("Enter your weight in kilograms: "))
height = float(input("Enter your height in meters: "))
activity_level = input("Enter your activity level (low, moderate, high): ").lower()

bmi = calculate_bmi(weight, height)
calories = calculate_calories(weight, bmi, activity_level)
diet_suggestion = suggest_diet(calories)
exercise_suggestion = suggest_exercise(calories)

print("BMI:", bmi)
print("Calories per day:", calories)
print("Diet suggestion:", diet_suggestion)
print("Exercise suggestion:", exercise_suggestion)
print("Thank you! Calculate again or exit the app.")
