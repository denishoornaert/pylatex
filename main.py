import sys
from src.generator import Generator

if (__name__ == '__main__'):
    try:
        Generator.generates(sys.argv[1])
    except IndexError as e:
        print("Haven't you forgot to specify a '.ptex' file ?")
    except EOFError as e:
        print("Are you sure that you have closed all your python environments ?")
    else:
        print("Well... Something really unexpected happened.")
