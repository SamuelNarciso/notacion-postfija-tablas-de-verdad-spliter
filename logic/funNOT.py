class FunNOT:
  def __init__(self):
      self.tablaNueva=[]
  
  
  def funcion(self,tabla1):
    self.tablaNueva = []
    for value in tabla1:
      self.tablaNueva.append(not(value))
    return self.tablaNueva