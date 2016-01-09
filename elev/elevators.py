# -*- coding: utf-8 -*-
import pickle

def myElevators():
    f = open(r'/home/iraqez/PycharmProjects/Gis12/elev/123', 'r')
    s = f.readline()
    f.close()
    s = s.replace('\\"','"')
    z = s.split('_')
    l2 = []
    for i in z:
        l2.append(parsToDict(i))


    return l2

def parsToDict(z):

    from slimit import ast
    from slimit.parser import Parser
    from slimit.visitors import nodevisitor

    data = z

    parser = Parser()
    tree = parser.parse(data)
    fields = {getattr(node.left, 'value', ''): getattr(node.right, 'value', '')
              for node in nodevisitor.visit(tree)
              if isinstance(node, ast.Assign)}
    fields.pop('')
    if KeyError:
        pass


    for key, values in fields.items(): fields[key]=values[1:-1]
    return fields

if __name__ == '__main__':
    files = open(r'/home/iraqez/PycharmProjects/Gis12/elev/pl', 'wb')
    a = myElevators()
    pickle._dump(a, files)
    files.close()