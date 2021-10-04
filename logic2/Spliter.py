
def spliter ( input='1 2 b s3 c 4 d++ 5 e' ):
  print('Input: ',input)
  strings, chars , numbers = [],[],[]
  splitted = input.split()
  def isaNumber(value):
    try:
      value = float(value)
      return True
    except:
      return False

  for value in splitted:
    number = isaNumber(value)

    if( not(number) ):
      if len(value)>=2:
            strings.append(value)  
      else: 
        chars.append(value)
    else:
      numbers.append(value)

  print(len(numbers), 'Numbers',numbers)
  print(len(chars), 'chars',chars)
  print(len(strings), 'strings',strings) 

# spliter( )