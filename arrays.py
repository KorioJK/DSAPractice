import array

class CustomArray:
    def __init__(self, size):
        self.array = array.array('i', [0] * size)
        self.count = 0
    def insert(self, item):
        if self.count >= len(self.array):
            new_array = array.array('i', [0] * (len(self.array) + 1))
        else:
            new_array = array.array('i', [0] * (len(self.array)))
        if self.count > 0:
            for i in range(self.count):
                new_array[i] = self.array[i]
        new_array[self.count] = item
        self.count += 1
        self.array = new_array

    def remove_at(self, index):
        if index >= len(self.array)  or index < 0:
            return self.array
        new_array = array.array('i', [0] * (len(self.array) - 1))
        for i in range(len(self.array)):
            if i < index:
                new_array[i] = self.array[i]
            elif i > index:
                new_array[i - 1] = self.array[i]
        self.array = new_array
        self.count -= 1
    
    def index_of(self,item):
        for i in range(len(self.array)):
            if  self.array[i] == item:
                print(i)
                return
        print(-1)

 
