import random
import string
import os
text = """
/* {}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{} */     /* {}  ooooo                      oooo                 {} */     /* {}   888   ooooooo    ooooooo   888  ooooo          {} */
/* {}   888   ooooo888 888     888 888o888             {} */
/* {}   888 888    888 888         8888 88o            {} */
/* {}   888  88ooo88 8o  88ooo888 o888o o888o          {} */
/* {}8o888                                             {} */
/* {}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{} */

     ▂▃▄▅▆▇▓▒░ Coded By SKJack ░▒▓▇▆▅▄▃▂
"""

print(text)

print("      Name :- All Password Genarator")
print("      Allah is watching you ")
def generate_password(length=12, use_uppercase=True, use_digits=True, use_special_chars=True):
    char_pool = string.ascii_lowercase
    if use_uppercase:
        char_pool += string.ascii_uppercase
    if use_digits:
        char_pool += string.digits
    if use_special_chars:
        char_pool += string.punctuation
    if length < 1:
        raise ValueError("Password length must be at least 1.")
        os.system("clear")
    password = ''.join(random.choice(char_pool) for _ in range(length))
    return password
if __name__ == "__main__":
    password_length = int(input("Password Length: "))
    num_passwords = int(input("Number of passwords to generate: "))
    include_uppercase = input("Include Letters? (y/n): ").lower() == 'y'
    include_digits = input("Include Digits? (y/n): ").lower() == 'y'
    include_special_chars = input("Include Special Characters? (y/n): ").lower() == 'y'
    file_name = input("Enter the file name to save passwords ")
    with open(file_name, 'w') as file:
        for _ in range(num_passwords):
            generated_password = generate_password(
                length=password_length,
                use_uppercase=include_uppercase,
                use_digits=include_digits,
                 use_special_chars=include_special_chars
            )
            print("Generated password:", generated_password)
            file.write(f"{generated_password}\n")

    print(f"Generated passwords have been saved to {file_name}")