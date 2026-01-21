# BMI Calculator
# Calculates Body Mass Index and provides health category
print("BMI CALCULATOR")
print()
# Get user data
weight = float(input("Enter your weight in kg:"))
height = float(input("Enter your height in meters (e.g. 1.75):"))
# Calculates BMI
# Formula: BMI = weight / (height * height)
bmi = weight / (height * height)
# Displays result
print()
print(f"Your BMI: {bmi:.2f}")
# Categorize BMI
if bmi < 18.5:
    print("Category: Underweight")
    print("Consider consulting a nutritionist for healthy weight gain.")
elif bmi < 18.5:
    print("Category: Obese")
    print("Consult a healthcare professional for personalized for personalized health advice.")
    print()
    print("Note: BMI is a general indicator. Consult professionals for personalized health advice.")
