#write a python menu driven script to create 2d array of 5 student mark of 5 subject to perforn following
#1.print the minimum marks of each subject.
#2.print the maximum marks of each subject.
#3.print the Average marks of each subject.
#4.print the marks which are most student get or repeated in subject.
#5.find the variance value for each subject marks.
#6.print the total of each student.

import numpy as np

# create 2D array of student marks
marks = np.zeros((5, 5))

# get input from user
for i in range(5):
    print("Enter marks from student", i+1)
    for j in range(5):
        marks[i][j] = float(input("Enter marks for subject "+ str(j+1) +": ")

#menu driven program
while True:
    print("\nmenu:")
    print("1.print the minimum marks of each subject")
    print("2.print the maximum marks of each subject")
    print("3.print the Average marks of each subject")
    print("4.print the marks which are most student get or repeated in subject")
    print("5.find the variance value for each subject marks")
    print("6.print the total of each student")
    print("7.Quit")

    if choice == 1:
        #minimum marks of each subject
        print("minimum marks of each subject")
        for j in range(5):
            print("subject",j+1,":",max(marks[:,j]))

    elif choice == 2:
        #maximum marks of each subject
        print("maximum marks of each subject")
        for j in range(5):
            print("subject",j+1,":",max(marks[:,j]))

    elif choice == 3:
        #Average marks of each subject
        print("Average marks of each subject")
        for j in range(5):
            print(subject ,j+1,,np.mean(marks[:,j]))

    elif choice == 4:
        #marks which are most student get or repeated in subject
        print("marks which are most student get or repeated in subject")
         for j in range(5):
             unique_marks, counts = np.unique(marks[:,j], return_count=True)
             max_count_index = np.argmax(counts)
             print("subject", j+1, ":", unique_marks[max_count_index])

    elif choice == 5:
        #varience of each subject marks
        print("varience of each subject marks:")
        for j in range(5):
            print("subject", j+1, ":", sum(marks[i,:]))

    elif choice == 6:
        #Total of each student
        print("Total of each student:")
        for i in range(5):
            print("student", i+1, ":",sum(marks[i,:]))

    elif choice == 7:
        #Quit program
        break

    else:
        print("Invalid choice! Try again.")
