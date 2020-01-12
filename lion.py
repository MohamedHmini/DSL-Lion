import readline
import textx as tx
import templateEngine as te
from textx.model import get_children
import os

os.chdir('..')


def tree_generator(node, prefix = '-'):
    print(prefix, node.__class__.__name__)
    try:
        for child in node.rules:
            if child != node:
                tree_generator(child, prefix + "--")
    except:
        pass


def save_code(pycode):
    pyfile = open("pycode.py","w+")
    pyfile.write(pycode)
    pyfile.close()


readline.write_history_file( '.lion_history' )
readline.set_history_length(1000)
mm = tx.metamodel_from_file('LION_META_MODEL.tx')

AllofCode = []
pycode = te.genDependenciesCode()
exec(pycode)

while(True):
    temp = AllofCode.copy()
    try : 
        c = input("lion> ")
        while(True) :
            if ';' in c:
                break
            c += input("...    ")
        temp.append(c)
        m = mm.model_from_str('\n'.join(temp))
        code = te.genCode(m.rules[-1])
        exec(code)
        pycode += code
        AllofCode.append(c)
    except EOFError :
        print("\r   bye :(")
        save_code(pycode)
        break
    except KeyboardInterrupt:
        print("\ntype exit() or EOF to quit!")
    except SyntaxError as e:
        print("Invalid Syntax ERRROR", e)
    except Exception as e:
        print(e)