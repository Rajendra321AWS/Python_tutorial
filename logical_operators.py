"""In this program we are using logical operators"""
def main():
    age = 20
    has_id = True
    Is_student = False

# using AND operator: bith conditions must be true
    if age >= 18 and has_id:
        print("you are allowed to enter")
    else:
        print("entry denaid")

# OR operator: at least one condition must be true
    if age < 18 or Is_student:
        print("you are eligible for discount")
    else:
        print("no discount available")

#NOT operator: reverse the above condition
    if not has_id:
        print("you must bring an ID")
    else:
        print("ID verified")

if __name__ == "__main__":
    main()
