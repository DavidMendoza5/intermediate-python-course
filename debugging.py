def divisors(num):
  assert num > 0, "El número debe ser mayor a 0"
  divs = [div for div in range(1, num+1) if num % div == 0]
  return divs
  # try:
  #   if num <= 0:
  #     raise ValueError
  #   divs = [div for div in range(1, num+1) if num % div == 0]
  #   return divs
  # except ValueError as ve:
  #   print("El número debe ser mayor a 0")
  #   return ve


def run():
  try:
    num = int(input("Ingresa un número: "))
    print(divisors(num))
  except ValueError:
    print("El valor debe de ser un número")


if __name__ == '__main__':
  run()