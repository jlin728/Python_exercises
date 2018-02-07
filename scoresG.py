def grades():
    print "Scores and Grades"
    import random
    for x in range(1, 11):
    #random_num = random.random() <--- returns a float
        score = random.randint(60,101)
        if (score > 90 and score <= 100):
            print ("Score:"), score, ("; Your grade is A.")
        elif (score > 80) and (score <= 89):
            print ("Score:"), score, ("; Your grade is B.")
        elif (score > 70) and (score <= 79):
            print ("Score:"), score, ("; Your grade is C.")
        elif (score > 60) and (score <= 69):
            print ("Score:"), score, ("; Your grade is D.")
    print ("End of the program. Bye!")

grades()
