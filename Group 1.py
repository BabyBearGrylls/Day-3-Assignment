print("You are enough everyday.")
print("Let's see if finishing a day of class is possible for you today.")
status = input("Do you feel like you can complete a day of the class today? Y or N ")
if status == "Y":
  print("Good for you! Finish the day and cross the day off on your calendar.")
else:
  reason = input("Is it because you don't have TIME, lack MOTIVATION, or are UNSURE if you want to complete this course? Type one of the uppercase options.")
  if reason == "TIME":
    print("If you don't have time now, that's ok. Pick a date when you can come back, set a reminder, and check back then.")
  elif reason == "MOTIVATION":
    print("Talk to an organizer to see how you can get support. We're here to help!")
  elif reason == "UNSURE":
    maybe = input("Can you commit to completing 10 days? Y or N ")
    if maybe == "Y":
      print("See if you're in a better place to make a decision then.")
    else:
      commit = input("Can you commit to completing 5 days? Y or N ")
      if commit == "Y":
        print ("See if you're in a better place to make a decision then.")
      else:
        print("The reason you don't feel like you can complete a day is valid. I also think it would be hard to invest time in something I wasn't sure about.")
