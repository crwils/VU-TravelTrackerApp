import pdb
from models.country import Country
from models.vu_point import Vu_point

import repositories.country_repository as country_repository
import repositories.vu_point_repository as vu_point_repository

country_repository.delete_all()
vu_point_repository.delete_all()

country_1 = Country("Spain", "Madrid", "Europe", True)
country_repository.save(country_1)

country_2 = Country("Fiji", "Suva", "South Pacific", True)
country_repository.save(country_2)

vu_point_1 = Vu_point("Es Vedra", country_1, 8, "Es Vedrà is a small rocky island off the south western seaboard of the Spanish island of Ibiza.", False)
vu_point_repository.save(vu_point_1)

vu_point_2 = Vu_point("Nacula Island Caves", country_2, 7, "Underwater caves off the coast of Nacula Island in the Yasawa Islands.", True)
vu_point_repository.save(vu_point_2)

vu_point_3 = Vu_point("Castaway Island Rock", country_2, 9, "Cliff-edge viewpoint atop Castaway Island in the Mamanuca's.", True)
vu_point_repository.save(vu_point_3)

pdb.set_trace()