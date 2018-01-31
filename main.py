import sys
from src.generator import Generator

if (__name__ == '__main__'):
    try:
        Generator.generates(argv[1])
    except IndexError as e:
        print("Haven't you forgot to specify a '.ptex' file ?")
    except Exception as e:
        print("Well... Something really unexpected happened.")
        print(e)
