import csv
import random


class PasswordManager:

    def __init__(self):
        self.csv_path = '../passwords.csv'

        lower_case_letters = list(range(97, 123))
        upper_case_letters = list(range(65, 91))
        digits = list(range(48, 58))
        self.pass_word_chars = lower_case_letters + upper_case_letters + digits

    def main(self):
        while True:
            print("Enter 'q' anytime to exit...")
            if (pass_name := input('Enter the name for the new password you wish to generate: ')) == 'q':
                break

            new_password = self.generate_new_password()
            print(f'New password for "{pass_name}" is {new_password}')

            if (response := input('Would you like to save this new password? (y/n): ')) == 'y':
                self.save_password(pass_name, new_password)
                print(f'{pass_name} saved successfully.')
            elif response == 'q':
                break

    def generate_new_password(self, length=15, special_chars='!$^&*', save_as=None):
        password = ''.join([self.generate_random_char(special_chars) for _ in range(length)])
        if save_as:
            self.save_password(save_as, password)
        return password

    def generate_random_char(self, special_chars=''):
        return chr(random.choice(self.pass_word_chars + [ord(c) for c in special_chars]))

    def save_password(self, name, password):
        with open(self.csv_path, 'a', newline='') as file:
            password_writer = csv.writer(file, delimiter=',')
            password_writer.writerow([name, password])
        return True


if __name__ == '__main__':
    password_manager = PasswordManager()
    password_manager.main()
