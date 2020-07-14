"""The pass statement is a null operation; nothing happens when it executes. 
   The pass is also useful in places where your code will eventually go,
   but has not been written yet (e.g., in stubs for example):"""
for letter in 'Python': 
   if letter == 'h':
      pass
      print ('This is pass block')
   print ('Current Letter :', letter)

print ("Good bye!")