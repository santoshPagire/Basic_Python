
score = int(input("Enter Score of student : "))
     
if score >= 90:
        print("This student's score of " + str(score) + " is in A grade")
else:
    if score >= 80:
            print("This student's score of " + str(score) + " is in B grade")
    else:
        if score >= 70:
                print("This student's score of " + str(score) + " is in C grade.")
        else:
            if score >= 60:
                    print("This student's score of " + str(score) + " is in D grade.")
            else:
                    print("This student's score of " + str(score) + " is in F grade")