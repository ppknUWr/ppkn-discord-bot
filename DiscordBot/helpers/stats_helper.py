import time

BOT_ID = 771875014651805727

"""
count_how_long_is_member_playing
Pozwala dla danego slownika obliczyc, ile procent taskow mogl zrobic uzytkownik, zamiast grac w gry

@param timestamp: Float z czasem, kiedy uzytkownik zaczal w cos grac w formie timestamp
@return czas: Float procent taskow, jaki mogl zrobic uzytkownik
"""

def count_how_long_is_member_playing(start):
    start = (start * 1000) + 3_600_000 # 3_600_00 poniewaz musimy dodac godzine, bo w Polsce jest inna strefa czasowa
    now = int(round(time.time() * 1000))
    diff = round( (now - start) / 1000 )
    bot_per_second = 0.0001
    return round(diff * bot_per_second, 5)