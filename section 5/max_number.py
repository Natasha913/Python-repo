student_scores = [150 , 142, 500, 164, 200, 302, 433]

max_score = 0
for score in student_scores:
    # print(score) #print all numbers
    if score > max_score:
        max_score = score
        
print(max_score)