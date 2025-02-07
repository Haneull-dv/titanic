from dataclasses import dataclass

@dataclass
class Dataset:
    matjip: object
    context : str
    fname: str
    id: str
    label: str


    @property
    def matjip(self) -> object:
        return self._matjip
    
    @matjip.setter
    def matjip(self,matjip):
        self._matjip = matjip

    @property
    def context(self) -> str:
        return self.context
    
    @context.setter
    def context(self,context):
        self.context = context

    @property
    def fname(self) -> str:
        return self.fname
    
    @fname.setter
    def fname(self,fname):
        self.fname = fname

    @property
    def id(self) -> str:
        return self.id
    
    @id.setter
    def id(self,id):
        self.id = id

    @property
    def label(self) -> str:
        return self.label
    
    @label.setter
    def label(self,label):
        self.label = label