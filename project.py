A= "Setosa"
B= "Versicolour"
C= "Virginica"
def classify(swidth,plength,pwidth):
    if pwidth <= 0.8:
        print(A)
    else:
            if plength <= 4.95:
                if pwidth <= 1.65:
                    print(B)
                elif swidth <= 3.1:
                    print(C)
                else:
                    print(B)
            elif pwidth <=1.75:
                if pwidth <=1.65:
                    print(C)
                else:
                    print(B)
            else:
                print(C)
                
swidth=float(input("Enter the sepal width (cm): "))
plength=float(input("Enter the petal length (cm): "))
pwidth=float(input("Enter the petal width (cm): "))
result=classify(swidth,plength,pwidth)
print("The flower classification is "+result)