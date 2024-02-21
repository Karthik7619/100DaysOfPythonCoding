path=input("You have to choose a path either leftlef or right:").lower()
print(path)
if path == 'right':
  print("You have choose wrong path, you are dead")
elif path == "left":
  sw = input("Choose either swim or wait to cross jornery:").lower()
  print(sw)
  if sw == "swim":
    print("Attacked by trout.Game Over.")
  elif sw == "wait":
    door = input("Choose a door either red, blue or yellow:")
    if door == "red":
      print("Burned by fire.Game Over.")
    elif door == "blue":
      print("Eaten by beasts.Game Over.")
    elif door == "yellow":
      print("You Win!")
    else:
      print("Game Over.")
  else:
    print("Not Swim or Wait - Game Over.")
else:
  print("Not Left or Right - Game Over.")
