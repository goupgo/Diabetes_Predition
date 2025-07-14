def New_BMI(bmi):
    NewBMI = ["Obesity 1", "Obesity 2", "Obesity 3", "Overweight", "Underweight"]

    if bmi < 18.5:
        return  0, 0, 0, 0, 1
    elif 18.5 < bmi <= 24.9:
        return 0, 0, 0, 0, 0
    elif 24.9 < bmi <= 29.9:
        return 0, 0, 0, 1, 0
    elif 29.9 < bmi <= 34.9:
        return 1, 0, 0, 0, 0
    elif 34.9 < bmi <= 39.9:
        return 0, 1, 0, 0, 0
    elif bmi > 34.9:
        return 0, 0, 1, 0, 0



def New_Insulin(insulin):
    if insulin >= 16 and insulin <= 166:
        return 1
    else:
        return 0
    


def New_Glucose(glucose):
    if glucose <= 70:
        return 1, 0, 0, 0
    elif 70 < glucose <= 99:
        return 0, 1, 0, 0
    elif 99 < glucose <= 126:
        return 0, 0, 1, 0
    elif glucose > 126:
        return 0, 0, 0, 1


