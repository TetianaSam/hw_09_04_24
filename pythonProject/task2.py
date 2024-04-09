class Ship:

    def __init__(self, name, length, beam, draft):
        self.__name = name
        self.length = length
        self.beam = beam
        self.draft = draft

    def info(self):
        return f"Name: {self.__name}, Length: {self.length}, Beam: {self.beam}, Draft: {self.draft}"


class Frigate(Ship):
    def __init__(self,name, length, beam, draft, sonar_system):
        super().__init__(name, length, beam, draft)
        self.sonar_system = sonar_system

    def frigat_sonar_system(self):
        return f"Sonar system variant: {self.sonar_system}"
class Destroyer(Ship):
    def __init__(self, name, length, beam, draft, aegis_combat_system):
        super().__init__(name, length, beam, draft)
        self.aegis_combat_system = aegis_combat_system

    def info_aegis_combat_system(self):
        return f"Aegis Combat System variant: {self.aegis_combat_system}"

class Cruiser(Ship):
    def __init__(self, name, length, beam, draft, vls):
        super().__init__(name, length, beam, draft)
        self.vls = vls

    def info_vls(self):
        return f"Vertical Launch System variant: {self.vls}"

frigate = Frigate("FR",250,40,15, "Hull-mounted Sonar")
destroyer = Destroyer("DS", 320, 55,18,"Aegis Baseline 9")
cruiser = Cruiser("CS", 900, 55,20,"Mk 41 Vertical Launch System (VLS)" )

print(frigate.info())
print(frigate.frigat_sonar_system())

print(destroyer.info())
print(destroyer.info_aegis_combat_system())

print(cruiser.info())
print(cruiser.info_vls())
