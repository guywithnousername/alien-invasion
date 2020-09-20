class Equation:
  def do_it(self):
    while True:
      global inputtedx
      try:
       inputtedx = input('Enter x:(enter q at any time to quit)')
       x= float(inputtedx)
       result = (5*x)+1
       while True:
         if result>500:
            print(result)
            break
         else:
          x=result
          result = (5*x)+1
      except:
        if inputtedx.lower() == 'q' or inputtedx.lower() == 'quit':
          break
      
  def do_it_manually(self,inputtedx):
   X = float(inputtedx)
   result = (5*X)+1
   while True:
     if result > 500:
       return result
       break
     else:
       x=result
       result = (5*x)+1
equation = Equation()
