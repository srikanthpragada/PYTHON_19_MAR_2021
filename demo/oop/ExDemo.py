radius = input("Enter radius :")
try:
    r = int(radius)
    print(22 / 7 * r ** 2)
except Exception as ex:
    print(ex.__class__.__name__)
    print(ex)



print("The End!")