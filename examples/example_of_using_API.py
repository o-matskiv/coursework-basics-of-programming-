from police_api import PoliceAPI

from police_api.forces import Force

from police_api.neighbourhoods import Neighbourhood


def main():

    api = PoliceAPI()
    # Force
    print(api.get_forces())  # All forces
    force = Force(api, id='leicestershire')  # Leicestershire Police
    print(force.description)  # description of Leicestershire Police
    # all the Neighbourhood Policing Teams in this Leicestershire Police area
    print(force.neighbourhoods)
    print(force.telephone)  # The force’s main switchboard number
    # Neighbourhood
    neighbourhood = Neighbourhood(api, force=force, id='NW02')  # neighbourhood with NW02 id
    print(neighbourhood.name)  # Name of neighbourhood (Abbey)
    print(neighbourhood.officers)  # All Abbey officers
    print(neighbourhood.events)  # Events in Abbey
    # Crimes
    anti_social_crimes = PoliceAPI().get_crimes_area(
        neighbourhood.boundary, category='anti-social-behaviour')
    print(anti_social_crimes)  # All crimes in Abbey with anti-social behaviour
    # All crimes in Abbey in October 2008
    crimes = api.get_crimes_area(neighbourhood.boundary, date='2018-10')
    crime = crimes[30]
    print(crime.location.name)  # location of crime
    print(crime.category)  # category of crime
    print(crime.outcomes)  # crime outcomes


main()
