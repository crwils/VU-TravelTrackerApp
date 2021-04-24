import pdb
from models.country import Country
from models.vu_point import Vu_point

import repositories.country_repository as country_repository
import repositories.vu_point_repository as vu_point_repository

country_repository.delete_all()
vu_point_repository.delete_all()

country_1 = Country("Spain", "Madrid", "Europe", True)
country_repository.save(country_1)

# country_1 = Country("Spain", "Madrid", "European Union", False)
# country_repository.update(country_1)

vu_point_1 = Vu_point("Es Vedra", country_1, 8, "Es Vedrà is a small rocky island off the south western seaboard of the Spanish island of Ibiza.", False)
vu_point_repository.save(vu_point_1)

pdb.set_trace()