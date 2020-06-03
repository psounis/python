semester_grades = [4, 6, 3, 8, 10]

passed = 0
sum_grades = 0
for grade in semester_grades:
    if grade >= 5:
        passed += 1
        sum_grades += grade

print("I've succeeded in " + str(passed) + " lessons")
print("My average is " + str(sum_grades/passed))
