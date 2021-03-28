from Raum import Raum
from Unterraum import Unterraum
from Entities.Gebaude import Gebaude

x = Raum("abc", 1)
y = Raum("xyz", 2)

print(x,y,x==y)

z= Unterraum("abc",1,"Linux")
print(z,z==x)

G=Gebaude([x,y,z])

G.print_rooms()
print(G.wievielPlatz("xyz"))

#G.write_file()
G.read_file()