def mood_checker(audience):
    if audience.total <= 70:
        audience.mood = "bored"
    elif audience.total == 80:
        audience.mood = "normal"
    elif audience.total > 80:
        audience.mood = "happy"
