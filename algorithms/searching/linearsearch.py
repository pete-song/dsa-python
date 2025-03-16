class LinearSearch:
  def __init__(self):
    self.array = []

  def findIndex(self, item):
    if not self.array or len(self.array) == 0:
      return None

    print(item)
    for i in range(len(self.array)):
      if self.array[i] == item:
        return i

    return None

def test():
  ls = LinearSearch()
  ls.array = [1,2,3,4,5,6,7,8,9,10]

  assert ls.findIndex(8) == 7, "Did not find the item"
  assert ls.findIndex(20) == None, "Where did you find that"

  print("All tests passed")

if __name__ == "__main__":
  test()
