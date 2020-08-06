import csv
from csv import DictReader
from json import loads, dumps

books_list: list = []
 # books = DictReader(open('books-39204-271043.csv', 'r'))
with open('books_test.csv') as books:
    b = DictReader(books)

    # Итерируемся по данным делая из них словари
    for row in b:
        books_list.append(dict(row))

with open('users-39204-8e2f95.json', 'r') as students:
    std = students.read()
    students_list = loads(std)

i = 0
student = []
for stud in students_list:
    print(i)
    if stud != None:
        st = dict(stud)
        try:
            bl = books_list[i]
            student.append([{
                        "name": st.get('name'),
                        "gender": st.get('gender'),
                        "address": st.get('address'),
                        "books":
                            [
                              {
                                "title": bl.get('Title'),
                                "author": bl.get('Author'),
                                "height": bl.get('Height')
                              }
                            ]
                        }])
        except IndexError:
            student.append([{
                "name": st.get('name'),
                "gender": st.get('gender'),
                "address": st.get('address'),
                "books":
                    [
                ]
            }])
    i += 1

with open('result.json', 'a') as file:
    s = dumps(student, indent=4)
    file.write(s)
