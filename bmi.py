#functions
def calculate_bmi(height, weight):
    print("Height = " + str(height))        #str() function changes the input value to string
    print("Weight = " + str(weight))

    bmi = weight/(height**2)
    print("BMI = " + str(bmi))
    return bmi

    
def classify_bmi(bmi):
    if(bmi<18.5):
        print("Under Weight")
        return -1
    elif(bmi>=18.5 and bmi<=25.0):
        print("Normal Weight")
        return 0
    else:
        print("Over Weight")
        return 1
def main():
    print("ET0735 (DevOps for AIoT) - Lab 2 - Introduction to Python")
    bmi_calculated = calculate_bmi(weight=57, height=1.73)  #can only concatenate str to str
    bmi_status = classify_bmi(bmi_calculated)
    print()


if __name__ == "__main__":
    main()