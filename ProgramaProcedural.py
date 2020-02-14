print ("Instituto Tecnologico Superior de Valladolid" + '\n'
    + "Programacion Logica y Funcional" + '\n'
    + "Paradigmas De Programacion " + '\n' + '\n'
    + "Paradigma de Programacion Procedural" );
print ("Calculadora Basica");
op = int (input ("Seleccione una operacion a realizar" '\n'
    +  "1.- Multuplicacion"'\n'
    +  "2.- Division"'\n'
    +  "3.- Suma"'\n'
    +  "4.- Resta" + '\n'
    +   "-------------- " + '\n' ));

if op is 1:
    print ("Multuplicacion");
    a = int (input ("Digite el primero numero " + '\n'));
    b = int (input ("Digite el segundo numero" + '\n'));

    print ("El resultado de la Multuplicacion es " + str(a*b));

elif op is 2:
    print ("Division");
    a = int (input ("Digite el primero< numero " + '\n'));
    b = int (input ("Digite el segundo numero" + '\n'));

    print ("El resultado de la Division es " + str(a/b));

elif op is 3: 
    print ("Suma");
    a = int (input ("Digite el primero numero " + '\n'));
    b = int (input ("Digite el segundo numero" + '\n'));

    print ("El resultado de la Suma es " + str(a+b));

elif op is 4:
    print ("Resta");
    a = int (input ("Digite el primero numero " + '\n'));
    b = int (input ("Digite el segundo numero" + '\n'));

    print ("El resultado de la Resta es " + str(a-b));
else:
    print ("No ha seleecionado ninguna operacion");
