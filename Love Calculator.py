while True:
  name_1 = input("What is your name?\n")
  name_2 = input("What is their name?\n")
  print("\n")
  print("The Love Calculator is calculating your score...")
  import time
  time.sleep(1.5)
  combined_names = name_1 + name_2
  lower_names = combined_names.lower()
  t = lower_names.count("t")
  r = lower_names.count("r")
  u = lower_names.count("u")
  e = lower_names.count("e")
  first_dig = t + r + u + e

  l = lower_names.count("l")
  o = lower_names.count("o")
  v = lower_names.count("v")
  e = lower_names.count("e")
  second_dig = l + o + v + e

  love_score = int(str(first_dig) + str(second_dig))
  if love_score < 10 or love_score > 90:
    print(f"Your score is {love_score}, you go together like coke and mentos.")
  elif love_score >= 40 and love_score <= 50:
    print(f"Your score is {love_score}, you are alright together.")
  else:
    print(f"Your score is {love_score}.")
  print("\n")
  try_again = input("Would you like to try again? (Y or N)\n")
  if try_again == "Y" or try_again == "y":
    continue
  else: 
    print("Bye! Have a nice day!")
    break
    
  