print("Ingreses su nota numerica: ")
nota = int(input())

if nota>=76 and nota<=100:
    print("Su nota es: O")
elif nota>=60 and nota<75:
    print("Su nota es: A")
elif nota>=50 and nota<59:
    print("Su nota es: B")
elif nota>=40 and nota<49:
    print("Su nota es: C")
elif nota>=0 and nota<40:
    print("Su nota es: D")
else:
    print("Error! Ingrese una nota valida")