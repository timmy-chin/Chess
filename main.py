# This is a sample Python script.
#
# # Press ⌃R to execute it or replace it with your code.
# # Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
#
#
# def print_hi(name):
#     # Use a breakpoint in the code line below to debug your script.
#     print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.
#
#
# # Press the green button in the gutter to run the script.
# if __name__ == '__main__':
#     print_hi('PyCharm')
#
# # See PyCharm help at https://www.jetbrains.com/help/pycharm/

# from tabulate import tabulate
#
# d = [ ["Mark", 12, 95],
#      ["Jay", 11, 88],
#      ["Jack", 14, 90]]
#
# print(tabulate(d, headers=["Index", "Age", "Percent"]))

# choice = 'killing'
# if choice.lower == 'k' or choice == 'killing':
#      print('True')


# dict = {'Hello':'Man', 'Goodbye': 'Homie'}
#
# print('Man' in dict.values())

# for i in range(1,1):
#     print(i)

# from Speech_Recognition import *
# import pyaudio
#
# def takecommand():  # function to take an audio input from the user
#     r = sr.Recognizer()
#     with sr.Microphone() as source:
#         print('Listening...')
#         r.pause_threshold = 2
#         r.adjust_for_ambient_noise(
#             source
#         )  # listen for 1 second to calibrate the energy threshold for ambient noise levels
#         audio = r.listen(source)
#         try:                                            # error handling
#             print('Recognizing...')
#             # using google for voice recognition
#             query = r.recognize_google(audio, language='en-in')
#             print(f'User said: {query}\n')
#
#         except Exception as e:
#             # 'say that again' will be printed in case of improper voice
#             print('Say that again please...')
#             return 'None'
#     return query
#
# speak(takecommand())

# checker = ['Black King', 'Black King']
# Black = False
# White = False
# for piece in checker:
#     if 'Black' in piece:
#         Black = True
#     if 'White' in piece:
#         White = True
#
# if Black and White:
#     print('Black Check and White Check')
# elif Black:
#     print('Black Check')
# elif White:
#     print('White Check')

# with open('Checkmate_Test.txt', 'r') as file:
#     test_case = [move.replace('\n', '') for move in file]

dict_1 = {'Heelo': 'Bye', 'Bro':'Ski'}
dict_2 = dict(dict_1)

dict_2['Heelo'] = '"Kitty'

print(dict_1)
print(dict_2)

