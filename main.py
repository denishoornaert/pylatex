import sys
from pythonInjector.src.generator import Generator
from pythonInjector.src.lexer.error import UnclosedEnvironmentError

if (__name__ == '__main__'):
    try:
        Generator.generates(sys.argv[1])
    except IndexError as e:
        print("Haven't you forgot to specify a '.ptex' file ?")
    except UnclosedEnvironmentError as e:
        print("Are you sure that you have closed all your python environments ?")
    except Exception as e:
        print("Well... Something really unexpected happened.")
        print("Hint : "+str(e))
