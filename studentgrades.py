# Tuple of student names and grades
students = (
    ("Ali", 85),
    ("Bob", 90),
    ("Charlie", 78),
    ("Muji", 92)
)

print("Student Grades:")

# Display each student's name and grade
for student in students:
    name, grade = student
    print(f"{name}: {grade}")

# Example: Find the highest grade
highest_grade = max(students, key=lambda x: x[1])
print(f"\nTop student: {highest_grade[0]} with a grade of {highest_grade[1]}")
