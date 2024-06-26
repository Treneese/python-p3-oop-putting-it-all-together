#!/usr/bin/env python3




class Shoe:
    def __init__(self, brand, size):
        self.brand =brand
        self.size = size

    def get_brand(self):
        return self._brand
    
    def set_brand(self, new_brand):
        if isinstance(new_brand, str):
            self._brand = new_brand
        else:
            raise TypeError('Brand must be of type str')
    brand = property(get_brand, set_brand)

    def get_size(self):
        return self._size
    
    def set_size(self,new_size):
        if isinstance(new_size,int):
            self._size = new_size
        else:
            print("size must be an integer")
    size = property(get_size, set_size)

    def cobble(self):
        self.condition = "New"
        print("Your shoe is as good as new!")
    

