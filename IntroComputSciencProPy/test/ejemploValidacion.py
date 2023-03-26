while True:
    val = input('Enter a integer:')
    try:
        val =int(val)
        print('Has ingresaod un entero: ',val)
        break#to exit the while loop
    except ValueError:
        print(val, 'it is not a integer')
