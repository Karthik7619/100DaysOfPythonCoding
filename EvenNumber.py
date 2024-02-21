#Program to sum even numbers
target = int(input())
total = 0
for number in range (2,target+1,2):
  total+=number

print(total)