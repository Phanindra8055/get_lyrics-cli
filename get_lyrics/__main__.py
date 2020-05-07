import sys
import os
from .get_lyrics import get_lyrics


def intro():
    print('''
Lyrics fetching program with CLI in Python

--------------------------------------------------------------------------------------------------------
Available Commands:

-h, -help:
    To display this and exit

get_lyrics:
    To fetching the actual lyrics

    Usage:

        get_lyrics song_title(with no spaces) artist_name(with no spaces)

        ''')


def help():
    print('''
Available Commands:

--h, --help:
    To display this and exit

get_lyrics:
    To fetching the actual lyrics

    Usage:

        get_lyrics song_title(with no spaces) artist_name(with no spaces)
        ''')


def main():
    # print('in main')
    args = sys.argv[1:]
    # print('count of args :: {}'.format(len(args)))
    # for arg in args:
    #     print('passed argument :: {}'.format(arg))

    if len(args) == 2:
        result = get_lyrics(args[1], args[0])

        print(result)

        if result == 'Lyrics found':
            os_command_string = "notepad.exe lyrics.txt"

            os.system(os_command_string)
    elif len(args) == 1:
        if args[0] == '--h' or args[0] == '--help':
            help()
        else:
            print("""
Command Not Found
------------------------------------------------------------------------------------------------------------
for help use '--h' or '--help'
                """)
    elif len(args) == 0:
        intro()



if __name__ == '__main__':
    main()
