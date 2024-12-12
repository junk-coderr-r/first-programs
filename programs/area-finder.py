# for finding area, was in my math class and bored
x = int(input("What shape is this? Parallelogram(1), Rhombus/kite(2), or a triangle(3)?"))

if x==1:
    def parallelogram():
        base = float(input("What is the base measurement?"))
        height = float(input("What is the height?"))
        area = base * height
        print(area)
        exit()
    parallelogram()

if x==2:
    def Rhombus():
        distance_1 = float(input("What is the first distance measurement?"))
        distance_2 = float(input("What is the second distance measurement?"))
        mult = int(input("Does the distance need to be multiplied by 2, Yes(1) or No(2)"))
        if mult==1:
            distance_1 *= 2
            distance_2 *= 2
        multiplied = distance_1*distance_2
        multiplied/=2
        print(multiplied)
        exit()
    Rhombus()

if x==3:
    def parallelogram():
        base = float(input("What is the base measurement?"))
        height = float(input("What is the height?"))
        area = base * height
        area/=2
        print(area)
        exit()
    parallelogram()

if x>3 or x <= 0:
        print("Invalid input, please retry.")
        exit()
