from threading import Timer
from app.service.mood_checker import mood_checker


def timeout(limit: int, message: str, audience):
    t = Timer(limit, print, ["you are ruining the show"])
    t.start()
    prompt = f"You have {limit} seconds to choose the correct answer...: "
    answer = input(prompt)
    if answer == "p":
        print(message)
        t.cancel()
    elif audience.total == 0:
        t.cancel()
    else:
        audience.total -= 10
        mood_checker(audience)
        print(f"you are ruining the show, \n total:{audience.total} \n mood:{audience.mood}")
        t.cancel()
