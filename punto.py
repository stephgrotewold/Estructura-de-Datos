class point:
    pass

p = point()
p.x = int(input("Ingrese la coordenada x: "))
p.y = int(input("Ingrese la coordenada y: "))

if((p.x>0) and (p.y>0)):
    print("El punto [",p.x, ",",p.y ,"] se encuentra en el primer cuadrante.")

elif((p.x<0) and(p.y>0)):
       print("El punto [",p.x, ",",p.y ,"] se encuentra en el segundo cuadrante.")

elif((p.x < 0) and(p.y < 0)):
       print("El punto [",p.x, ",",p.y ,"] se encuentra en el tercer cuadrante.")

elif((p.x > 0) and(p.y < 0)):
       print("El punto [",p.x, ",",p.y ,"] se encuentra en el cuarto cuadrante.")

else:
    print("El punto [",p.x, ",",p.y ,"] se encuentra en el origen.")




