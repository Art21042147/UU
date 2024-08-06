grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}

average_score = [float(sum(list_score) / len(list_score)) for list_score in grades]
list_student_sorted = list(sorted(students))

print(dict(zip(list_student_sorted, average_score)))
