i=0
maxn =0
while(i<10):
    num = input('ingrese un numero')
    if int(num)%2!=0:
        print('este es el num ',num)
        if int(num)>maxn:
            maxn=int(num)
    elif maxn==0:
        print('no hay impares')
    else:
        print('el Maximo impar es ',maxn)
    i=i+1



