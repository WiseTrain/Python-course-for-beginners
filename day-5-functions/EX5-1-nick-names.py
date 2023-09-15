from random import choice
# list of adjectives
list1 = ["Geeky", "Nerdy", "Tech-savvy", "Cyber", "Innovative", "Digital", "Caffeinated", "Screaming", "Techoholic", "Gigabit", "Futuristic", 
         "Cloudy", "Wireless", "Pixelated", "Robotronic", "Artificial", "Viral", "Quantum", "Epic", "Databionic"]

# list of nouns
list2 = ["Banana", "Penguin", "Noodle", "Cupcake", "Bumblebee", "Pickle", "Flamingo", "Pancake", "Snickerdoodle", "Cucumber", 
         "Wombat", "Marshmallow", "Llama", "Gummy Bear", "Muffin", "Koala", 
         "Panda", "Popcorn", "Jigsaw", "Raindrop"]
# additions
list3 = ["Master of Memes", "Pixel Picasso", "Code Wizard", "Digital Dynamo", 
         "Tech Ninja", "Byte Buccaneer", "Debugging Diva", "Chief Emoji Officer", "Virtual Virtuoso", "Data Jedi", "Wi-Fi Whisperer", "Chief Troubleshooting Titan", "Byte-sized Comedian", "Pixel Puncher", "Algorithm Alchemist", 
         "Digital Doodle Dandy", "Error Eradicator", "Byte Blaster", "Techie Tinkerer", "Chief of Laughter Loops"]

# randome nick name generator
def nickNameGenerator():
    result = ""
    result += choice(list1) + " "
    result += choice(list2) + ", "
    result += choice(list3)
    return result

print("\nBest nickname for you is\033[95m",nickNameGenerator(), "\033[0m\n")