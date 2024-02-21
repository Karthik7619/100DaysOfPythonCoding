# Input a Python list of student heights
student_heights = input().split()
for n in range(0, len(student_heights)):
    student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆

# Write your code below this row 👇
count = 0
for height in student_heights:
    total_height = + height
    count = count + 1

Avgheight = total_height / count
roundAvgheight = round(Avgheight)
print(f"total height = {total_height}")
print(f"number of students = {count}")
print(f"average height = {roundAvgheight}")
