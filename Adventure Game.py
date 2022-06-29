import time
import random

reactions = ["Oh no! The little guy hid under your chair and refused to\n"
             "meet you.\n",
             "Awe! She crawled on to your lap and wants to snuggle.\n",
             "Yipes! The creature nipped at you!\n",
             "Crikey! This is the sweetest being you ever encountered!\n",
             "Good gravy! This thing really wants to play!\n",
             "Flibberty gibbets! This is the cutest animal you ever saw!\n"]


def random_reaction(reactions):
    print(random.choice(reactions))


def print_pause(message_to_print):
    print(message_to_print)
    time.sleep(1)


def intro():
    print_pause("You step out of the car outside the shelter,\n"
                "eager to adopt the perfect pet!\n")
    print_pause("Keeping in mind where you live, you know it is important\n"
                "to choose a pet that will be a good fit in your home.\n")
    print_pause("Excitedly, you enter the shelter!\n")
    print_pause("The greeter welcomes you, gives you an adoption \n"
                "application, and asks what type of home you live in.\n")
    choose_home()


def choose_home():
    print_pause("Please enter the number for the type of home you live in.\n")
    home = input("1. City Apartment\n"
                 "2. Farmhouse with lots of land\n"
                 "3. A Hut on the Beach\n")
    if home == '1':
        city_apartment()
    elif home == '2':
        farmhouse()
    elif home == '3':
        beach_hut()
    else:
        print_pause("Please enter 1, 2, or 3.\n")
        choose_home()


def city_apartment():
    print_pause("You share that you live in a city apartment.\n")
    print_pause("The greeter directs you to the small animal wing.\n")
    print_pause("You find two animals that you like in the small animal\n"
                "wing:\n"
                "a cute chihuahua, and a tiny hamster.\n")
    print_pause("You decide to meet one to see if it likes you. Choose\n"
                "the number for the animal you'd like to meet:\n")
    pet = input("1. chihuahua\n"
                "2. hamster\n")

    if pet == '1':
        print_pause("You decide to meet the chihuahua.\n")

    elif pet == '2':
        print_pause("You decide to meet the hamster.\n")

    else:
        print_pause("Please enter 1 or 2.\n")
        city_apartment()

    print(random.choice(reactions))
    adopt_or_not()


def farmhouse():
    print_pause("You share that you live in a farmhouse with lots of land.\n")
    print_pause("The greeter directs you to the barn animal wing.\n")
    print_pause("You find two animals that you like in the barn animal wing:\n"
                "a curious cat, and a fun collie.")
    print_pause("You decide to meet one to see if it likes you. Choose\n"
                "the number for the animal you'd like to meet:\n")
    pet = input("1. cat\n"
                "2. collie\n")

    if pet == '1':
        print_pause("You decide to meet the cat.\n")

    elif pet == '2':
        print_pause("You decide to meet the collie.\n")

    else:
        print_pause("Please enter 1 or 2.\n")
        farmhouse()

    print(random.choice(reactions))
    adopt_or_not()


def beach_hut():
    print_pause("You share that you live in a hut on the beach.\n")
    print_pause("The greeter directs you to the tropical pet wing.\n")
    print_pause("You find two animals that you like in the tropical\n"
                "pet wing:\n"
                "a quiet turtle, and a talkative toucan.")
    print_pause("You decide to meet one to see if it likes you. Choose\n"
                "the number for the animal you'd like to meet:\n")
    pet = input("1. turtle\n"
                "2. toucan\n")

    if pet == '1':
        print_pause("You decide to meet the turtle.\n")

    elif pet == '2':
        print_pause("You decide to meet the toucan.\n")

    else:
        print_pause("Please enter 1 or 2.\n")
        beach_hut()

    print(random.choice(reactions))
    adopt_or_not()


def adopt_or_not():
    print_pause("Will you adopt this little creature?\n")
    adopt = input("1. yes\n"
                  "2. no\n")
    if adopt == '1':
        print_pause("Congratulations! You are a new pet owner!\n")
    elif adopt == '2':
        print_pause("Sorry to hear that didn't work out.\n")
    else:
        print("Please enter 1 or 2.\n")

    play_again()


def play_again():
    print_pause("Would you like to play again? Enter the number\n"
                "for your choice.\n")
    play_again = input("1. yes\n"
                       "2. no\n")
    if play_again == '1':
        print_pause("Super! Let's adopt a new pet.\n")
        return play_game()
    elif play_again == '2':
        print_pause("Thanks for playing! Game over.\n")
        exit(0)
    else:
        print_pause("I don't understand. Please enter 1 or 2.")


def play_game():
    intro()
    choose_home()

play_game()
