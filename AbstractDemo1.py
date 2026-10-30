from abc import ABC, abstracthmethod

class Base(ABC):
    @abstractmethod
    def Adddition(self,No1,No2):


class Derived(Base):
    pass

dobj = Derived()