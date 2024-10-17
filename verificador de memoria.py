import matplotlib .pyplot as plt 
import psutil as p

list_aplication  = []

consumo_aplication = []

conteo_aplication  = 0

for process in p.process_iter():
    conteo_aplication = conteo_aplication + 1
    if  conteo_aplication <= 6:
        name = process.name()
        consumo_acess = p.cpu_percent()
        print('nombre:'+name+"consumo de la cpu"+str(consumo_acess))
        list_aplication.append(name)
        consumo_aplication.append(consumo_acess)

plt.figure(figsize=(15,7))
plt.xlabel("aplicaciones")
plt.ylabel("consumo de la cpu")
plt.bar(list_aplication,consumo_aplication,width=1,color=("red","blue","green","black","white","brown"))
plt.show()        