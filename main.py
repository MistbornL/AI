from app.classes.audience import Audience
from app.classes.orchestra import Orchestra
from threading import Timer

audience = Audience(100, "normal")
conductor = Orchestra("lasha", "violin", "cello", "strings", "drums")

while True:
    if audience.total == 0:
        break
    else:
        conductor.command_strings_start(audience)
        conductor.command_percusion_start(audience)
        conductor.command_percusion_stop(audience)
        conductor.command_strings_stop(audience)
