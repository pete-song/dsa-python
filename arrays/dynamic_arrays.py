# Implementation of a Dynamic Array

class DynamicArray:
  def __init__(self):
    self.array = [0] * 1
    self.count = 0
    self.size = 1

  def append(self, data):
    if self.size == self.count:
      self.double()
    self.array[self.count] = data
    self.count += 1

  def double(self):
    temp = [0] * (self.size * 2)

    for i in range(self.size):
      temp[i] = self.array[i]

    self.array = temp
    self.size *= 2

  def halve(self):
    if self.count > 0:
      temp = [0] * self.count
      for i in range(self.count):
        temp[i] = self.array[i]
      self.size = self.count
      self.array = temp

  def appendAt(self, index, data):
    if self.size == self.count:
      self.double()
    for i in range(self.count, index, -1):
      self.array[i] = self.array[i - 1]
    self.array[index] = data
    self.count += 1

  def pop(self):
    if self.count > 0:
      self.array[self.count - 1] = 0
      self.count -= 1

  def popAt(self, index):
    if self.count > 0:
      for i in range(index, self.count - 1):
        self.array[i] = self.array[i + 1]
      self.array[self.count - 1] = 0
      self.count -= 1

    if self.count == self.size // 2:
      self.halve()

def main():
  da = DynamicArray()
  for i in range(1, 11):
    da.append(i)

  def printArray():
    for i in range(da.count):
      print(str(da.array[i]) + " ", end="")
    print()

  print("Elements of the array:")
  printArray()

  print('da size', da.size)
  print('da count', da.count)
  print('da array', da.array)

  da.appendAt(5, 100)
  printArray()

  da.pop()
  printArray()

  da.popAt(2)
  printArray()
  print('da array', da.array)

  for i in range(10):
    da.append(i)

  print('da size', da.size)
  print('da count', da.count)
  print('da array', da.array)

if __name__ == "__main__":
  main()
