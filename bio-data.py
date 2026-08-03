name = input("Enter your name: ")
age = int(input("Enter your age: "))
gender = input("Enter your gender: ")
mother_name = input("Enter your mother name: ")
father_name = input("Enter your father name: ")
phone = input("Enter your phone number: ")
email = input("Enter your email id: ")
address = input("Enter your address: ")
city = input("Enter your city: ")
state = input("Enter your state: ")

student = input("Are you a School student or College student? (school/college): ")

if student.lower() == "school":
    school = input("Enter your school name: ")
    standard = input("Enter your standard: ")
    section = input("Enter your section: ")
else:
    college = input("Enter your college name: ")
    degree = input("Enter your degree: ")
    year = input("Enter your year: ")

skill = input("Enter your skills: ")
hobbies = input("Enter your hobbies: ")
languages = input("Enter your languages: ")

print("\n========== BIODATA ==========")
print("Name          :", name)
print("Age           :", age)
print("Gender        :", gender)
print("Mother Name   :", mother_name)
print("Father Name   :", father_name)
print("Phone Number  :", phone)
print("Email ID      :", email)
print("Address       :", address)
print("City          :", city)
print("State         :", state)

if student.lower() == "school":
    print("School        :", school)
    print("Standard      :", standard)
    print("Section       :", section)
else:
    print("College       :", college)
    print("Degree        :", degree)
    print("Year          :", year)

print("Skills        :", skill)
print("Hobbies       :", hobbies)
print("Languages     :", languages)
print("========== THANK YOU ==========")