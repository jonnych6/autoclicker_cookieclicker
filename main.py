from functions import CookieFunctions
CLICK_COUNT = 50
cf = CookieFunctions()

#Get everything in order
cf.prepare_settings()
game_on = True
while(game_on):
    for _ in range(CLICK_COUNT):
        cf.click_cookie()
    cf.check_upgrades()




#cf.quit_game()

