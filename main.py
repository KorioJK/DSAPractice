from arrays import CustomArray
def main():
   playWithArrays()




def playWithArrays():
    testArr = CustomArray(3)
    print("Original Array: ",testArr.array)
    testArr.insert(10)
    print("\nAfter inserting array becomes: ",testArr.array)
    testArr.insert(20)
    print("\nAfter inserting array becomes: ",testArr.array)
    testArr.insert(30)
    print("\nAfter inserting array becomes: ",testArr.array)
    testArr.insert(40)
    print("\nAfter inserting array becomes: ",testArr.array)
    testArr.insert(50)
    print("\nAfter inserting array becomes: ",testArr.array)    
    testArr.remove_at(0)
    print("\nAfter removing becomes: ",testArr.array)
    testArr.remove_at(3)
    print("\nAfter removing becomes: ",testArr.array)
    testArr.remove_at(1)
    print("\nAfter removing becomes: ",testArr.array)
    testArr.remove_at(10)
    print("\nAfter removing becomes: ",testArr.array)
    testArr.insert(50)
    print("\nAfter inserting array becomes: ",testArr.array) 
    testArr.remove_at(-10)
    print("\nAfter removing becomes: ",testArr.array)
    testArr.index_of(50)
    testArr.index_of(69)
    testArr.insert(60)
    print("\nAfter inserting array becomes: ",testArr.array) 
    testArr.index_of(60)

if __name__ == "__main__":
    main()