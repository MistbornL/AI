class Strings:
    def __init__(self, cello, violin):
        self.cello = cello
        self.violin = violin

    def harmony(self):
        print("strings started playing")


class Conductor(Strings):
    def __init__(self, conductor):
        self.conductor = conductor

    def command_strings_start(self):
        print("conductor gives sign to play for strings!!")
        self.harmony()

    def command_strings_stop(self):
        return "conductor gives sign to stop for strings"

    def command_percusion(self):
        return "conductor gives beat to percusion"


conductor = Conductor("Lasha")
strings = Strings("cello", "violin")

conductor.command_strings_start()
