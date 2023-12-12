student_scores = input("Enter scores: ").split()
for n in range(0, len(student_scores)):
    student_scores[n] = int(student_scores[n])
    
max_number = 0
for scores in student_scores:
    if max_number < scores:
        max_number = scores
print(max_number)