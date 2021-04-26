import pdb
from models.country import Country
from models.vu_point import Vu_point
from models.location import Location

import repositories.country_repository as country_repository
import repositories.vu_point_repository as vu_point_repository
import repositories.location_repository as location_repository

country_repository.delete_all()
vu_point_repository.delete_all()
location_repository.delete_all()


country_1 = Country("Australia", True)
country_repository.save(country_1)

country_2 = Country("Fiji", True)


location_1 = Location("McMahon's Point, North Sydney", country_1)
location_repository.save(location_1)

location_2 = Location("Blue Mountains", country_1)
location_repository.save(location_2)

location_3 = Location("Royal National Park", country_1)
location_repository.save(location_3)

vu_point_1 = Vu_point("Sydney Harbour Bridge", location_1, country_1, 8, "Amazing view!", True)
vu_point_repository.save(vu_point_1)
vu_point_2 = Vu_point("Three Sisters", location_2, country_1, 8, "Amazing view!", True)
vu_point_repository.save(vu_point_2)
vu_point_3 = Vu_point("Wedding Cake Rock", location_3, country_1, 9, "Slightly dangerous but very cool.", True)
vu_point_repository.save(vu_point_3)

# change repositories to add city in vu_point save and create save for city in city_repository
pdb.set_trace()