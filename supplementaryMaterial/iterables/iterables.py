from itertools import repeat, permutations, \
    dropwhile, takewhile, groupby, count, \
    cycle, batched, pairwise



#                                                   --repeat--
# repeat a specific task a set number of times

# for i in repeat(5, 10):
#     print(i)

values = ['Rubber Duck', 'Teapot', 'One Sock']
repeat_list = list(zip(repeat("Repeat", len(values)), values))

for index, value in repeat_list:
    print(f"{index} : {value}")
    
print(values)
print(repeat_list)




#                                                   --permutations--
# number of how many different permutations are possible within the iterable input


permutable = permutations("Python")

count_ = 0
for permute in permutable:
    print(permute)
    count_ = count_ + 1

print(count_)



#                                                   --dropwhile--
# drops elements until a condition is met

numbers = [1, 3, 5, 7, 2, 4, 6, 8]

filter_numbers = dropwhile(lambda x: x < 5, numbers)
print(list(filter_numbers)) # will include the 2 because it's a while loop

students = [('Michael', 60), ("Gladys", 85), ('Ezekiel', 70), ('Gertrude', 95), ('Concepción', 70), ('Sylvia', 95)]
filter_students = dropwhile(lambda students: students[1] < 75, students)
print(list(filter_students))



#                                                   --takewhile--
# do something until a condition is met
filter_students_two = takewhile(lambda student: student[1] < 80, students)
print(list(filter_students_two))



#                                                   --groupby--
# group data into distinct groups
sorted_students = sorted(students, key=lambda student: student[1])
group_of_students = groupby(sorted_students, lambda student: student[1])

for grade, group in group_of_students:
    print(f"Grade {grade} : {[student[0] for student in group]}")



#                                                   --count--
# creates counter variables that can iterate in custom amount of steps; needs next()

counter = count(start=2, step=3)

for _ in range(10):
    print(next(counter))

names = ['Alice', 'Bob', 'Charlie', 'David', 'Ezekiel', 'Fernando', 'Gabriel']
id_counter = count(start=1)
mapping = {name: next(id_counter) for name in names}
print(mapping)



#                                                   --cycle--
#  continue to loop through an iterable

cycler = cycle(values)
for i in range(10):
    print(next(cycler))
    
developer_cycle = cycle(names)
for week in range(1, 53):
    print(f"Week: {week} | Code Reviewer: {next(developer_cycle)}")
    


#                                                   --batched--
# allows us to link up elements into a tuple

values_two = ['duck', 'yellow', 'tea', 'green', 'sock', 'white']
organized_list = list(batched(values_two, 2))
print(organized_list)



#                                                   --pairwise--
# pair elements together based on last element
values_three = 'QSCWDVEFBRGNTHMYJZUKXILAOP'
linked_file = dict(pairwise(sorted(values_three)))
print(linked_file)