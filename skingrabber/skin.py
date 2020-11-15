import requests
import json


class skingrabber:
    """This is the class for all skingrabber functions"""

    def __init__(self):
        self.url = "https://api.mojang.com/users/profiles/minecraft/"

    def get_uuid(self, user: str):

        """user is the nickname of the player in this case"""
        print("Searching...")
        response = requests.get(self.url + user)
        if response.status_code != 200:
            print("That player doesn't seem to exist")
        else:
            responsejson = json.loads(response.content)

            uuid = responsejson["id"]
            return uuid

    def get_skin(self, user: str):
        """The 2D version of the users skin"""

        print("Searching...")
        response = requests.get(self.url + user)
        if response.status_code != 200:
            print("That player doesn't seem to exist!")
        else:
            responsejson = json.loads(response.content)

            uuid = responsejson["id"]
            return f"https://crafatar.com/skins/{uuid}"

    def get_skin_rendered(self, user: str):
        """The 3D rendered version of the users skin"""

        print("Searching...")
        response = requests.get(self.url + user)
        if response.status_code != 200:
            print("That player doesn't seem to exist!")
        else:
            responsejson = json.loads(response.content)

            uuid = responsejson["id"]
            return f"https://crafatar.com/renders/body/{uuid}"
