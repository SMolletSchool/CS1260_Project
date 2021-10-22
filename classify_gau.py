A= "Setosa"
B= "Versicolour"
C= "Virginica"
def classify(swidth,plength,pwidth):
    if pwidth <= 0.8:
        if __name__ == "__main__": print(A)
        return A
    else:
            if plength <= 4.95:
                if pwidth <= 1.65:
                    if __name__ == "__main__": print(B)
                    return B
                elif swidth <= 3.1:
                    if __name__ == "__main__": print(C)
                    return C
                else:
                    if __name__ == "__main__": print(B)
                    return B
            elif pwidth <=1.75:
                if pwidth <=1.65:
                    if __name__ == "__main__": print(C)
                    return C
                else:
                    if __name__ == "__main__": print(B)
                    return B
            else:
                if __name__ == "__main__": print(C)
                return C
                
if __name__ == "__main__":
    swidth=float(input("Enter the sepal width (cm): "))
    plength=float(input("Enter the petal length (cm): "))
    pwidth=float(input("Enter the petal width (cm): "))
    result=classify(swidth,plength,pwidth)
    print("The flower classification is "+result)