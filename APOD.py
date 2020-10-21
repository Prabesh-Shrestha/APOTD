#QxpEp29XVShhKSwmHCJ6ozqUkga25ub581umUhe2
from tkinter import *
import requests
import os
from PIL import ImageTk, Image
root = Tk()
root.title("APOD")

url = "https://api.nasa.gov/planetary/apod?api_key=QxpEp29XVShhKSwmHCJ6ozqUkga25ub581umUhe2"
a = requests.get(url)
response = a.json()
print(response)
photo_url = response['url']
date = str(response['date'])
print(date)
exp = response['explanation']
print("URL request sent")
b = requests.get(photo_url)
try:
    os.remove("APOD.png")
    print("deleted the file")
except:
    pass
with open("APOD.png", "wb") as f:
    f.write(b.content)

def ex():
    root.quit()
images = ImageTk.PhotoImage(Image.open("APOD.png"))
img = Label(image=images).grid(row =0, column =1, rowspan = 10)

data = Label(text = date).grid(row =0 , column = 0)
exits = Button(text = "Exit", command = ex, padx = 25, pady = 300).grid(row =1 , column = 0)
root.mainloop()