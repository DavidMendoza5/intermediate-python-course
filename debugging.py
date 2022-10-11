def divisors(num):
  divs = [div for div in range(1, num+1) if num % div == 0]
  return divs


def run():
  num = int(input("Ingresa un número: "))
  print(divisors(num))


if __name__ == '__main__':
  run()