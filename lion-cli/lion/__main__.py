import sys
import os

def main():
    args = sys.argv[1:]

    # call the interpreter :
    if len(args) == 0:
        os.system("python " + os.path.abspath("..") + "/lion.py")
        pass
    # generate the pycode for the input files :
    else:
        for arg in args:
            pass
    
if __name__ == '__main__':
    main()