import sys
from .get_lyrics import get_lyrics


def main():
    print('in main')
    args = sys.argv[1:]
    print('count of args :: {}'.format(len(args)))
    for arg in args:
        print('passed argument :: {}'.format(arg))

    lyrics, result = get_lyrics(args[1], args[0])

    print(result)

#     my_function('hello world')
#     my_object = MyClass('Thomas')
#     my_object.say_name()
if __name__ == '__main__':
    main()
