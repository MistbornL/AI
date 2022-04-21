from threading import Timer


def mood_checker(total, mood):
    if total <= 70:
        mood == "bored"
    elif total == 80:
        mood == "normal"
    elif total > 80:
        mood == "happy"


def timeout(limit: int, message):
    t = Timer(limit, print, ["you ruined the show"])
    t.start()
    prompt = f"You have {limit} seconds to choose the correct answer...: "
    answer = input(prompt)
    if answer == "p":
        print(message)
        t.cancel()
    else:
        audience.total -= 10
        mood_checker(audience.total, audience.mood)
        print(f"you are ruining the show, \n total:{audience.total} \n mood:{audience.mood}")
        t.cancel()


class Orchestra:
    def __init__(self, conductor: str, violin: str, cello: str, strings: str, percusion: str):
        self.conductor = conductor
        self.violin = violin
        self.cello = cello
        self.strings = strings
        self.percusion = percusion

    def command_strings_start(self):
        print("conductor gives sign to play for strings!!")
        timeout(3, f"{self.strings} started playing")

    def command_strings_stop(self):
        print(f"self{conductor} gives sign to stop for {self.strings}")
        timeout(3, f"{self.strings} stoped playing")

    def command_percusion_start(self):
        print(f"self{conductor} gives beat to {self.percusion}")
        timeout(3, f"{self.percusion} started playing")

    def command_percusion_stop(self):
        print(f"self{conductor} gives beat to {self.percusion}")
        timeout(3, f"{self.percusion} stoped playing")


class Audience:
    def __init__(self, total: int, mood: str):
        self.total = total
        self.mood = mood


audience = Audience(100, "normal")
conductor = Orchestra("lasha", "violin", "cello", "strings", "drums")
conductor.command_strings_start()
