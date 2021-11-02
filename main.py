import builtins
import tkinter as tk
from tkinter import*
from bs4 import BeautifulSoup
import requests
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_5)AppleWebKit/605.1.15 (KHTML, like Gecko)Version/12.1.1 Safari/605.1.15)'}

v=" "
main=tk.Tk()
main.geometry("450x270")
main.resizable(0,0)

def data():
    global entry,v
    string= entry.get()
    v=string
    weather(v)
    
def weather(v):
    city=v
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_5)AppleWebKit/605.1.15 (KHTML, like Gecko)Version/12.1.1 Safari/605.1.15)'}
    res = requests.get(f'https://www.google.com/search?q=weather+{city}',headers=headers)
    soup=BeautifulSoup(res.content,'html.parser')
    l=soup.select('#wob_loc')[0].getText().strip()
    weather=soup.select('#wob_tm')[0].getText().strip()
    time=soup.select('#wob_dts')[0].getText().strip()
    st=soup.select('#wob_dc')[0].getText().strip()

    string = l
    lc.destroy()
    la.configure(text=string)

    unit="°C"
    string=weather+unit
    we.configure(text=string)

    sttt=st
    stt.configure(text=sttt)

    tim=time
    tame.configure(text=tim)
    
    dev_inf="Developer-Amitabh chaurasia version-0.1"
    dev.configure(text=dev_inf)

#main***********************    
entry=tk.Entry(main,width=40)
entry.focus_set()
entry.pack(pady=10)

b=tk.Button(main,text="SEARCH",command=data).pack()
lc=Label(main, text="Enter the location", font=("Courier 20 bold"))
lc.pack(pady=10)

la=Label(main, text=" ", font=("Courier 10 bold"))
la.pack(pady=15)

we=Label(main,text=" ",font=("Courier 15 bold"))
we.pack(pady=5)

stt=Label(main,text=" ",font=("Courier 10 "))
stt.pack(pady=3)

tame=Label(main,text=" ",font=("Courier 10 "))
tame.pack(pady=3)

dev=Label(main,text=" ",font=("Courier 12"))
dev.pack(pady=8)

main.mainloop()
