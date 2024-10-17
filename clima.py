from tkinter import*
import requests
import json

root = Tk()
root.geometry("600x600")
root.title("clima")


name = Label(root,text="nombre de la ciudad")

clima = Label(root)

humedad = Label(root)

entry_name = Entry(root)
 
name.place(relx=0.5,rely=0.15,anchor=CENTER)
clima.place(relx=0.5,rely=0.38,anchor=CENTER)
humedad.place(relx=0.5,rely=0.5,anchor=CENTER)
entry_name.place(relx=0.5,rely=0.35,anchor=CENTER)

def obtener_informacion():
    Api_information = requests.get("https://api.openweathermap.org/data/2.5/weather?q=" + entry_name.get() + "&appid=" + "21cab08deb7b27f4c2b55f3e2df28ea4") 

    json_almacenamiento = json.loads(Api_information.content)
    information_clima = json_almacenamiento['weather'][0]["main"]
    information_humedad = json_almacenamiento['main']["humidity"]
    print(information_clima)
    print(str(information_humedad) + "%")
    clima["text"] = "clima:" + str(information_clima) + "°"
    humedad["text"] =  "humedad:" + str(information_humedad) + "%"
    name["text"] = entry_name.get()
    
    entry_name.destroy()
    btn.destroy()
    



btn = Button(root,text="funcionar",command=obtener_informacion)
btn.place(relx=0.5,rely=0.70,anchor=CENTER)


root.mainloop()


