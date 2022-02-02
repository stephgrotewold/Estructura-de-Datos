import cProfile

def h():

    item_database = [
        {'item_id': 1701, 'item_name': 'Jack Daniels', 'precio': 150.99},
        {'item_id': 1702, 'item_name': 'RedBull', 'precio': 20.57},
        {'item_id': 1703, 'item_name': 'Jagermeister','precio': 230.00},
        {'item_id': 1704, 'item_name': 'Bailey', 'precio': 198.97},
        {'item_id': 1705, 'item_name': 'XL', 'precio': 100.00},
        {'item_id': 1706, 'item_name': 'Johnnie Walker','precio': 215.00},
        {'item_id': 1707, 'item_name': 'Gallo', 'precio': 6.00},
        {'item_id': 1708, 'item_name': 'Corona', 'precio': 7.45},
        {'item_id': 1709, 'item_name': 'Bicardi','precio': 199.00},
        {'item_id': 1710, 'item_name': 'San Miguel','precio': 205.99},
        {'item_id': 1711, 'item_name': 'Smirnoff','precio': 110.00},
    ]


    print('\nMenu:')
    print('1. Ver catalogo')
    print('2. Ingresar item de compra')
    print('3. Ingresar pago')
    print('4. Mostrar total del recibo de compra')
    print('5. Mostrar total de pagos realizados')
    print('6. Calcular el saldo pendiente a pagar')
    print('7. Calcular promedio de precio por item')
    print('8. Mostrar el precio del producto mas caro')
    print('9. Mostrar el recibo de compra con los pagos ingresados')
    print('10. Eliminar pagos 2 y 4')
    print('11. Salir\n')


    compra =[]
    pagos = []
    items_count = 0
    pagos_count = 0
    x = 0
    precio_Total = 0
    counter = 0 
    counter2 = 0 
    counter3 =0
    average = 0
    pago = 0 
    max = 0

    def get_item_by_item_id(pid, db):
        for item in db:
            if item['item_id'] == pid:
                return item

    while x !=10: 
        x = int(input('Ingrese su opcion:\n'))

        if x==1:
            print(item_database)
        
        if x==2:

            item_Comprado = int(input('Ingrese el item id:\n'))
            if (item_Comprado >1700 and item_Comprado < 1712):
                temp = get_item_by_item_id(item_Comprado,item_database) 
                precio = temp['precio']
                precio_Total += precio
                counter +=1
                compra.append(temp) 
                if precio > max:
                    max = precio
                print("Producto añadido a su recibo.\n")    
            
            else:
                print("error")

        
        if x==3:
            pago = float(input("Ingrese su pago: \n"))
            pagos.append(pago)
            counter2 += pago

        if counter2 == precio_Total:
            print("Deuda Pagada.")

        if counter2 > precio_Total:
            deuda = precio_Total - counter2
            float4 = deuda * -1
            format_float4 = "{:.2f}".format(float4)
            print("Pago Realizado, su cambio es de Q.",format_float4)

        
        if x==4:
            print("Su recibo es:",compra) 
            float = precio_Total
            format_float = "{:.2f}".format(float)
            print("Su Total del recibo de compra es: Q.", format_float)
        
        if x==5:
            print("Los pagos recibidos son:",pagos)

        
        if x==6:
            pago2 = precio_Total - counter2
            float3 = pago2
            format_float3 = "{:.2f}".format(float3)
            print("Su deuda restante es de:", format_float3)
        

        if x==7:
            average = precio_Total/counter
            float2 = average
            format_float2 = "{:.2f}".format(float2)
            print('El promedio del precio de sus items es: de Q.',format_float2)
            print('\n')
        
        
        if x==8:
            print("Su precio maximo es de Q.", max)
            
            
        if x==9:
            print("Su carrito consiste de:", compra)
        
            float = precio_Total
            format_float = "{:.2f}".format(float)
            print("Su deuda es de: Q.", format_float)

            for i in pagos:
                counter3 +=i
            
            float5 = counter3
            format_float5 = "{:.2f}".format(float5)
            print("Su pago es de: Q.",format_float5)

            deuda = precio_Total - counter2
            float4 = deuda * -1
            format_float4 = "{:.2f}".format(float4)
            print("Su cambio es de Q.",format_float4)
        
        if x==10:
        
            index = 1
            index2 = 3
            pagos.pop(index)
            pagos.pop(index2)
            print('Sus pagos 2 y 4 han sido eliminados correctamente.\n')
                
        
        if x == 11:
            x == 12

        if x > 12:
            print('Opcion No valida')
            print('\n')

cProfile.run('h()')