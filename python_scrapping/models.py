from sqlmodel import Field, SQLModel

#CSV
class true_car_listings(SQLModel, table=True):
    Id: int = Field(default=None, primary_key=True)
    Price: int
    Year: int
    Mileage: int
    City: str
    State: str
    Vin: str
    Make: str
    Model: str
    InformacionActualizada: str
    
    def __init__(self, Price: int = 0, Year: int = 0, Mileage: int = 0, City: int = 0, State: str = '', Vin: str = '', Make: str = '', Model: str = '', InformacionActualizada: bool = False) -> None:
        #self.Id = Id
        self.Price = Price
        self.Year = Year
        self.Mileage = Mileage
        self.City = City
        self.State = State
        self.Vin = Vin
        self.Make = Make
        self.Model = Model
        self.InformacionActualizada = InformacionActualizada

class true_cars_test(SQLModel, table=True):
    Id: int = Field(default=None, primary_key=True)
    Price: int
    Year: int
    Mileage: int
    City: str
    State: str
    Vin: str
    Make: str
    Model: str
    InformacionActualizada: str
    
    def __init__(self, Price: int = 0, Year: int = 0, Mileage: int = 0, City: int = 0, State: str = '', Vin: str = '', Make: str = '', Model: str = '', InformacionActualizada: bool = False) -> None:
        #self.Id = Id
        self.Price = Price
        self.Year = Year
        self.Mileage = Mileage
        self.City = City
        self.State = State
        self.Vin = Vin
        self.Make = Make
        self.Model = Model
        self.InformacionActualizada = InformacionActualizada
        
class true_cars_train(SQLModel, table=True):
    Id: int = Field(default=None, primary_key=True)
    Price: int
    Year: int
    Mileage: int
    City: str
    State: str
    Vin: str
    Make: str
    Model: str
    InformacionActualizada: str
    
    def __init__(self, Price: int = 0, Year: int = 0, Mileage: int = 0, City: int = 0, State: str = '', Vin: str = '', Make: str = '', Model: str = '', InformacionActualizada: bool = False) -> None:
        #self.Id = Id
        self.Price = Price
        self.Year = Year
        self.Mileage = Mileage
        self.City = City
        self.State = State
        self.Vin = Vin
        self.Make = Make
        self.Model = Model
        self.InformacionActualizada = InformacionActualizada        

#https://vincheckpro.com       
class fuel(SQLModel, table=True):
    Id: int = Field(default=None, primary_key=True)
    Vin: str #= Field(default=None, primary_key=True)
    CityMileage: float
    HighwayMileage: float
    FuelType: str
    FuelCapacity: float
    
    def __init__(self, Vin: str = '', CityMileage: float = 0, HighwayMileage: float = 0, FuelType: str = '', FuelCapacity: float = 0) -> None:
        #self.Id = Id
        self.Vin = Vin
        self.CityMileage = CityMileage
        self.HighwayMileage = HighwayMileage
        self.FuelType = FuelType
        self.FuelCapacity = FuelCapacity
                
                
class market_value(SQLModel, table=True):
    Id: int = Field(default=None, primary_key=True)
    #Vin: str = Field(default=None, primary_key=True)
    Vin: str
    InvoicePrice: float
    BelowMarketPrice: float
    AverageMarketPrice: float
    AboveMarketPrice: float
    
    def __init__(self, Vin: str = '', InvoicePrice: float = 0, BelowMarketPrice: float = 0, AverageMarketPrice: float = 0, AboveMarketPrice: float = 0) -> None:
        #self.Id = Id
        self.Vin = Vin
        self.InvoicePrice = InvoicePrice
        self.BelowMarketPrice = BelowMarketPrice
        self.AverageMarketPrice = AverageMarketPrice
        self.AboveMarketPrice = AboveMarketPrice
        
        
class safety_rating(SQLModel, table=True):
    Id: int = Field(default=None, primary_key=True)
    Vin: str
    RoofStrengthTestResults: str
    RearCrashProtectionHeadRestraintRatings: str
    SmallOverlapFrontTestResults: str
    ModerateOverlapFrontTestResults: str
    SideImpactTestResults: str
    
    def __init__(self, Vin: str = '', RoofStrengthTestResults: str = '', RearCrashProtectionHeadRestraintRatings: str = '', SmallOverlapFrontTestResults: str = '', ModerateOverlapFrontTestResults: str = '', SideImpactTestResults: str = '') -> None:
        self.Vin = Vin
        self.RoofStrengthTestResults = RoofStrengthTestResults
        self.RearCrashProtectionHeadRestraintRatings = RearCrashProtectionHeadRestraintRatings
        self.SmallOverlapFrontTestResults = SmallOverlapFrontTestResults
        self.ModerateOverlapFrontTestResults = ModerateOverlapFrontTestResults
        self.SideImpactTestResults = SideImpactTestResults    
    
      
class specifications_car(SQLModel, table=True):
    Id: int = Field(default=None, primary_key=True)
    Vin: str
    TrimPremiumPackage: str
    CountryOrigin: str
    VehicleType: str
    VehicleSize: str
    TransmissionType: str
    Doors: int
    
    def __init__(self, Vin: str = '', TrimPremiumPackage: str = '', CountryOrigin: str = '', VehicleType: str = '', VehicleSize: str = '', TransmissionType: str = '', Doors: int = 0) -> None:
        self.Vin = Vin
        self.TrimPremiumPackage = TrimPremiumPackage
        self.CountryOrigin = CountryOrigin
        self.VehicleType = VehicleType
        self.VehicleSize = VehicleSize
        self.TransmissionType = TransmissionType   
        self.Doors = Doors          
      
      
#https://driving-tests.org/vin-decoder
class info_car(SQLModel, table=True):
    Id: int = Field(default=None, primary_key=True)
    Vin: str
    Manufactured: str
    Plant_Company_Name: str
    Vehicle_Type: str
    Series: str
    Body_Class: str
    Doors: int
    Front_Airbag_Location: str
    Seat_Belts_Type: str
    Engine_Displacement_CI: float
    Engine_Displacement_CC: float
    Fuel_Type: str
    Engine_Number_Cylinders: int
        
    def __init__(self, Vin: str = '', Manufactured: str = '', Plant_Company_Name: str = '', Vehicle_Type: str = '', Series: str = '', Body_Class: str = '', Doors: int = 0,
                 Front_Airbag_Location: str = '', Seat_Belts_Type: str = '', Engine_Displacement_CI: float = 0, Engine_Displacement_CC: float = 0,  Fuel_Type: str = '',
                 Engine_Number_Cylinders: int = 0) -> None:
        self.Vin = Vin
        self.Manufactured = Manufactured
        self.Plant_Company_Name = Plant_Company_Name
        self.Vehicle_Type = Vehicle_Type
        self.Series = Series
        self.Body_Class = Body_Class   
        self.Doors = Doors  
        self.Front_Airbag_Location = Front_Airbag_Location
        self.Seat_Belts_Type = Seat_Belts_Type
        self.Engine_Displacement_CI = Engine_Displacement_CI
        self.Engine_Displacement_CC = Engine_Displacement_CC
        self.Fuel_Type = Fuel_Type
        self.Engine_Number_Cylinders = Engine_Number_Cylinders
        
class aditional_info_car(SQLModel, table=True):
    Id: int = Field(default=None, primary_key=True)
    Vin: str
    Bed_Type: str
    Cab_Type: str
    Engine_Model: str
    Engine_Power: float
    Vehicle_Weight: str
    Transmission_Style: str
    Trim: str
    Air_Bag_Locations: str
    Valve_Train_Design: str
    Transmission_Speeds: str
    Engine_Configuration: str
    Engine_Manufacturer: str
        
    def __init__(self, Vin: str = '', Bed_Type: str = '', Cab_Type: str = '', Engine_Model: str = '', Engine_Power: int = 0, Vehicle_Weight: str = '', Transmission_Style: str = '',
                 Trim: str = '', Air_Bag_Locations: str = '', Valve_Train_Design: str = '', Transmission_Speeds: str = '',  Engine_Configuration: str = '',
                 Engine_Manufacturer:str = '') -> None:
        self.Vin = Vin
        self.Bed_Type = Bed_Type
        self.Cab_Type = Cab_Type
        self.Engine_Model = Engine_Model
        self.Engine_Power = Engine_Power
        self.Vehicle_Weight = Vehicle_Weight   
        self.Transmission_Style = Transmission_Style  
        self.Trim = Trim
        self.Air_Bag_Locations = Air_Bag_Locations
        self.Valve_Train_Design = Valve_Train_Design
        self.Transmission_Speeds = Transmission_Speeds
        self.Engine_Configuration = Engine_Configuration
        self.Engine_Manufacturer = Engine_Manufacturer    
        
## csv registro unico             
class registro_unico_vin(SQLModel, table=True):
    Id: int = Field(default=None, primary_key=True)
    Clave: str
    Make: str
    Model: str
    Vin: str
    InformacionActualizada: str
    
    def __init__(self, Clave: str = '', Make: str = '', Model: str = '', Vin: str = '', InformacionActualizada: bool = False) -> None:
        self.Clave = Clave
        self.Make = Make
        self.Model = Model
        self.Vin = Vin
        self.InformacionActualizada = InformacionActualizada


class info_car_registrounico(SQLModel, table=True):
    Id: int = Field(default=None, primary_key=True)
    Vin: str
    Manufactured: str
    Plant_Company_Name: str
    Vehicle_Type: str
    Series: str
    Body_Class: str
    Doors: int
    Front_Airbag_Location: str
    Seat_Belts_Type: str
    Engine_Displacement_CI: float
    Engine_Displacement_CC: float
    Fuel_Type: str
    Engine_Number_Cylinders: int
        
    def __init__(self, Vin: str = '', Manufactured: str = '', Plant_Company_Name: str = '', Vehicle_Type: str = '', Series: str = '', Body_Class: str = '', Doors: int = 0,
                 Front_Airbag_Location: str = '', Seat_Belts_Type: str = '', Engine_Displacement_CI: float = 0, Engine_Displacement_CC: float = 0,  Fuel_Type: str = '',
                 Engine_Number_Cylinders: int = 0) -> None:
        self.Vin = Vin
        self.Manufactured = Manufactured
        self.Plant_Company_Name = Plant_Company_Name
        self.Vehicle_Type = Vehicle_Type
        self.Series = Series
        self.Body_Class = Body_Class   
        self.Doors = Doors  
        self.Front_Airbag_Location = Front_Airbag_Location
        self.Seat_Belts_Type = Seat_Belts_Type
        self.Engine_Displacement_CI = Engine_Displacement_CI
        self.Engine_Displacement_CC = Engine_Displacement_CC
        self.Fuel_Type = Fuel_Type
        self.Engine_Number_Cylinders = Engine_Number_Cylinders
        
class aditional_info_car_registrounico(SQLModel, table=True):
    Id: int = Field(default=None, primary_key=True)
    Vin: str
    Bed_Type: str
    Cab_Type: str
    Engine_Model: str
    Engine_Power: float
    Vehicle_Weight: str
    Transmission_Style: str
    Trim: str
    Air_Bag_Locations: str
    Valve_Train_Design: str
    Transmission_Speeds: str
    Engine_Configuration: str
    Engine_Manufacturer: str
        
    def __init__(self, Vin: str = '', Bed_Type: str = '', Cab_Type: str = '', Engine_Model: str = '', Engine_Power: int = 0, Vehicle_Weight: str = '', Transmission_Style: str = '',
                 Trim: str = '', Air_Bag_Locations: str = '', Valve_Train_Design: str = '', Transmission_Speeds: str = '',  Engine_Configuration: str = '',
                 Engine_Manufacturer:str = '') -> None:
        self.Vin = Vin
        self.Bed_Type = Bed_Type
        self.Cab_Type = Cab_Type
        self.Engine_Model = Engine_Model
        self.Engine_Power = Engine_Power
        self.Vehicle_Weight = Vehicle_Weight   
        self.Transmission_Style = Transmission_Style  
        self.Trim = Trim
        self.Air_Bag_Locations = Air_Bag_Locations
        self.Valve_Train_Design = Valve_Train_Design
        self.Transmission_Speeds = Transmission_Speeds
        self.Engine_Configuration = Engine_Configuration
        self.Engine_Manufacturer = Engine_Manufacturer              