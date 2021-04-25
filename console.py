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


country_1 = Country("Spain", False)
country_repository.save(country_1)

country_2 = Country("Fiji", True)
country_repository.save(country_2)

country_3 = Country("Indonesia", True)
country_repository.save(country_3)


location_1 = Location("Madrid", country_1)
location_repository.save(location_1)

location_2 = Location("Ubud, Bali", country_3)
location_repository.save(location_2)

location_3 = Location("Nacula, Yasawa Islands", country_2)
location_repository.save(location_3)

location_4 = Location("Ibiza Town, Ibiza", country_1)
location_repository.save(location_4)

location_5 = Location("Monuriki Island, Mamanuca Islands", country_2)
location_repository.save(location_5)


vu_point_1 = Vu_point("Es Vedra", location_3, country_1, 8, "Es Vedrà is a small rocky island off the south western seaboard of the Spanish island of Ibiza.", False)
vu_point_repository.save(vu_point_1)

vu_point_2 = Vu_point("Blue Lagoon", location_3, country_2, 7, "Underwater caves off the coast of Nacula Island in the Yasawa Islands.", True)
vu_point_repository.save(vu_point_2)

vu_point_3 = Vu_point("Castaway Island Rock", location_5, country_2, 9, "Cliff-edge viewpoint atop Castaway Island in the Mamanuca's.", True)
vu_point_repository.save(vu_point_3)

vu_point_4 = Vu_point("Tegalalang Rice Terrace", location_2, country_3, 10, "Rice terraces in the Ubud region of Bali", True)
vu_point_repository.save(vu_point_4)
# change repositories to add city in vu_point save and create save for city in city_repository
pdb.set_trace()