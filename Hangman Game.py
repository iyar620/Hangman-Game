import random

# רשימת נושאים עם מילים סודיות
list_of_topics = {
    "Animals": ["dog", "cat", "elephant", "giraffe", "tiger", "lion", "zebra", "kangaroo", "panda", "koala", "dolphin", "whale", "shark", "eagle", "owl", "crocodile", "deer", "fox", "wolf", "bear", "hedgehog", "parrot", "duck", "rooster", "donkey", "sheep", "goat", "cow", "horse", "rabbit"],
    "Fruits_and_Vegetables": ["apple", "banana", "tomato", "cucumber", "orange", "grape", "watermelon", "strawberry", "blueberries", "kiwi", "carrot", "broccoli", "lettuce", "pepper", "spinach", "cherry", "peach", "pear", "plum", "pomegranate", "mango", "pineapple", "melon", "papaya", "fig", "zucchini", "eggplant", "onion", "garlic"],
    "Countries_and_Cities": ["Israel", "Tel Aviv", "New York", "Paris", "Tokyo", "London", "Berlin", "Sydney", "Rome", "Madrid", "Beijing", "Moscow", "Cairo", "Dubai", "Toronto", "Los Angeles", "San Francisco", "Chicago", "Miami", "Boston", "Washington", "Mexico City", "Buenos Aires", "Rio de Janeiro", "Sao Paulo", "Cape Town", "Johannesburg", "Mumbai", "New Delhi", "Bangalore"],
    "Professions": ["Doctor", "Teacher", "Engineer", "Lawyer", "Chef", "Nurse", "Architect", "Pilot", "Scientist", "Artist", "Musician", "actor", "writer", "photographer", "journalist", "firefighter", "policeman", "driver", "farmer", "builder", "electrician", "plumber", "programmer", "designer", "manager", "secretary", "pharmacist", "veterinarian", "psychologist", "coach"],
    "Hobbies": ["Drawing", "Reading", "Running", "Swimming", "Cooking", "Gardening", "Fishing", "Hiking", "Biking", "Knitting", "Dance", "Singing", "Music", "Painting", "Photography", "Collecting", "Writing", "Video Games", "Puzzles", "Chess", "Yoga", "Meditation", "Camping", "Surfing", "Skiing", "Snowboarding", "Karate", "Judo", "Boxing", "Football"],
    "Vehicles": ["car", "bicycle", "plane", "train", "boat", "motorcycle", "bus", "truck", "scooter", "submarine", "helicopter", "spaceship", "tram", "van", "yacht", "tractor", "caravan", "off-road vehicle", "commercial vehicle", "police car", "fire engine", "ambulance", "tank"],
    "Foods": ["pizza", "hamburger", "sushi", "falafel", "chocolate", "pasta", "salad", "sandwich", "soup", "steak", "taco", "burrito", "pancakes", "waffles", "ice cream", "shawarma", "hummus", "couscous", "bread", "cake", "cookies", "pie", "croissant", "bagel", "pita", "bun", "biscuit", "dessert", "candy"],
    "Sports": ["Football", "Basketball", "Tennis", "Cricket", "Baseball", "Hockey", "Golf", "Swimming", "Running", "Cycling", "boxing", "wrestling", "gymnastics", "skiing", "surfing", "volleyball", "handball", "water polo", "rugby", "football", "badminton", "table tennis", "squash", "karate", "judo", "taekwondo", "jumping", "diving", "kayaking", "sailing"],
    "Music_Instruments": ["guitar", "piano", "violin", "drums", "flute", "saxophone", "trumpet", "cello", "harp", "clarinet", "trombone", "accordion", "banjo", "ukulele", "mandolin", "contrabass", "bouzouki", "oud", "canon", "darboka", "tamborine", "marimba", "xylophone", "bells", "gong", "synthesizer", "organ", "harmonica", "melodica", "kazoo"],
    "Movies_and_TV_Shows": ["Inception", "Titanic", "Friends", "Line Breaker", "The Godfather", "The Dark Knight", "Game-of-Thrones", "The-Simpsons", "Stranger-Things", "Harry-Potter", "Star-Wars", "Lord-of-the-Rings", "The Avengers", "Sherlock", "The Office", "Black-Panther", "Avengers: Endgame", "The Diary", "Life-is-beautiful", "The-Never-Ending-Story", "The-Magic-Princess", "The-Secret-Life-of-Pets", "The-Voice-In-Your-Head", "The-Wizard-of-Oz", "The-Wonderful-Journey", "Journey-to-the-mystery-planet", "Journey-to-the-forbidden-planet", "Journey-to-the-lost-planet"],
    "Colors": ["red", "blue", "green", "yellow", "purple", "orange", "pink", "brown", "black", "white", "gray", " turquoise", "burgundy", "gold", "silver", "bronze"],
    "Random": [
        "dog", "cat", "elephant", "giraffe", "tiger", "lion", "zebra", "kangaroo", "panda", "koala", "dolphin", "whale", "shark", "eagle", "owl", "crocodile", "deer", "fox", "wolf", "bear", "hedgehog", "parrot", "duck", "rooster", "donkey", "sheep", "goat", "cow", "horse", "rabbit",
        "apple", "banana", "tomato", "cucumber", "orange", "grape", "watermelon", "strawberry", "blueberries", "kiwi", "carrot", "broccoli", "lettuce", "pepper", "spinach", "cherry", "peach", "pear", "plum", "pomegranate", "mango", "pineapple", "melon", "papaya", "fig", "zucchini", "eggplant", "onion", "garlic",
        "Israel", "Tel Aviv", "New York", "Paris", "Tokyo", "London", "Berlin", "Sydney", "Rome", "Madrid", "Beijing", "Moscow", "Cairo", "Dubai", "Toronto", "Los Angeles", "San Francisco", "Chicago", "Miami", "Boston", "Washington", "Mexico City", "Buenos Aires", "Rio de Janeiro", "Sao Paulo", "Cape Town", "Johannesburg", "Mumbai", "New Delhi", "Bangalore",
        "Doctor", "Teacher", "Engineer", "Lawyer", "Chef", "Nurse", "Architect", "Pilot", "Scientist", "Artist", "Musician", "actor", "writer", "photographer", "journalist", "firefighter", "policeman", "driver", "farmer", "builder", "electrician", "plumber", "programmer", "designer", "manager", "secretary", "pharmacist", "veterinarian", "psychologist", "coach",
        "Drawing", "Reading", "Running", "Swimming", "Cooking", "Gardening", "Fishing", "Hiking", "Biking", "Knitting", "Dance", "Singing", "Music", "Painting", "Photography", "Collecting", "Writing", "Video Games", "Puzzles", "Chess", "Yoga", "Meditation", "Camping", "Surfing", "Skiing", "Snowboarding", "Karate", "Judo", "Boxing", "Football",
        "car", "bicycle", "plane", "train", "boat", "motorcycle", "bus", "truck", "scooter", "submarine", "helicopter", "spaceship", "tram", "van", "yacht", "tractor", "caravan", "off-road vehicle", "commercial vehicle", "police car", "fire engine", "ambulance", "tank",
        "pizza", "hamburger", "sushi", "falafel", "chocolate", "pasta", "salad", "sandwich", "soup", "steak", "taco", "burrito", "pancakes", "waffles", "ice cream", "shawarma", "hummus", "couscous", "bread", "cake", "cookies", "pie", "croissant", "bagel", "pita", "bun", "biscuit", "dessert", "candy",
        "Football", "Basketball", "Tennis", "Cricket", "Baseball", "Hockey", "Golf", "Swimming", "Running", "Cycling", "boxing", "wrestling", "gymnastics", "skiing", "surfing", "volleyball", "handball", "water polo", "rugby", "football", "badminton", "table tennis", "squash", "karate", "judo", "taekwondo", "jumping", "diving", "kayaking", "sailing",
        "guitar", "piano", "violin", "drums", "flute", "saxophone", "trumpet", "cello", "harp", "clarinet", "trombone", "accordion", "banjo", "ukulele", "mandolin", "contrabass", "bouzouki", "oud", "canon", "darboka", "tamborine", "marimba", "xylophone", "bells", "gong", "synthesizer", "organ", "harmonica", "melodica", "kazoo",
        "Inception", "Titanic", "Friends", "Line Breaker", "The Godfather", "The Dark Knight", "Game-of-Thrones", "The-Simpsons", "Stranger-Things", "Harry-Potter", "Star-Wars", "Lord-of-the-Rings", "The Avengers", "Sherlock", "The Office", "Black-Panther", "Avengers: Endgame", "The Diary", "Life-is-beautiful", "The-Never-Ending-Story", "The-Magic-Princess", "The-Secret-Life-of-Pets", "The-Voice-In-Your-Head", "The-Wizard-of-Oz", "The-Wonderful-Journey", "Journey-to-the-mystery-planet", "Journey-to-the-forbidden-planet", "Journey-to-the-lost-planet",
        "red", "blue", "green", "yellow", "purple", "orange", "pink", "brown", "black", "white", "gray", "turquoise", "burgundy", "gold", "silver", "bronze"
        ]  
}

# משתנה קבוע שמחזיק את שבעת המצבים של האיש התלוי
HANGMAN_PHOTOS = {
    1: "x-------x",
    2: "x-------x\n|\n|\n|\n|\n|",
    3: "x-------x\n|       |\n|       0\n|\n|\n|",
    4: "x-------x\n|       |\n|       0\n|       |\n|\n|",
    5: "x-------x\n|       |\n|       0\n|      /|\\\n|\n|",
    6: "x-------x\n|       |\n|       0\n|      /|\\\n|      /\n|",
    7: "x-------x\n|       |\n|       0\n|      /|\\\n|      / \\\n|"
}

# משתנה קבוע שמחזיק את האמנות ASCII של המשחק
HANGMAN_ASCII_ART = ("""Welcome to the game Hangman
  _    _                                         
 | |  | |   
 | |__| | __ _ _ __   __ _ _ __ ___   __ _ _ __  
 |  __  |/ _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
 | |  | | (_| | | | | (_| | | | | | | (_| | | | |
 |_|  |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                      __/ |
                     |___/ """)

LINEBREAK = "\n"
MAX_TRIES = "6"
OPENING_DISPLAY = HANGMAN_ASCII_ART + LINEBREAK + "You have "  + MAX_TRIES + " trials " + "\n"

def check_valid_input(letter_guessed, old_letters_guessed):
    """
    Checks if the character received from the user is correct and has not been guessed before.

    param letter_guessed: a string representing the character received from the user
    param old_letters_guessed: list of previously guessed letters
    return: a Boolean value representing the correctness of the character and whether it was guessed before
    """
    if len(letter_guessed) != 1:
        return False
    elif not letter_guessed.isalpha() or not letter_guessed.islower():
        return False
    elif letter_guessed in old_letters_guessed:
        return False
    else:
        return True

def try_update_letter_guessed(letter_guessed, old_letters_guessed):
    """
    Trying to update the list of guessed letters with the new character received from the user.

    param letter_guessed: A string representing the character guessed from the user
    param old_letters_guessed: A list of previously guessed letters
    return: A Boolean value representing whether the character was successfully added to the list
    """
    if check_valid_input(letter_guessed, old_letters_guessed):
        old_letters_guessed.append(letter_guessed)
        return True
    else:
        print("X")
        print(" -> ".join(sorted(old_letters_guessed)))
        return False

def display_hidden_word(secret_word, old_letters_guessed):
    """
    Shows the hidden word with underlined letters for missed letters and correctly guessed letters.

    param secret_word: A string representing the secret word
    param old_letters_guessed: A list of previously guessed letters
    return: A string representing the hidden word
    """
    displayed_word = ""
    for letter in secret_word:
        if letter in old_letters_guessed:
            displayed_word += letter + " "
        else:
            displayed_word += "_ "
    return displayed_word.strip()

def print_hangman(num_of_tries):
   """
 Prints one of the seven states of the hanging man depending on the number of failed attempts.

 param num_of_tries: The number of failed attempts by the user so far
 """
   print(HANGMAN_PHOTOS[num_of_tries])

def choose_secret_word():
    """
 Allows the user to select a topic and chooses a random word from the list of that topic.

 return: a string representing the secret word
 """
    print("Please choose a topic: \n")
    for topic in list_of_topics:
        print(topic)
    
    chosen_topic = input("Enter the topic name: \n")
    
    if chosen_topic in list_of_topics:
        secret_word = random.choice(list_of_topics[chosen_topic])
        print(f"The secret word has been chosen from the topic '{chosen_topic}'. \n")
        return secret_word
    else:
        print("Invalid topic. Please try again. \n")
        return choose_secret_word()

def main():
    """
    Main function to run the Hangman game.
    """
    print(OPENING_DISPLAY)
    secret_word = choose_secret_word()
    old_letters_guessed = []
    num_of_tries = 1
    print("_ " * len(secret_word))

    while num_of_tries < int(MAX_TRIES) and "_" in display_hidden_word(secret_word, old_letters_guessed):
        letter_guessed = input("Guess a letter: ").lower()
        if try_update_letter_guessed(letter_guessed, old_letters_guessed):
            if letter_guessed not in secret_word:
                num_of_tries += 1
            print(display_hidden_word(secret_word, old_letters_guessed))
            print_hangman(num_of_tries)
        else:
            print("Invalid input. Try again.")

    if "_" not in display_hidden_word(secret_word, old_letters_guessed):
        print("Congratulations, you won!")
        
    else:
        print("Sorry, you lost. The word was:", secret_word)
        

# קריאה לפונקציה הראשית
if __name__ == "__main__":
    main()










 


