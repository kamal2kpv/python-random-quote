def primarycode():
  #print("Keep it logically awesome.")
  
  f = open("quotes.txt","a")
  f.write("\nSpeak like a human !\n")
  f.write("Keep it Simple!\n")
  f.write("Simle like a King!")
  #msg = f.readlines()
  #print(msg)
  f.close()
  
  f = open("quotes.txt")
  quotes = f.readlines()
  
  i = len(quotes)
  j = i - 1
  k = i - 2
  #print(i)
  print ("Read Line: %s" % (quotes[k]).rsplit())
  print ("Read Line: %s" % (quotes[j]))

  #print(quotes[15])
  
  f.close()
  
if __name__== "__main__":
  primarycode()
  
