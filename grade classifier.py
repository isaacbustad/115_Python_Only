# grade score range
A = 95


#if score > garde
	#print (lettr)


def calc_grade(a_score):
	if a_score >= A:
		print ("A")

	elif a_score >= 80:
		print ("B")

	elif a_score >= 70:
		print ("C")

	else:
		print("F")


# execute main
# test score
score = int(input())
calc_grade(score)