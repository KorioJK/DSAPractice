from arrays import CustomArray
from data.node import  Node
from linkedlist import LinkedList
def main():
   linkedList()


def linkedList():
    node1 = Node(1)
    node2 = Node("Node2")
    node3 = Node([1,2,3])
    node4 = Node(3)
    node5 = Node(2)

    node1.next=node2
    node2.next=node3
    node3.next=node4
    node4.next=node5

    lList = LinkedList(node1)
    lList.print()
    lList.remove_first()
    lList.print()
    lList.insert_first(Node("First"))
    lList.print()
    lList.insert_last(Node("Last"))
    lList.print()
    print(lList.contains("First"))
    lList.remove_first()
    lList.print()
    print(lList.contains("First"))
    print(lList.index_of("First"))
    print(lList.index_of("Last"))


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