# Introduction (Intro Flow)

viewer_name = input("Hello Viewer. Please let me know your name:")

import pickle
f = open('User_name.py', 'wb')
pickle.dump(viewer_name, f, protocol=None, fix_imports=True, buffer_callback=None)
f.close() # to save viewer_name for future linking

introduction = f"----- // ----- \n" \
               f"Nice to meet you, {viewer_name}!\n" \
               f"Let me introduce how the process of sharing knowledge formed and I'll also give you a clear view of  \n" \
               f"Options you can use any time you need during our Presentation of Knowledge.\n" \
               f"--- / --- \n" \
               f"The Interaction process is simple - it will look like you are using console. It's devided into Steps \n" \
               f"while you go through Main Presentation Flow. If you don't want or have no time to check full functionality \n" \
               f"I've coded, just use command '/topics_list' to skip present Topic.\n" \
               f"Each Step I give you some intro information in a Topic and you do something with it investigating my \n" \
               f"Python practical experience.\n" \
               f"--- / --- \n" \
               f"At any time you can use predefined commands typing in command line '/commands_list'. For example, if \n" \
               f"you want to check my knowledge in OOP, just find relevant command from from '/topics_list' \n" \
               f"(!type in command line without quotes!)), pick relevant Topic\n" \
               f"in our case: <OOP> , and type it in command line.\n" \
               f"In case of willing to pass your current step, just type command '/pass' \n" \
               f"----- // ----- \n"
print(introduction)

from Command_Line import command_line
# it start using command_line function