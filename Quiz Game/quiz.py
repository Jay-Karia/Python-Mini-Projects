print("Welcome to Python Quiz Game Developed -- By Jay")

# Topics
topics = ["About World", "Current Affairs", "History", "Computer Science", "About Novels"]

# Questions
aboutWorldQ = ["Which one is the smallest ocean in the World?",
               "Which country gifted the 'Statue of Liberty' to USA in 1886?",
               "Dead Sea is located between which two countries?",
               "Total number of oceans in the World is", "Which country is known as playground of europe"]

# Answers
aboutWorldA = ["central arctic ocean", "france", "israel and jordan", "5", "switzerland"]

point = 0


# Methods
def answer(answers):
    global point
    # if answers.lower() == aboutWorldA[0] or answers.lower() == aboutWorldA[1] or answers.lower() == aboutWorldA[2]
    # or answers.lower() == aboutWorldA[3] or answers.lower() == aboutWorldA[4]: print("Correct")
    if answers.lower() == aboutWorldA[0]:
        print("Correct!")
        point += 1
    elif answers.lower() == aboutWorldA[1]:
        print("Correct!")
        point = point + 1
    elif answers.lower() == aboutWorldA[2] or answers.lower() == "israel, jordan" or answers.lower() == "israel jordan":
        print("Correct!")
        point = point + 1
    elif answers.lower() == aboutWorldA[3]:
        print("Correct!")
        point = point + 1
    elif answers.lower() == aboutWorldA[4]:
        print("Correct!")
        point = point + 1
    else:
        print("Wrong!")
        point -= 1
    # return point


play = input("\nDo you want to play? ")

if play.lower() == "yes":
    select = input(
        f"\nSelect a Topic: \n\n1) {topics[0]} \n2) {topics[1]} \n3) {topics[2]} \n4) {topics[3]} Computer Science" "\n5) About Novels\n")

    if select == "1":
        print("Questions ", topics[0])

        print(f"\nQ-1: {aboutWorldQ[0]}")
        print("1) Atlantic Ocean\n2) Central Arctic Ocean\n3) Pacific Ocean\n4) Indian Ocean\n5) Southern Oceans\n")
        ans1 = input()
        answer(ans1)

        print("\nQ-2: ", aboutWorldQ[1])
        print("1) France\n2) Britain\n3) America\n4) India\n5) Norway\n")
        ans2 = input()
        answer(ans2)

        print("\nQ-3: ", aboutWorldQ[2])
        print("1) US and Canada\n2) China and Mongolia\n3) Spain and France\n4) Israel and Jordan\n5) Iran and Iraq\n")
        ans3 = input()
        answer(ans3)

        print("\nQ-4: ", aboutWorldQ[3])
        print("1) 5\n2) 2\n3) 7\n4) 3\n5) 12\n")
        ans4 = input()
        answer(ans4)

        print("\nQ-5: ", aboutWorldQ[4])
        print("1) Germany\n2) Italy\n3) France\n4) Switzerland\n5) Greece\n")
        ans5 = input()
        answer(ans5)

        print(
            f"\nAnswers: \nA-1: {aboutWorldA[0]}, A-2: {aboutWorldA[1]}, A-3: {aboutWorldA[2]}, A-4: {aboutWorldA[3]}, A-5: {aboutWorldA[4]}")
        print(point)
    elif select == "2":
        pass
else:
    quit()
