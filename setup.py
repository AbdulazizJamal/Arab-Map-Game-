import turtle

import pandas as pd

TV = turtle.Screen()
TV.bgpic("Map.gif")
TV.setup(1400, 800, 0, 0)
TV.title("Arab Map Game")

# قائمة لتجميع البيانات 
data_list = []


def add_country(x,y):
    country = TV.textinput(title="إضافة دولة", prompt= f"الإحداثيات, ({int(x), int(y)})\nادخل اسم الدولة (او اتركها فارغة للإلغاء)")

    if country and country.strip():
        country_name = country.strip()
    



# 1 - إظهار رد فعل بصري 
    marker = turtle.Turtle()
    marker.hideturtle()
    marker.penup()
    marker.goto(x, y)
    marker.dot(10, "red")
    marker.write(f" {country_name}", font=("Arial", 9, "bold"))


# 2 - حفظ البيانات في القائمة 
    data_list.append({
        "country": country_name,
        "xcore": int(x),
        "ycore": int(y),
    })

    print(f"تمت إضافة: {country_name} --> {int(x)}, {int(y)}")

turtle.onscreenclick(add_country)
turtle.mainloop()

if data_list:
    df = pd.DataFrame(data_list)
    df.to_csv("Cities_location.csv", mode="a", index=False, encoding="utf-8-sig")
    print("تم حفظ جميع الإحداثيات بنجاح في ملف Cities_location.csv.csv")
