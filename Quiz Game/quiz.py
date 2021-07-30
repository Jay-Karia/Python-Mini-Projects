print("Welcome to Python Quiz Game Developed -- By Jay")

# Topics
topics = ["About World", "Current Affairs", "Computer Science", "History", "About Novels"]

# Questions
aboutWorldQ = ["Which one is the smallest ocean in the World?",
               "Which country gifted the 'Statue of Liberty' to USA in 1886?",
               "Dead Sea is located between which two countries?",
               "Total number of oceans in the World is", "Which country is known as playground of europe"]

currentAffairsQ = ["Which Union Ministry has notified the standards for Safety Evaluation of Hydrogen Fuels?", "Which E-commerce platform launched a Start-up promotion and mentoring programme named ‘Leap’?", "Which Indian airport has partnered with Virgin Hyperloop for Hyperloop corridor?", "When was the Indian Meteorological Department established?", "India has provided around 3000 vials of Remdisvir to which country?"]

# Answers
aboutWorldA = ["central arctic ocean", "france", "israel and jordan", "5", "switzerland"]
currentAffairsA = ["ministry of road transport and highways", "flipkart", "bangalore international airport", "1875", "myanmar"]

point = 0


# Methods
def answer(answers):
    global point
    # if answers.lower() == aboutWorldA[0] or answers.lower() == aboutWorldA[1] or answers.lower() == aboutWorldA[2]
    # or answers.lower() == aboutWorldA[3] or answers.lower() == aboutWorldA[4]: print("Correct")
    if answers.lower() == aboutWorldA[0] or answers.lower() == currentAffairsA[0] or answers == "1":
        print("Correct!")
        point += 1
    elif answers.lower() == aboutWorldA[1] or answers.lower() == currentAffairsA[1] or answers == "2":
        print("Correct!")
        point = point + 1
    elif answers.lower() == aboutWorldA[2] or answers.lower() == "israel, jordan" or answers.lower() == "israel jordan" or answers.lower() == currentAffairsA[2] or answers == "3":
        print("Correct!")
        point = point + 1
    elif answers.lower() == aboutWorldA[3] or answers.lower() == currentAffairsA[3] or answers == "4":
        print("Correct!")
        point = point + 1
    elif answers.lower() == aboutWorldA[4] or answers.lower() == currentAffairsA[4] or answers == "5":
        print("Correct!")
        point = point + 1
    else:
        print("Wrong!")
        point -= 1


play = input("\nDo you want to play? ")

if play.lower() == "yes":
    select = input(
        f"\nSelect a Topic: \n\n1) {topics[0]} \n2) {topics[1]} \n3) {topics[2]} \n4) {topics[3]} Computer Science" "\n5) About Novels\n")

    if select == "1":
        print("Questions ", topics[0])

        print(f"\nQ-1: {aboutWorldQ[0]}")
        print(f"1) Atlantic Ocean\n2) Central Arctic Ocean\n3) Pacific Ocean\n4) Indian Ocean\n5) Southern Oceans")
        ans1 = input()
        answer(ans1)

        print("\nQ-2: ", aboutWorldQ[1])
        print("1) France\n2) Britain\n3) America\n4) India\n5) Norway")
        ans2 = input()
        answer(ans2)

        print("\nQ-3: ", aboutWorldQ[2])
        print("1) US and Canada\n2) China and Mongolia\n3) Spain and France\n4) Israel and Jordan\n5) Iran and Iraq")
        ans3 = input()
        answer(ans3)

        print("\nQ-4: ", aboutWorldQ[3])
        print("1) 5\n2) 2\n3) 7\n4) 3\n5) 12")
        ans4 = input()
        answer(ans4)

        print("\nQ-5: ", aboutWorldQ[4])
        print("1) Germany\n2) Italy\n3) France\n4) Switzerland\n5) Greece")
        ans5 = input()
        answer(ans5)

        print(
            f"\nAnswers: \nA-1: {aboutWorldA[0]}, A-2: {aboutWorldA[1]}, A-3: {aboutWorldA[2]}, A-4: {aboutWorldA[3]}, A-5: {aboutWorldA[4]}")
    elif select == "2":
        print("Questions ", topics[1])

        print(f"\nQ-1: {currentAffairsQ[0]}")
        print("1) Ministry of Road Transport and Highways\n2) Ministry of Power\n3) Ministry of MSME\n4) state ministry\n5) ] Ministry of Renewable Energy")
        ans1 = input()
        answer(ans1)

        print("\nQ-2: ", currentAffairsQ[1])
        print("1) Amazon\n2) E-Bay\n3) Flipkart\n4) Snapdeal\n5) Shopclues")
        ans2 = input()
        answer(ans2)

        print("\nQ-3: ", currentAffairsQ[2])
        print("1) Delhi International Airport\n2) Bangalore International Airport\n3) Cochin International Airport\n4) Mumbai International Airport\n5) Ahmedabad International Airport")
        ans3 = input()
        answer(ans3)

        print("\nQ-4: ", currentAffairsQ[3])
        print("1) 1975\n2) 1990\n3) 1875\n4) 1950\n5) 1947")
        ans4 = input()
        answer(ans4)

        print("\nQ-5: ", currentAffairsQ[4])
        print("1) Bangladesh\n2) Sri Lanka\n3) Thailand\n4) Nepal\n5) Myanmar")
        ans5 = input()
        answer(ans5)

        print(
            f"\nAnswers: \nA-1: {currentAffairsA[0]}, A-2: {currentAffairsA[1]}, A-3: {currentAffairsA[2]}, A-4: {currentAffairsA[3]}, A-5: {currentAffairsA[4]}")
    print(f"\nYou scored {str(point)}!")
    print(f"Your Percentage: {(point * 100) / 5}")
else:
    quit()
