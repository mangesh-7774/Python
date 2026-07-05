class Average:
  def data(self,total_petrol,dist):
    self.total_petrol = total_petrol
    self.dist=dist

  def avg(self):
    return self.total_petrol//self.dist


obj1 = Average()
obj1.data(60,10)
print(f"Average is : {obj1.avg()} km/ltr")