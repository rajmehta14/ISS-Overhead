import requests
import datetime
import smtplib
import time
LAT=23.0216238
LNG=72.5797068
e = "rajmehta2300@gmail.com"
password = "pnzdbwmzqkqklzju"
user_name = e.split('@')[0]

def overhead():
    response=requests.get("http://api.open-notify.org/iss-now.json")
    data=response.json()
    latitude = float(data["iss_position"]["latitude"])
    longitude=float(data["iss_position"]["longitude"])

    if LAT-5<= latitude >= LAT+5 and LNG-5 <= longitude >= LNG+5:
        return True



parameters={
    "lat":LAT,
    "lng":LNG,
    "formatted":0
}

def is_night():

    response = requests.get("https://api.sunrise-sunset.org/json",params=parameters)

    response.raise_for_status()
    data=response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])

    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])
    print(sunrise)
    print(sunset)

    t=datetime.datetime.now().hour
    print(t)
    if t>=sunset and t<=sunrise:
        return True





while True:
    time.sleep(60)
    if overhead() and is_night():


        connection = smtplib.SMTP("smtp.gmail.com", 587)
        connection.starttls()
        connection.login(user=user_name, password=password)
        connection.sendmail(from_addr=e, to_addrs="rajmehta2300@gmail.com", msg=f"Subject:ISS overhead alert!!!\n\nLook up")
        connection.quit()



