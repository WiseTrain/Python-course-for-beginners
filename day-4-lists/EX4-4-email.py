students = ["Punit", "Graham", "Alex", "Karen", "Van",
            "Falwinder", "Gurpreet", "Jasper", "Lyle", 
            "Nega", "Amandeep", "Pawandeep", "Daman", 
            "Pruthviraj", "Beau", "Thilini", "Jashandeep", 
            "Ritesh", "Sahilpreet", "Onkar", "Sourav",
            "Harkamalpreet", "Talwinder"];

def email(name):
    RED = "\033[31m"
    RESET = "\033[0m"
    text = f'''Dear {RED}{name}{RESET},

We are happy to invite you to our Student Work Exhibition, 
happening on {RED}Thursday, 21 September 2023{RESET}, 
at the Whitecliffe campus (67 Symonds Street, Auckland) 
from {RED}10:00 AM to 1:00 PM{RESET}. 
Join us in celebrating the remarkable achievements of our students 
and the outstanding work they've accomplished this term. 
We look forward to seeing you at the exhibition!

Best regards,
Ying, Marina, Rashid, John, Pinal

'''

    return text

for student in students:
    print(email(student))