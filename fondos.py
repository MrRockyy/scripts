import os 
import random
path= '/home/camilo/Pictures/wallpapers'
contenido = os.listdir(path)
a=len(contenido)
print(a)
num=random.randint(0,a)
print(num)
os.system(f'feh --bg-scale /home/camilo/Pictures/wallpapers/"{contenido[num]}"')

