import requests
import json


class skingrabber:
    """This is the class for all skingrabber functions"""

    def __init__(self):
        self.url = "https://api.mojang.com/users/profiles/minecraft/"

    def get_uuid(self, user):
        """user is the nickname of the player in this case"""

        response = requests.get(self.url + user)
        if response.status_code != 200:
            pass
        else:
            responsejson = json.loads(response.content)

            uuid = responsejson["id"]
            return uuid

    def get_skin(self, user):
        """The 2D version of the users skin"""

        response = requests.get(self.url + user)
        if response.status_code != 200:
            pass
        else:
            responsejson = json.loads(response.content)

            uuid = responsejson["id"]
            return f"https://crafatar.com/skins/{uuid}"

    def get_skin_rendered(self, user):
        """The 3D rendered version of the users skin"""

        response = requests.get(self.url + user)
        if response.status_code != 200:
            pass
        else:
            responsejson = json.loads(response.content)

            uuid = responsejson["id"]
            return f"https://crafatar.com/renders/body/{uuid}"

    @staticmethod
    def __version__():
        return "0.1.5"
