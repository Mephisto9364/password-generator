import secrets
from pathlib import Path
import pyperclip

def ChoiceYN(output):
    while True:
        YN = input(str(output)).strip().lower()
        if YN != 'n':
            return True
        return False
        # if YN == 'y':
        #     YN = 1
        #     return bool(YN)
        # elif YN == 'n':
        #     YN = 0
        #     return bool(YN)


def GeneratePassword():
    while True:
        try:
            length = int(input('Какой длинны пароль создать? (5 - 100): '))
            if length > 4 and length <= 100:

                password = []
                required = []

                Letters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
                upper = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
                lower = 'abcdefghijklmnopqrstuvwxyz'
                nums = '0123456789'
                punctuation = '!\"#$%&\'()*+,-./:;<=>?@[]^_`{|}~'
                alphabet = Letters

                UseNums = ChoiceYN('Использовать Цифры? 0123456789 \n(y/n): ')
                UseSpecialS = ChoiceYN('Использовать Спец Символы? \n!\"#$%&\'()*+,-./:;<=>?@[]^_`{|}~ \n(y/n): ')

                if UseNums:
                    alphabet += nums
                    required.append(secrets.choice(nums))
                if UseSpecialS:
                    alphabet += punctuation
                    required.append(secrets.choice(punctuation))
                required.append(secrets.choice(upper))
                required.append(secrets.choice(lower))  
                

                if len(required) > length:
                    print('Длина пароля слишком мала для всех условий')
                    continue
                

                password = list(required)
                for _ in range(length - len(required)):
                    password += secrets.choice(alphabet)
                secrets.SystemRandom().shuffle(password)
                
                CompletePassword = ''.join(password)
                SavePass = ChoiceYN(f'Сохранить Пароль в файл? {CompletePassword}')
                if SavePass:
                    file_path = Path(r"C:\Users\User\Desktop\Python\PasswordGen\Passwords.txt")
                    NamePassword = input('Для чего пароль: ')
                    with open(file_path, 'a', encoding='utf-8') as file:
                        file.write(f"{NamePassword}:  {CompletePassword} \n")
                        
                pyperclip.copy(CompletePassword)
                return CompletePassword
            
            else:
                print('Ошибка длинны пароля.')
        except ValueError:
            print('Ошибка значения длинны пароля.')
            return 'Ошибка значения длинны пароля.'
    



print(GeneratePassword())