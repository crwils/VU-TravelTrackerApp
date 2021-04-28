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


country1 = Country("Australia", True)
country_repository.save(country1)

country2 = Country("Belgium", True)
country_repository.save(country2)

country3 = Country("Cambodia", True)
country_repository.save(country3)

country4 = Country("Croatia", True)
country_repository.save(country4)

country5 = Country("Czech Republic", True)
country_repository.save(country5)

country6 = Country("Fiji", True)
country_repository.save(country6)

country7 = Country("France", True)
country_repository.save(country7)

country8 = Country("Germany", True)
country_repository.save(country8)

country9 = Country("Greece", True)
country_repository.save(country9)

country10 = Country("Hong Kong", True)
country_repository.save(country10)

country11 = Country("Indonesia", True)
country_repository.save(country11)

country12 = Country("India", True)
country_repository.save(country12)

country13 = Country("Ireland", True)
country_repository.save(country13)

country14 = Country("Jordan", True)
country_repository.save(country14)

country15 = Country("Lebanon", True)
country_repository.save(country15)

country16 = Country("Malaysia", True)
country_repository.save(country16)

country17 = Country("Netherlands", True)
country_repository.save(country17)

country18 = Country("Oman", True)
country_repository.save(country18)

country19 = Country("Qatar", True)
country_repository.save(country19)

country20 = Country("Singapore", True)
country_repository.save(country20)

country21 = Country("Spain", True)
country_repository.save(country21)

country22 = Country("Sri Lanka", True)
country_repository.save(country22)

country23 = Country("Thailand", True)
country_repository.save(country23)

country24 = Country("Turkey", True)
country_repository.save(country24)

country25 = Country("United Kingdom", True)
country_repository.save(country25)

country26 = Country("United Arab Emirates", True)
country_repository.save(country26)

country27 = Country("United States of America", True)
country_repository.save(country27)

country28 = Country("Vanuatu", True)
country_repository.save(country28)

country29 = Country("Vietnam", True)
country_repository.save(country29)

country30 = Country("Colombia", False)
country_repository.save(country30)

country31 = Country("Costa Rica", False)
country_repository.save(country31)

country32 = Country("Hawaii", False)
country_repository.save(country32)

country33 = Country("Mexico", False)
country_repository.save(country33)

country34 = Country("Nepal", False)
country_repository.save(country34)

country35 = Country("Namibia", False)
country_repository.save(country35)

country36 = Country("New Zealand", False)
country_repository.save(country36)

country37 = Country("Philippines", False)
country_repository.save(country37)

country38 = Country("Peru", False)
country_repository.save(country38)
# country_2 = Country("Fiji", True)
# country_repository.save(country_2)

# country_3 = Country("Ghana", True)
# country_repository.save(country_3)

# country_4 = Country("Belgium", False)
# country_repository.save(country_4)

location_1 = Location("McMahon's Point, North Sydney", country1)
location_repository.save(location_1)

location_2 = Location("Blue Mountains", country1)
location_repository.save(location_2)

location_3 = Location("Royal National Park", country1)
location_repository.save(location_3)

vu_point_1 = Vu_point("Sydney Harbour Bridge", location_1, country1,
                      8, "Lesser known spot to take in the bridge in all its glory.", True)
vu_point_repository.save(vu_point_1)

vu_point_2 = Vu_point("Three Sisters", location_2, country1, 8,
                      "Cool rock formation in the Blue Mountains, near Katoomba West of Sydney.", True)
vu_point_repository.save(vu_point_2)

vu_point_3 = Vu_point("Wedding Cake Rock", location_3, country1, 9,
                      "Sandstone rock formation that looks like a wedding cake! Now blocked off to the public due to fears of erosion making it unsafe.", True)
vu_point_repository.save(vu_point_3)

# change repositories to add city in vu_point save and create save for city in city_repository
pdb.set_trace()
