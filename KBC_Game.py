questionsList = [
    "What is capital of pakistan?",
    "What is capital of Punjab",
    "What is capital of Sindh?",
    "What is capital of KPK?",
    "What is capital of Bloachistan?",
]

answerList = ["islamabad", "lahore", "karachi", "peshawar", "quetta"]

optionList = [
    ["peshawar", "karachi", "lahore", "rawalpindi", "islamabad"],
    ["gujranwala", "multan", "sialkot", "lahore", "faisalabad"],
    ["karachi", "sukkur", "hyderabad", "mirpur khas", "larkana"],
    ["abbottabad", "dg khan", "peshawar", "kohat", "mardan"],
    ["sibi", "quetta", "gwadar", "khuzdar", "zob"],
]

prize = list((n + 1) * 1000 for n in range(len(questionsList)))

wonAmount = 0

for questionNo in range(len(questionsList)):
    print("Won amount so far: ", wonAmount)
    print(
        "\nFor the prize money of",
        prize[questionNo],
        "\nQuestion no.",
        questionNo + 1,
        ":",
        questionsList[questionNo],
    )
    gameEnd = False
    print("Your options are: ")
    for options in range(len(optionList[questionNo])):
        print(options + 1, optionList[questionNo][options], end=" ")
    while True:
        try:
            userChoice = int(
                input("\nPlease choose an answer(Enter one of the option no): ")
            )
            if userChoice not in range(1, (len(optionList[questionNo]) + 1)):
                print("Invalid choice!")
            elif answerList[questionNo] == optionList[questionNo][userChoice - 1]:
                print("good!")
                wonAmount = prize[questionNo]
                # wonAmount = wonAmount + prize[questionNo]
                break
            else:
                print("In correct! Game Over.")
                gameEnd = True
                break
        except ValueError:
            print("Invalid input! Please enter a number.")
    if gameEnd:
        break
print("Total amount you won is:", wonAmount)
