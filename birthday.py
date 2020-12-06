#!/usr/bin/env python3
#code for wish me birthday
#Author Ankush Das
#02/12/2020 11:47pm
import sys
import time
from datetime import date
import smtplib
import os
from os import path
from twilio.rest import Client

if not path.exists('tokens.txt'):
    print("First creat a twillo account  and follow there instruction :)")
    ssid = str(input("Enter Your Twillo ssid >>"))
    token = str(input("Enter Your Twillo auth_token>>"))
    number = str(input("Enter your number>>(with country code)"))
    wp-number =  str(input("Enter twillo number >>"))
    date = input("Enter Your birth date(ex:03/12/2003)>>")
    date = date.split("/")
    with open("tokens.txt", "w+") as file:
        file.write(ssid+"\n"+token+"\n"+number+"\n"+wp-number+"\n"+str(date[0])+"\n"+str(date[1]))
    print("Every Thing Done :)")
    print("Open The program again : )")
    sys.exit()
else:
    with open("tokens.txt", "r+") as file :
        x = file.readlines()
        pass
def massage():
    account_sid = x[0]
    auth_token = x[1]
    client = Client(account_sid, auth_token)

    message = client.messages.create(
                                body='Hey  i know no one wish but mai hu na wish you many many happy birth day, Wish you a many many happy returns of the day. May God bless you with health, wealth and prosperity in your life. HAPPY BIRTHDAY',
                                from_='whatsapp:'+x[2],
                                to='whatsapp:'+x[3]
                                )
if __name__ == "__main__":
    try:
        while True:
            t = date.today()
            d1 = t.strftime("%d/%m/%Y")
            d1 = d1.split("/")
            d = str(int(x[3])-int(d1[0])) 
            m = str(int(x[4])-int(d1[1]))
            if d == "0" and m == "0":
                print("Today is Your Birth Day")
                print("Sending massge to "+str(x[3]))
                massage()
                sys.exit()
            else:
                print("Your birth day is left by "+str(d)+" days and "+str(m)+" months")
                if d > "2":
                    time.sleep(86400)
                else:
                    time.sleep(60)
    except KeyboardInterrupt:
        print("Quiting ......")
    except Exception as e:
        print("Error Detected \n Error:\n "+str(e))
