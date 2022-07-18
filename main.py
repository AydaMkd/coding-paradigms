class Podracer:
      def __init__(self, max_speed, condition, price):
       self.max_speed = max_speed
       self.condition = condition
       self.price = price

       def repair(self):
        self.condition = "repaired"
    

class AnakinsPod(Podracer):
  def __init__(self, max_speed, condition, price):
    super.init(max_speed, condition, price)
  
def boost(self):
    self.max_speed *= 2

class SebulbasPod(Podracer):
  def __init__(self, max_speed, condition, price):
    super.init(max_speed, condition, price)
  
  def flame_jet(self,other):
    other.condition = "trashed"
    
#1- no it does not it returns the same data in the array
#2- yes it returns the same result when the same argument is passed
#3- yes because it takes a function as an argument
#4- I would choose this solution since because it provides the benefits of oop which makes my code resuable and clearer to understand. 
#5 the flexibility and modularity makes it solving this problem more methodic and easier to troubleshoot issues.