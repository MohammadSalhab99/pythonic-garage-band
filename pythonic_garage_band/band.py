from abc import ABC, abstractmethod



class Musician:
    def __init__(self,name, instrument):
        self.name = name
        self.instrument = instrument
    def __str__(self):
        return f'My name is {self.name} and I play {self.instrument}'
    @abstractmethod    
    def __repr__(self):
        pass
    def get_instrument(self):
        return  f'{self.instrument}'
    @abstractmethod
    def play_solo():
        pass







class Guitarist(Musician):
    def __init__(self,name):
        self.name=name
        self.instrument='guitar'
    def __repr__(self):
        return f'Guitarist instance. Name = {self.name}'
    def play_solo(self):
        return 'face melting guitar solo'




class Bassist(Musician):
    def __init__(self,name):
        self.name=name
        self.instrument='bass'
    def __repr__(self):
        return f'Bassist instance. Name = {self.name}'
    def play_solo(self):
        return "bom bom buh bom"


class Drummer(Musician):
    def __init__(self,name):
        self.name=name
        self.instrument='drums'
    def __repr__(self):
        return f'Drummer instance. Name = {self.name}'
    def play_solo(self):
        return "rattle boom crash"


class Band:
    band_instances=[]
    Name=""
    def __init__(self,name,members):
        Band.Name=name
        self.name = name
        self.members = members
        

    def __str__(self):
        return f'The band name is: {self.name}'
    def __repr__(self):
        return f'I am a representation for {self.name}'
    def play_solos(self):
        solos = []
        for i in self.members:
            solos.append(i.play_solo())
        return solos
    @classmethod
    def to_list(cls):
        Band.band_instances.append(cls.Name)
        return cls.band_instances
        

