student_scores = input("Input a list of student scores ").split()
for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n])
print(student_scores)

highest_number = 0
for highest in student_scores:
    if highest > highest_number:
       highest_number = highest
print(f"The highest score in the class is : {highest_number}") 
