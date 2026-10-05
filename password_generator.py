import secrets
import pyperclip
from pathlib import Path

def ask_yn(text: str) -> bool:
    while True:
        answer = input(text).strip().lower()
        if answer == 'y':
            return True
        elif answer == 'n':
            return False
        print("Please enter 'y' or 'n'.")


def save_to_txt(label: str, password: str):
    file_path = Path(__file__).parent / "Passwords.txt"
    with open(file_path, 'a', encoding='utf-8') as file:
        file.write(f"{label}:  {password} \n")


def generate_password(length: int, use_digits: bool, use_special_symbols: bool):
    required = []

    letters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    upper = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    lower = 'abcdefghijklmnopqrstuvwxyz'
    digits = '0123456789'
    punctuation = '!\"#$%&\'()*+,-./:;<=>?@[]^_`{|}~'
    alphabet = letters

    if use_digits:
        alphabet += digits
        required.append(secrets.choice(digits))
    if use_special_symbols:
        alphabet += punctuation
        required.append(secrets.choice(punctuation))
    required.append(secrets.choice(upper))
    required.append(secrets.choice(lower))  
    
    if len(required) > length:
        print('ERROR\nToo small length for all selected requirements')
        return

    for _ in range(length - len(required)):
        required.append(secrets.choice(alphabet))
    secrets.SystemRandom().shuffle(required)
    
    complete_password = ''.join(required)
    return complete_password
        

def main():
    try:
        password_length = int(input('Length password (5-100): '))
    except ValueError:
        print('ERROR\nLength must be Integer')
        return
    if password_length > 100 or password_length < 5:
        print('ERROR\nLength must be 5 - 100')
        return
    
    use_digits = ask_yn('Use digits? 0123456789\n(y/n): ')
    use_special_symbols = ask_yn('Use special characters? \'!\"#$%&\'()*+,-./:;<=>?@[]^_`{|}~\n(y/n): ')

    password = generate_password(password_length, use_digits, use_special_symbols)
    if password == None:
        return
    print(f'\nYour password:\n{password}\n')

    try:
        pyperclip.copy(password)
        print('Password copied to clipboard')
    except pyperclip.PyperclipException:
        print('Could not copy to clipboard. Make sure pyperclip works.')

    if ask_yn('\nSave your password to .txt file?: '):

        label_password = input('Label password? ')
        save_to_txt(label_password, password)


if __name__ == "__main__":
    main()