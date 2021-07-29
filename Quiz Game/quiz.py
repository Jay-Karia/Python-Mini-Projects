print("Welcome to Python Quiz Game Developed -- By Jay")

# Topics
topics = ["About World", "Current Affairs", "History", "Computer Science", "About Novels"]

# Questions
aboutWorldQ = ["Which one is the smallest ocean in the World?", "What happened during Earth's Dark Age",
              " or the first 500 million years after it formed?", "How did life begin",
              "How does Earth's interior work, and how does it affect the surface?",
              "Why does Earth have plate tectonics and continents?"]

# Answers
aboutWorldA = ["Central Arctic Ocean"]

play = input("\nDo you want to play? ")

if play == "Yes" or "yes":
    points = 0
    select = input(
        "\nSelect a Topic: \n\n1) About World" "\n2) Current Affairs" "\n3) History" "\n4) Computer Science" "\n5) About Novels\n")

    if select == "1":
        print("Questions ", topics[0], "\n")
        for i in range(5):
            print(f"\nQ-0{i}: ", aboutWorldQ[i])

        que1 = input()
        if que1 == "Arctic Ocean" or "Central Arctic Ocean" or "arctic ocean" or "central arctic ocean":
            print("Correct")
            point = + 1
        else:
            print("Answer: ", aboutWorldA[0])
