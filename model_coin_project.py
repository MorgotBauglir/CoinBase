import json
import os


os.chdir('D:\\Python\\Coin_project')
file = open('cat_to_name.json')
data = json.load(file)


def read_all_country(data):
    for i in data:
        print(i, '-', data[i])


def read():
    number_of_country = input('Enter country: ')
    for i in data:
        print(i, '-', data[i].split(',')[2])
        """number = data[i].split(',')[2]
        if number == number_of_country:
            print(i, '-', data[number])
        else:
            break"""


def menu():
    while True:
        choice = input('Enter your choice:\nAll coins - 1\nYour choice - 2\nExit - 3\n')
        if choice == '1':
            read_all_country(data)
            print('-' * 40)
        if choice == '2':
            read()
        if choice == '3':
            break


menu()
