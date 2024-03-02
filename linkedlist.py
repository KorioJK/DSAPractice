class LinkedList:
    def __init__(self,head):
        self.head = head

    def insert_first(self,node):
        node.next = self.head
        self.head = node
        
    
    def insert_last(self,node):
        if not self.head:  
            self.head = node
            return

        current_node = self.head
        while current_node.next:
            current_node = current_node.next

       
        current_node.next = node
    
    def remove_first(self):
        if self.head:
            self.head = self.head.next
        else:
            print("Linked list is empty, cannot remove first node.")

    def remove_last(self):
        if self.head:
            if not self.head.next:
                self.head = None
                return
            current_node = self.head
            previous_node = None
            
            while current_node.next:
                previous_node=current_node
                current_node = current_node.next

            previous_node.next = None
        else:
            print("Linked list is empty, cannot remove last node.")

    def contains(self, value):
        if not self.head:
            print("Linked list is empty.")
            return False

        current_node = self.head
        while current_node:
            if current_node.data == value:
                return True
            current_node = current_node.next

        return False

        
    def index_of(self, value):
        if not self.head:
            print("Linked list is empty.")
            return -1
        
        current_node = self.head
        count = 0

        while current_node:   
            if current_node.data == value:
                return count    
            count += 1
            current_node= current_node.next
            
        
        return -1
    

    def print(self):
        listItems = []
        if not self.head:
            print(listItems)
            return
        current_node = self.head
        while current_node:
            listItems.append(current_node.data)
            current_node = current_node.next
        print(listItems)
        


            
        
        

            
    


        
