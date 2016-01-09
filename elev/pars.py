from elev.elevators import parsToDict

f = open(r'/home/iraqez/PycharmProjects/Gis12/elev/123', 'r')
s = f.readline()
f.close()
s.split('_')
l2 = []
for i in s[1:10]:
    l2.append(parsToDict(i))