class payment_gateway:
  def payment_process(self,obj):

    if hasattr(obj,"pay"):
      obj.pay()
    else:
      print("method not found")
      return

  