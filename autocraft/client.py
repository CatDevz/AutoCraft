import socket, threading, json
from requests import post


class Client:
    def __init__(self, email, password):
        self.connection = None

        # Generating a payload to send to Mojang's auth servers
        payload = {
            "agent": {
                "name": "Minecraft",
                "version": 1
            },
            "username": email,
            "password": password,
            "requestUser": True }

        # Sending auth request to Moajng's servers
        res = post(
            "https://authserver.mojang.com/authenticate", 
            json.dumps(payload), 
            headers={
                "content-type": "application/json", 
                "user-agent": "AutoCraft"})
        if res.status_code == 403:
            print("Invalid username & password")
            return
        elif 200 > res.status_code > 299:
            print(res, res.json(), sep='\n')
            return
        res = res.json()

        self.token = res['accessToken']
        self.name = res['selectedProfile']['name']
        self.uuid = res['selectedProfile']['id']

        print(json.dumps(res, indent=2, sort_keys=True))

    def connect(self, ip, port=25565):
        if self.connection:
            raise Exception("Client already connected to a server.")
        self.connection = (ip, port)

    def disconnect(self):
        if not self.connection:
            raise Exception("Client not connected to a server.")
        # TODO: Add disconnection stuff here
        self.connection = None

    def __handshake(self):
        pass

