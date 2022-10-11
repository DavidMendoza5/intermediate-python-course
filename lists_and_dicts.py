def run():
  # Creación de una lista
  my_list = [1, "Hello", True, 4.5]
  
  # Creación de un diccionario
  my_dictionay = {
    "firstname": "David",
    "lastname": "Mendoza"
  }

  super_list = [
    {
      "firstname": "David",
      "lastname": "Mendoza"
    },
    {
      "firstname": "Sara",
      "lastname": "Reyes"
    },
    {
      "firstname": "Bryan",
      "lastname": "Mendoza"
    },
    {
      "firstname": "Marcos",
      "lastname": "Pérez"
    }
  ]

  super_dict = {
    "natural_nums": [1,2,3,4,5],
    "integer_nums": [-1,-2,0,1,2],
    "floating_nums": [1.1,4.5,6.43]
  }

  # El método items() permite recorrer la llave y el valor de un diccionario
  for key, value in super_dict.items():
    print(key, " - ", value)

  for value in super_list:
    print(value)

def calculate_square():
  squares = []
  for i in range(1, 101):
    squares.append(i**2)
  print(squares)

def calculate_square_not_divisible_by_three():
  # squares = []
  # for i in range(1, 101):
  #   if i % 3 != 0: 
  #     squares.append(i**2)
  # print(squares)


  # comprehensions list
  squares = [i**2 for i in range(1,101) if i % 3 != 0]
  print(squares)

def dict_comprehensions():
  # my_dict = {}

  # for i in range(1,101):
  #   my_dict[i] = i**3
  
  my_dict = {i: i**3 for i in range(1,101) if i % 3 != 0}
  
  print (my_dict)

if __name__ == '__main__':
  dict_comprehensions()