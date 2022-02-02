print('\nMenu:')
print('1. Ingresar debitos')
print('2. Ingresar creditos')
print('3. Calcular el total de debitos')
print('4. Calcular el total de creditos')
print('5. Calcular el saldo')
print('6. Calcular promedio de debitos')
print('7. Mostrar el monto mayor de debitos')
print('8. Conteo de operaciones de credito y debito')
print('9. Mostrar los debitos y creditos')
print('10. Eliminar creditos')
print('11. Salir\n')

debits =[]
credits = []
credit_count=0
debit_count=0
x=0

while x !=11:
    x = int(input('Ingrese su opcion:\n'))

    if x==1:
        debits.append(int(input('Ingrese un debito:\n')))
        debit_count +=1
    
    if x==2:
        credits.append(int(input('Ingrese un credito:\n')))
        credit_count +=1
    
    if x==3:
        counter = 0 
        for i in debits:
            counter +=i
        print('El Total de debitos es:', counter)
        print('\n')
    
    if x==4:
        counter = 0 
        for i in credits:
            counter +=i
        print('El Total de creditos es:',counter)
        print('\n')
    
    if x==5:
        counter = 0 
        for i in credits:
            counter +=i
        for i in debits:
            counter -=1
        print('Su saldo total es de:',counter)
        print('\n')
    
    if x==6:
        counter = 0 
        j = 0
        for i in debits:
            counter +=i
            j +=1
            average = counter/j
        print('El promedio de sus debitos es:',average)
        print('\n')
    
    if x==7:
        counter = 0 
        for i in debits:
            if i > counter:
                counter = i
        print('El monto mayor de debitos es:',counter)
        print('\n')

    if x==8:
        print('El Conteo de debitos es de:', debit_count)
        print('El Conteo de creditos es de:', credit_count)
        print('\n')
    
    if x==9:
        print('Debitos:')
        for i in debits:
            print('*',i)
        print('Creditos:')
        for i in credits:
            print('*',i)
        print('\n')
    
    if x==10:
        credits.clear()
        print('Sus creditos han sido eliminados correctamente\n')
    
    if x==11:
        x == 12

    if x > 11:
        print('Opcion No valida')
        print('\n')
    