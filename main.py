import turtle
import pandas as pd
import time
TV = turtle.Screen()
TV.bgpic("Map.gif")
TV.setup(1400, 800, 0, 0)
TV.title("Arab Map Game")



Data = pd.read_csv("Cities_location.csv")
countries = Data.country.to_list()
gussed = []
missed_country = []

while len(gussed) < 21:
    answer = TV.textinput(title=f"Guess a country! {len(gussed)}/21 ", prompt=" Type a country name and hit Enter (Exit to left ...) !")
    if answer is None:
        continue
    answer = answer.title()

    if answer in countries:
        gussed.append(answer)
        marker = turtle.Turtle()
        marker.hideturtle()
        marker.penup()
        country_x = Data[Data.country == answer]["xcore"].item()
        country_y = Data[Data.country == answer]["ycore"].item()
        marker.goto(country_x, country_y)
        marker.dot(10, "red")
        marker.color("green")
        marker.write(f"{answer}", font=("arial",10))     
        if len(gussed) == 21:
            marker.goto(0,0)
            marker.color("gold")
            marker.write("Congratulations ⭐", align="center", font=("arial", 45, "bold"))
            marker.goto(0, -75)
            marker.write("Click on screen to exit ...", align="center", font=("arial", 30, "bold"))
            break


    elif answer == "Exit":
        for miss in countries:
            if miss not in gussed:
                missed_country.append(miss)
        pd.DataFrame(missed_country, columns=["country_miss"]).to_csv("missed_country.csv")
        time.sleep(1)
        TV.bye()
        
        break


TV.exitonclick()
        
        


