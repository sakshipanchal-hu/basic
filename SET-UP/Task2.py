marks = int(input("Enter your marks: "))

if marks == 100:
    print("Perfect Score!")

if marks != 0:
    print("You attempted the exam.")

if marks > 50:
    print("You passed the exam.")

if marks < 35:
    print("You failed the exam.")

if marks >= 75:
    print("Grade: A")

if marks <= 35:
    print("Need Improvement")

print("\nComparison Results:")
print("marks == 50 :", marks == 50)
print("marks != 50 :", marks != 50)
print("marks > 50  :", marks > 50)
print("marks < 50  :", marks < 50)
print("marks >= 50 :", marks >= 50)
print("marks <= 50 :", marks <= 50)