from app.service.timeout import timeout


class Orchestra:
    def __init__(self, conductor: str, violin: str, cello: str, strings: str, percusion: str):
        self.conductor = conductor
        self.violin = violin
        self.cello = cello
        self.strings = strings
        self.percusion = percusion

    def command_strings_start(self, audience):
        print("conductor gives sign to play for strings!!")
        timeout(3, f"{self.strings} started playing", audience)

    def command_strings_stop(self, audience):
        print(f"{self.conductor} gives sign to stop for {self.strings}")
        timeout(3, f"{self.strings} stoped playing", audience)

    def command_percusion_start(self, audience):
        print(f"{self.conductor} gives beat to {self.percusion}")
        timeout(3, f"{self.percusion} started playing", audience)

    def command_percusion_stop(self, audience):
        print(f"{self.conductor} gives beat to {self.percusion}")
        timeout(3, f"{self.percusion} stoped playing", audience)
