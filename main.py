#*******Series Solver****************************
#solves
#multiplication series, common difference series
#exponential series
#alternate multiplication series/common diff/exponential
#fibonacci
#perfect squares
#perfect cubes
while True:
    import math
    print('NOTE')
    print('Program can solve following series\nmultiplication,exponential,alternate multiplication\nalternate exponential,fibonacci,perfect squares ,perfect cubes')
    print('Make sure the length of the series you\'re entering is atleast 6')
    print('*****************************************************************')
    x = list()
    d = 0
    s = 0
    m = 1
    d1 = 1
    n = int(input("Length of series: "))
    for i in range(n):
        i = int(input())
        x.append(i)


    #multiplication
    if x[1] - x[0] == x[2] - x[1] and x[2] - x[1] == x[3] - x[2] and x[3] - x[2] == x[4] - x[3]:
        cd = x[1] - x[0]
        print('Series has common difference: ', cd)    
        print('Enter how many numbers to append: ')
        n1 = int(input())
        e = x[n-1]
        for i in range(n1):
            j = e + cd
            e = j
            x.append(j)
        print(x)              
        ch = input('Achieved result? y/n')
        if ch == 'y' or ch == 'Y':
            break
        else:
            continue

    #exponential
    if len(x)>3:
        if x[0]*x[0] == x[1] and x[1]*x[0] == x[2] and x[2]*x[0] == x[3]:
            cm = x[0]
            print('Series has common multiple: ', cm)
            print('Series is exponential')
            print('Enter how many numbers to append: ')
            n1 = int(input())
            e = x[n-1]
            for i in range(n1):
                j = e*x[0]
                e = j
                x.append(j)
            print(x)              
            ch = input('Achieved result? y/n')
            if ch == 'y' or ch == 'Y':
                break
            else:
                continue

    #multiplication alternate
    if len(x)>=6:
        if x[2] - x[0] == x[4] - x[2] and x[3] - x[1] == x[5] - x[3]:
            cd1 = x[2] - x[0]
            cd2 = x[3] - x[1]
            print('Series is alternate multiplication and has 2 common differences: ')
            print(f'odd pos: {cd2}, even pos: {cd1}')
            print('Enter how many numbers to append: ')
            n1 = int(input())
            e = x[n-1]
            e1 = x[n-2]
            if n%2 == 0:
                for i in range(n1):
                    if i%2==0:
                        j = e1 + cd1
                        e1 = j
                        x.append(j)
                    else:
                        j = e + cd2
                        e = j
                        x.append(j)
            if n%2 != 0:
                for i in range(n1):
                    if i%2==0:
                        j = e1 + cd2
                        e1 = j
                        x.append(j)
                    else:
                        j = e + cd1
                        e = j
                        x.append(j)
            print(x)              
            ch = input('Achieved result? y/n')
            if ch == 'y' or ch == 'Y':
                break
            else:
                continue

        #exponential alternate
        if x[0]*x[0] == x[2] and x[2]*x[0] == x[4] and x[1]*x[1] == x[3] and x[3]*x[1] == x[5]:
            cm1 = x[0]
            cm2 = x[1]
            print('Series is alternate exponential:')
            print(f'Seires has 2 common multiples: odd pos: {cm2} and even pos: {cm1}')
            print('Enter how many numbers to append: ')
            n1 = int(input())
            e = x[n-1]
            e1 = x[n-2]
            if n%2 == 0:
                for i in range(n1):
                    if i%2==0:
                        j = e1*x[0]
                        e1 = j
                        x.append(j)
                    else:
                        j = e*x[1]
                        e = j
                        x.append(j)
            if n%2 != 0:
                for i in range(n1):
                    if i%2==0:
                        j = e1*x[1]
                        e1 = j
                        x.append(j)
                    else:
                        j = e*x[0]
                        e = j
                        x.append(j)
            print(x)              
            ch = input('Achieved result? y/n')
            if ch == 'y' or ch == 'Y':
                break
            else:
                continue

        #fibonacci
        if x[0] + x[1] == x[2] and x[1] + x[2] == x[3] and x[2] + x[3] == x[4]:
            print('Series is a fibonacci series')
            print('Enter how many numbers to append: ')
            n1 = int(input())
            e = x[n-1]
            e1 = x[n-2]
            for i in range(n1):
                j = e + e1
                e1 = e
                e = j
                x.append(j)
            print(x)              
            ch = input('Achieved result? y/n')
            if ch == 'y' or ch == 'Y':
                break
            else:
                continue

        #perfect squares
        if math.sqrt(x[0]).is_integer() and math.sqrt(x[1]).is_integer() and math.sqrt(x[2]).is_integer():
            root = list()
            print('Series is of perfect squares.') 
            for i in range(len(x)):
                j = int(math.sqrt(x[i]))
                root.append(j)
            if root[1] - root[0] == root[2] - root[1] and root[2] - root[1] == root [3] - root[2]:
                cd = root[1] - root[0]
                print(f'series has a common difference of {cd}')
            print('Enter how many numbers to append: ')
            n1 = int(input())
            e = int(math.sqrt(x[n-1]))
            for i in range(n1):
                j = e + cd
                j1 = j*j
                x.append(j1)
                e = j
            print(x)              
            ch = input('Achieved result? y/n')
            if ch == 'y' or ch == 'Y':
                break
            else:
                continue 

        #perfect cubes
        if x[0]**(1/3).is_integer() and x[1]**(1/3).is_integer() and x[2]**(1/3).is_integer():
            cuberoot = list()
            print('Series is of perfect cubes')
            for i in range(len(x)):
                j = round((x[i]**(1. /3)))
                cuberoot.append(int(j))    
            if cuberoot[1] - cuberoot[0] == cuberoot[2] - cuberoot[1] and cuberoot[2] - cuberoot[1] == cuberoot[3] - cuberoot[2]:
                cd = cuberoot[1]-cuberoot[0]
                print(f'series has common difference of {cd}')  
            print('Enter how many numbers to append: ')
            n1 = int(input())
            e = x[n-1]**(1/3)  
            for i in range(n1):
                j = e+cd
                j1 = round(j*j*j)
                x.append(j1)
                e = j
            print(x)             
            ch = input('Achieved result? y/n')
            if ch == 'y' or ch == 'Y':
                break
            else:
                continue  
        

        "# python"
