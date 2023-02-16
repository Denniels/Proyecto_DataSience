from sqlmodel import Field, SQLModel


class make(SQLModel, table=True):
    Id: int = Field(default=None, primary_key=True)
    Make_Car: str
    __table_args__ = {'extend_existing': True}
    
    def __init__(self, Make_Car: str = '') -> None:        
        self.Make_Car = Make_Car
        
        
class model(SQLModel, table=True):
    Id: int = Field(default=None, primary_key=True)
    Model_Car: str
    __table_args__ = {'extend_existing': True}
    
    def __init__(self, Model_Car: str = '') -> None:        
        self.Model_Car = Model_Car  
        
class state(SQLModel, table=True):
    Id: int = Field(default=None, primary_key=True)
    State_Car: str
    __table_args__ = {'extend_existing': True}
    
    def __init__(self, State_Car: str = '') -> None:        
        self.State_Car = State_Car

class city(SQLModel, table=True):
    Id: int = Field(default=None, primary_key=True)
    City_Car: str
    __table_args__ = {'extend_existing': True}
    
    def __init__(self, City_Car: str = '') -> None:        
        self.City_Car = City_Car  
        
class fuel_type(SQLModel, table=True):
    Id: int = Field(default=None, primary_key=True)
    Fuel: str
    __table_args__ = {'extend_existing': True}
    
    def __init__(self, Fuel: str = '') -> None:        
        self.Fuel = Fuel                                