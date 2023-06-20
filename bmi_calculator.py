def calculate_bmi(height, weight):
    bmi = weight / (height ** 2)
    return bmi

def get_bmi_category(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif bmi < 25:
        return "Normal weight"
    elif bmi < 30:
        return "Overweight"
    else:
        return "Obese"

def main():
    height = float(input("Enter your height in meters: "))
    weight = float(input("Enter your weight in kilograms: "))

    bmi = calculate_bmi(height, weight)
    category = get_bmi_category(bmi)

    print("Your BMI is: {:.2f}".format(bmi))
    print("Category: ", category)

if __name__ == "__main__":
    main()
