

select * from public.true_car_listings limit 100

select * from public.true_car_listings where "Model" = 'General' limit 100

select * from public.model where model."Model_Car" = '124'

select * from public.make

update model
set "Make" = true_car_listings."Make"
from true_car_listings
--on mo.Model_Car = tcl.Model
where model."Model_Car" = true_car_listings."Model" 
and true_car_listings."Model" = '124'


select * from public.model

select  count(*) from public.info_automotora_train