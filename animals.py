class Dog:
  def speak(self):
    print('bark')
  
class Cat:
  def speak(self):
    print('meow')
  
if __name__ == '__main__':
  jack = Dog()
  jack.speak()
  
  tom = Cat()
  tom.speak()
