

role = input("Enter the role for which you want to generate interview questions: ")

print("Select 1 for Junior experience level\nSelect 2 for Mid experience level\nSelect 3 for Senior experience level")

experience_level = input("Enter the experience level (junior, mid, senior): ")
if experience_level == "1":
    experience_level = "Junior"
elif experience_level == "2":
    experience_level = "Mid"
elif experience_level == "3":
    experience_level = "Senior"
else:
    print("Invalid experience level selected. Defaulting to Junior.")
    experience_level = "Junior"