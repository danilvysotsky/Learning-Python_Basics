def Strings_flow_1(): # написать инструкции
    print("---//---\n"
          "To code current program I had to use input() function to implement possibility for your to type \n" \
          "commands in Command Line.\n" \
          "F-strings where also useful when I wanted to mention your name in the text\n" \
          "Here is a source code where I used input() and F-strings at the same time in present program.\n")
    input('Please press enter to see the code:')

    from pathlib import Path  # To correctly show direction to picture in any os
    path = Path('Pics', 'Strings_1.GIF')
    print(str(path))
    from PIL import Image  # Pillow module to open images
    pic_Strings_1 = Image.open(path, mode='r', formats=None)
    pic_Strings_1.show()
    print("")

    input('Press enter to go through String slicing, Concatenation and Indexing:')

    print('---//---\n'
          'Slicing and indexing should be used to change or extract string word(s) from the text, concatenation - to unite:')
    #################
    first_word = input('Type first any word:')
    second_word = input('Type second any word:')
    print(f'---//---\n'
          f'To include both words in one string, we should concatenate them in one string:')
    two_words = first_word + ' ' + second_word
    print('')
    print(two_words)
    print("\n So, every letter in the string has it's own index, here they are:")
    two_words_conversion = list(two_words)

    two_words_indexing = len(two_words)
    two_words_indexing_list = list(range(two_words_indexing))
    two_words_indexing_list_int = range(two_words_indexing)

    print(f"Your two Words:        {' '.join(two_words_conversion)}")
    print(f"Indexes of two Words:  {' '.join(map(str, two_words_indexing_list))}")
    print('---//---\n'
          'We can extract or slice words or letters from the text by defining a range from indexes.\n')

    def first_number():
        global index_a
        try:  # implemented and exeption as code worked well while index_a was an integer
            index_a = int(input('\nPlease type First integer index Number, the start of slicing of 2 words:'))
            if index_a not in two_words_indexing_list_int:
                print(
                    f"\nWarning! First Number should be within the range of mentioned indexes: {' '.join(map(str, two_words_indexing_list))}")
                return first_number()
        except:
            print("\nWarning! First Number must be an integer.")
            return first_number()
        return f"First index: {index_a}"

    print(first_number())

    def second_number():
        global index_b
        try:  # implemented and exeption as code worked well while index_a was an integer
            index_b = int(input('\nPlease type Second integer index Number, the start of slicing of 2 words:'))
            if index_b not in two_words_indexing_list_int:
                print(
                    f"\nWarning! Second Number should be within the range of mentioned indexes: {' '.join(map(str, two_words_indexing_list))}")
                return second_number()
        except:
            print("\nWarning! Second Number must be an integer.")
            return second_number()
        return f"Second index: {index_b}\n"

    print(second_number())

    sliced_words = two_words[index_a:index_b]
    print(f"{sliced_words} <=== That's the result of slicing of 2 words\n")
    print(f"Congrats! You've just passed the whole topic <Strings>. Moving to <Main> Command line.")

    return command_line_strings()

def command_line_strings():
    x = input('<Topic Strings>. Type your command:')
    if x == '/continue':
        print(Strings_flow_1())
    elif x == '/pass':
        from Command_Line import command_line
        print(command_line)
    else:
        print('\n --- Wrong command. Please try again. Note! If you want to use commands and change a topic, please goto\n'
              '<Main> menu just typing /pass')
    return command_line_strings()

import pickle
f = open('User_name.py', 'rb')
viewer_name_load = pickle.load(f)
f.close() # to load viewer_name from introduction.py

def f_topic_strings():
    print(f"--- // ---\n"
          f"{viewer_name_load}, now you are in the Topic: 'Strings'\n"\
          f"The following subtopics I would like to share with you:\n"\
          f"input()\n" \
          f"F-string\n" \
          f"String slicing\n"\
          f"Concatenation and Indexing\n"\
          f"\nPlease type /continue to go through String Topic\n"
          f"If you want to change topic or choose other commands in <Main> menu, just type /pass\n"
          f"--- // ---\n")
    return command_line_strings()

print(f_topic_strings())