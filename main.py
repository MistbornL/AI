from threading import Timer


def timeout(limit: int, message):
    t = Timer(limit, print, ["you ruined the show"])
    t.start()
    prompt = f"You have {limit} seconds to choose the correct answer...: "
    answer = input(prompt)
    if answer == "p":
        print(message)
        t.cancel()
    else:
        print("you ruied the show")
        t.cancel()


class Orchestra:
    def __init__(self, conductor, violin, cello, strings, percusion):
        self.conductor = conductor
        self.violin = violin
        self.cello = cello
        self.strings = strings
        self.percusion = percusion

    def command_strings_start(self):
        print("conductor gives sign to play for strings!!")
        timeout(3, f"{self.strings} started playing")

    def command_strings_stop(self):
        return f"self{conductor} gives sign to stop for {self.strings}"

    def command_percusion(self):
        return f"self{conductor} gives beat to {self.percusion}"


conductor = Orchestra("lasha", "violin", "cello", "strings", "drums")
conductor.command_strings_start()
