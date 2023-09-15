# Programming language inspiration

lang = input("Enter the programming language: ")
## if-elseif-else
# if lang == "JavaScript":
#     insp = "You can become a Web Developer."
# elif lang == "PHP":
#     insp = "You can become a Backend Developer."
# elif lang == "Python":
#     insp = "You can become a Data Scientist."
# elif lang == "Solidity":
#     insp = "You can become a Blockchain Developer."
# elif lang == "Java":
#     insp = "You can become a Mobile App Developer."
# else:
#     insp = "The language doesn't matter, what matters is solving problems."


# **************************************
# match
match(lang):
    case "JavaScript":
        insp = "You can become a Web Developer."
    case "PHP":
        insp = "You can become a Backend Developer."
    case "Python":
        insp = "You can become a Data Scientist"
    case "Solidity":
        insp = "You can become a Blockchain Developer."
    case "Java":
        insp = "You can become a Mobile App Developer"
    case _: 
        insp = "The language doesn't matter, what matters is solving problems."

print(insp);