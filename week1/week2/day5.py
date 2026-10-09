print("====Exercise 1 LIST OPERATIONS====")


fruits = ["pineapple","mango","pawpaw","apple","banana"]
fruits.sort()
print(fruits)

fruits.reverse()
print(fruits)

fruits.append("guava")
print(fruits)


print("===Exercise 2 DICTIONARY WORK===")

student = {"name":"Moses","age":"29","grade":"A-"}
for key, value in student.items():
    print(key, ":", value)


print("===Exercise 3:NESTED DATA===")

students = [
        {"name":"Moses","grade":"A-"},
        {"name":"Sakwa","grade":"A"},
        {"name":"Aston","grade":"B"}
    ]
for student in students :
    print(student["name"], ":", student["grade"])


print("====Exercise 4:CHALLANGE====")

phonebook = {"Moses":"0791935747","Philip":"0717805167","Jairus":"0727472373"}
print("===CONTACTS===")
for name, number in phonebook.items():
    print(f"{name} : {number}")