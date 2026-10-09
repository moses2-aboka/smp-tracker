print("===WEEK 1 EXERCISE 1===")


name = "Moses Aboka"
age = 29
city = "Nairobi"

print(f"My name is {name}, I am {age}, from {city}.")


# 90+ = A, 75+ = B, 60+ = C, below 60 = F
score = 78
if score >= 90:
    print("A")
elif score >= 75:
    print("B") 



print("=== EXERCISE 3 ===") 


# Print the first 10 even numbers using a loop

for i in range (1, 21):
    if i % 2 == 0:
        print(i)



print("=== EXERCISE 4 ===")

num = int(input("Enter a number :"))
for i in range (1, 11):
    print(f"{num} x{i} =  {num * i}")


