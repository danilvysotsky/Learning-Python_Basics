#Commands List
commands_list_str = f'/menu \n' \
                    f'/commands_list \n' \
                    f'/topics_list \n' \
                    f'/passed_topics \n' \
                    f'/save <Name> \n' \
                    f'/load <Name> \n' \
                    f'/list_of_saved_progress \n' \
                    f'/go_to_topic <name of the topic from the /topics_list> \n' \
                    f'/pass  - to pass current step \n' # execution of command  /commands_list
#Topics List:

topics_list_str = f'\n<OOP>\n' \
                  f'<FP>\n' \
                  f'<BS&N> - Basic Syntax & Numbers\n' \
                  f'<Strings>'

def command_line():
    x = input('<Main>. Type your command:')
    if x == '/commands_list':
        print('Following Commands are available:', str(commands_list_str))
    elif x == '/topics_list':
        print('Following Topics are available:', str(topics_list_str))
    elif x == '<Strings>':
        import topic_strings
    else:
        print('Wrong command. Please try again. \n')
    return command_line()

print(command_line())