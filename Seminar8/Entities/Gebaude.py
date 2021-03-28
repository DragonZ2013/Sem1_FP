class Gebaude():
    def __init__(self, Raume):
        self.__Raume = Raume

    def print_rooms(self):
        for r in self.__Raume:
            print(r)

    def wievielPlatz(self, arr):
        for r in self.__Raume:
            if r.name==arr:
                return r.nr
        return None

    def write_file(self):
        f=open("rooms.txt", "w")
        for r in self.__Raume:
            f.write(str(r)+'\n')
        f.close()

    def read_file(self):
        f=open("rooms.txt", "r")
        for l in f.readlines():
            s = l.strip("-")
            print(s.split())




