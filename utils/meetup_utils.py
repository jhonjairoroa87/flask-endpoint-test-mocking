import meetup.api
from settings import MEETUP_API_KEY


class MeetupUtils:
    """
    Contains meetup api client instance and methods to interact with the api
    """

    def __init__(self):
        self.__client__ = meetup.api.Client(MEETUP_API_KEY)

    def get_all_groups(self):
        """
        Get all the python groups from meetup api
        """
        found_places = []
        python_groups = self.__client__.GetFindGroups({'text': 'python'})
        # TODO: there should be a better place to map the fields from the api groups
        for python_group in python_groups:
                found_places.append({
                    'country_code': python_group.country,
                    'country_name': python_group.localized_country_name,
                    'city': python_group.city,
                    'members': python_group.members,
                    'name': python_group.name,
                })
        return found_places
