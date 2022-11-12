
import numpy as np
bank = 150
outcomes = []

for play in range(150):
  comeout_roll = np.random.randint(low = 2, high = 13)
  outcome = ''
  rolls = []
  rolls.append(comeout_roll)
  if comeout_roll  == 7 or comeout_roll == 11:
    outcome = "win"
    
  
  elif comeout_roll == 2 or comeout_roll == 3 or comeout_roll == 12:
  
    outcome = "lose"
  
  
  else :
    point = comeout_roll
    secondroll = 0
  
    while(secondroll != 7 and secondroll != point) :
      secondroll = np.random.randint(low = 2, high = 13)
      rolls.append(secondroll)
      if point == secondroll:
        outcome = "win"
      elif secondroll == 7 :
        outcome = "lose"
      else: 
        outcome = "tie"
      
  print(f"The outcome is {outcome} and the comeout roll number is {comeout_roll}")
  print(f"The list of outcome rolls is {rolls}")
  outcomes.append(outcome)
  if outcome == "win":
    bank = bank + 1
  else:
    bank = bank - 1
print(f"The remaining bank balance is {bank}")
net_loss = 150 - bank
print(f"The house advantage is {net_loss/150}")