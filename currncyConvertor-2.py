from tkinter import *
from tkinter import ttk
import urllib.request
import json

request_url = urllib.request.urlopen("https://free.currconv.com/api/v7/countries?apiKey=92139c44c58c2a36a2d3")
data=json.loads(request_url.read())

s=[]
for i in data["results"]:
    s.append(data["results"][i]["currencyId"])

s=sorted(list(set(s)))

def callbackFunc(event):
    global var_to,var_frome
    if var_frome.get()!="" and var_to.get()!="":
        try:
            web_url = urllib.request.urlopen(f"https://free.currconv.com/api/v7/convert?q={var_frome.get()}_{var_to.get()}&compact=ultra&apiKey=92139c44c58c2a36a2d3")
            data = json.loads(web_url.read())
            amount=data[f"{var_frome.get()}_{var_to.get()}"] * from_amount.get()
            to_amount.set(amount)
        except Exception as e:
            print(str(e))
root=Tk()
root.title("Currency Convertor")
root.geometry("350x400")


var_frome=StringVar()
from_name=ttk.Combobox(root,textvariable=var_frome)
from_name["values"]=s
from_name.grid(row=0,column=0,padx=30,pady=30)
from_name.bind("<<ComboboxSelected>>", callbackFunc)

from_amount=DoubleVar()
from_entry=Entry(root,textvariable=from_amount)
from_entry.grid(row=0,column=2,padx=30,pady=30)

var_to=StringVar()
to_name=ttk.Combobox(root,textvariable=var_to)
to_name["values"]=s
to_name.grid(row=1,column=0,padx=30,pady=30)
to_name.bind("<<ComboboxSelected>>", callbackFunc)


to_amount=DoubleVar()
to_entry=Label(root,textvariable=to_amount)
to_entry.grid(row=1,column=2,padx=30,pady=30)

root.mainloop()