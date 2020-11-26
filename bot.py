from twitchbot import BaseBot, load_commands_from_directory

if __name__ == '__main__':
    load_commands_from_directory('./commands')
    BaseBot().run()