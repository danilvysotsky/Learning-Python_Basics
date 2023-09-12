def calculator(): # написать калькулятор
    return command_line_calculator()

def command_line_calculator():
    x = input('<Topic Calculator>. Type your command:')
    if x == '/run_calculator':
        print(calculator()) # написать калькулятор
    elif x == '/pass':
        from Command_Line import command_line
        print(command_line) # Создать функцию command_pass и Изучить импорт из модуля, и перенаправить на функцию command_line()
    else:
        print('\n --- Wrong command. Please try again ---\n')
    return command_line_calculator()

import pickle
f = open('User_name.py', 'rb')
viewer_name_load = pickle.load(f)
f.close() # to load viewer_name from introduction.py

def f_topic_basic_syntax_numbers():
    print(f"Great! {viewer_name_load}, Now you are in the Topic: 'Basic Syntax & Numbers'\n" \
          f"To present that I've learned python Syntax and Number type at a sufficient level, I decided to \n" \
          f"create a Calculator, as to implement such scripts you need to deeply investigate Python Syntax\n" \
          f"and Type 'Numbers'.\n"
          f"To start checking Calculator please run command: /run_calculator\n" \
          f"To skip this Topic, just type '/pass'. Please note, if you pass the Topic, all progress will not be saved.\n")
    return command_line_calculator()

print(f_topic_basic_syntax_numbers())


