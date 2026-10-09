
print("EXERCISE 1: Functions")
def greet (name):
   return f"Hello, {name}. Welcome to the program."

print (greet("Moses"))
print (greet("Albert"))


print("\nEXERCISE 2: Default parameters")
def power(base, exp = 2):
   return base ** exp
print(power(3))
print(power(2, 20))


print("\nEXERCISE 3: List Comprehensions")
evens = [n for n in range (1,31) if n % 2 == 0]
print(evens)
squares = [n ** 2 for n in evens]
print(squares)


print("\nEXERCISE 4: Challange")
def analyse (scores):
   return {
      "average": sum(scores) / len(scores),
      "highest": max(scores),
      "lowest": min(scores)
   }

result = analyse([68, 75, 88, 94, 52, 60, 86, 72, 98, 62])
for k, v in result.items():
   print(f"{k} : {v}")
   