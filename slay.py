while True:
  total = 0
  custom_Name = input("what's your bank details (not scam i swear) - ")
  
  while True:
    quantity = int(input("how many items are you buying ?? - "))
    items = int(input("guess your total price (whole number only tank yu) - "))
    total = quantity*items
    repeat = input("do you want to add more items(y/n only uwu)")
    
    if repeat=='n' or repeat=='N':
      break
    
    print("_"*50)
    print("your name is: ", custom_Name)
    print("total money you wasted today: ", total)
    print()
    print("*****thanks for letting me get your money uwuwuwuwuuw****")
    print("_"*50)
    
    new_customer = input("are you done bruh(y/n)")
    
    if new_customer=='n' or new_customer=='N':
      break
