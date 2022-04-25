'''class Square:
   def __init__(self):
     self.height = 2
     self.width = 2
   def set_side(self, new_side):
     self.height = new_side
     self.width = new_side'''

'''square = Square()
square.height = 3''' # not a square anymore

# "_" a esquerda significa que esses dados nao devem ser tocados mas ainda podem ser modificados...Sao protegidos.
'''class Square:
    def __init__(self):
      self._height = 2
      self._width = 2
      
    def set_side(new_side):
      self._height = new_side
      self._width = new_side

square = Square()
square._height = 3''' # not a square anymore

# dados privados com "__".
'''class Square:
    def __init__(self):
      self.__height = 2
      self.__width = 2
    def set_side(new_side):
      self.__height = new_side
      self.__width = new_side

square = Square()
square.__height = 3''' # raises AttributeError

#getters e setters
'''class Square:
    def __init__(self):
      self.__height = 2
      self.__width = 2
    def set_side(self, new_side):
      self.__height = new_side
      self.__width = new_side
    def get_height(self):
      return self.__height
    def set_height(self, h):
      if h >= 0:
        self.__height = h
      else:
        raise Exception("value needs to be 0 or larger")

square = Square()
square.__height = 3 '''# raises AttributeError