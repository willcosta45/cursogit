def generaPares(limite):

    num=1

    while num<limite:

       yield num*4

       num=num+1

devuelvePares=generaPares(20)

    
print(next(devuelvePares))

print("Aqui podria ir mas codigo...")

print(next(devuelvePares))

print("Aqui podria ir mas codigo...")


print(next(devuelvePares))

print("Aqui podria ir mas codigo...")

print(next(devuelvePares))

print("Aqui podria ir mas codigo...")

print(next(devuelvePares))

