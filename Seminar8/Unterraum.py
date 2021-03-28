from Raum import Raum

class Unterraum(Raum):
    def __init__(self,name,nr,OS):
        if OS not in ["Unix", "Linux", "Windows","MacOS"]:
            raise ValueError
        Raum.__init__(self,name,nr)
        self.__OS= OS

    @property
    def OS(self): return self.__OS

    @OS.setter
    def OS(self, a): self.__OS = a

    def __str__(self):
        return self.name+" "+str(self.nr)+" "+self.__OS

