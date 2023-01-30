insert into vehicle_brand (brand) values('Acura');
insert into vehicle_brand (brand) values('Alfa');
insert into vehicle_brand (brand) values('AM');
insert into vehicle_brand (brand) values('Aston');
insert into vehicle_brand (brand) values('Audi');
insert into vehicle_brand (brand) values('Bentley');
insert into vehicle_brand (brand) values('BMW');
insert into vehicle_brand (brand) values('Buick');
insert into vehicle_brand (brand) values('Cadillac');
insert into vehicle_brand (brand) values('Chevrolet');
insert into vehicle_brand (brand) values('Chrysler');
insert into vehicle_brand (brand) values('Dodge');
insert into vehicle_brand (brand) values('Ferrari');
insert into vehicle_brand (brand) values('FIAT');
insert into vehicle_brand (brand) values('Fisker');
insert into vehicle_brand (brand) values('Ford');
insert into vehicle_brand (brand) values('Freightliner');
insert into vehicle_brand (brand) values('Genesis');
insert into vehicle_brand (brand) values('Geo');
insert into vehicle_brand (brand) values('GMC');
insert into vehicle_brand (brand) values('Honda');
insert into vehicle_brand (brand) values('HUMMER');
insert into vehicle_brand (brand) values('Hyundai');
insert into vehicle_brand (brand) values('INFINITI');
insert into vehicle_brand (brand) values('Isuzu');
insert into vehicle_brand (brand) values('Jaguar');
insert into vehicle_brand (brand) values('Jeep');
insert into vehicle_brand (brand) values('Kia');
insert into vehicle_brand (brand) values('Lamborghini');
insert into vehicle_brand (brand) values('Land');
insert into vehicle_brand (brand) values('Lexus');
insert into vehicle_brand (brand) values('Lincoln');
insert into vehicle_brand (brand) values('Lotus');
insert into vehicle_brand (brand) values('Maserati');
insert into vehicle_brand (brand) values('Maybach');
insert into vehicle_brand (brand) values('Mazda');
insert into vehicle_brand (brand) values('McLaren');
insert into vehicle_brand (brand) values('Mercedes-Benz');
insert into vehicle_brand (brand) values('Mercury');
insert into vehicle_brand (brand) values('MINI');
insert into vehicle_brand (brand) values('Mitsubishi');
insert into vehicle_brand (brand) values('Nissan');
insert into vehicle_brand (brand) values('Oldsmobile');
insert into vehicle_brand (brand) values('Plymouth');
insert into vehicle_brand (brand) values('Pontiac');
insert into vehicle_brand (brand) values('Porsche');
insert into vehicle_brand (brand) values('Ram');
insert into vehicle_brand (brand) values('Rolls-Royce');
insert into vehicle_brand (brand) values('Saab');
insert into vehicle_brand (brand) values('Saturn');
insert into vehicle_brand (brand) values('Scion');
insert into vehicle_brand (brand) values('smart');
insert into vehicle_brand (brand) values('Subaru');
insert into vehicle_brand (brand) values('Suzuki');
insert into vehicle_brand (brand) values('Tesla');
insert into vehicle_brand (brand) values('Toyota');
insert into vehicle_brand (brand) values('Volkswagen');
insert into vehicle_brand (brand) values('Volvo');


insert into city("City_Car")
select true_car_listings."City" from true_car_listings 
group by true_car_listings."City"
order by true_car_listings."City" asc;

insert into state("State_Car")
select true_car_listings."State" from true_car_listings 
group by true_car_listings."State"
order by true_car_listings."State" asc;

insert into model("Model_Car")
select true_car_listings."Model" from true_car_listings 
group by true_car_listings."Model"
order by true_car_listings."Model" asc;


alter table true_car_listings
add constraint FK_Model
foreign key ("Model")
references model ("Model_Car")

alter table true_car_listings
add constraint FK_State
foreign key ("State")
references state ("State_Car")

alter table true_car_listings
add constraint FK_Make
foreign key ("Make")
references make ("Make_Car")

alter table true_car_listings
add constraint FK_City
foreign key ("City")
references city ("City_Car")
