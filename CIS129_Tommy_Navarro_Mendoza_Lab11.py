# Storing grades
grades = [85, 90, 71, 75, 80, 85]  # Example grades
with open("grades.txt", "w") as file:
    for grade in grades:
        file.write(str(grade) + "\n")


# calculating total, count, and average
with open("grades.txt", "r") as file:
    grades = [int(line.strip()) for line in file]

total = sum(grades)
count = len(grades)
average = total / count

print("Individual Grades:")
for grade in grades:
    print(grade)

print("\nTotal:", total)
print("Count:", count)
print("Average:", average)


import csv

# Function to input student data and write to CSV
def inpt_and_write_csv():
    with open("grades.csv", "w", newline="") as file:
        writer = csv.writer(file)
        while True:
            first_name = input("Enter student's first name (or 'quit' to exit): ")
            if first_name.lower() == "quit":
                break
            last_name = input("Enter student's last name: ")
            exam_grades = [float(input(f"Enter {first_name}'s grade for exam {i+1}: ")) for i in range(3)]
            writer.writerow([first_name, last_name] + exam_grades)

# Call the function
inpt_and_write_csv()
