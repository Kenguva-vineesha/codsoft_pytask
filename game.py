rock='👊'
paper='✋'
scissor='✌'
game_emoji=[rock,paper,scissor]
import random
user_choice=int(input('enter your choice:[type 0 for rock,1 for paper,2 for scissor]:\n'))
print(f"\nyou choice is {game_emoji[user_choice]}")
if user_choice>=3 or user_choice<0:
	print('you entered invalid choice.\n')
else:
	# print(game_emoji[user_choice])
     computer_choice=random.randint(0,2)    
     print('computer choice: ',game_emoji[computer_choice])
     if computer_choice == user_choice:
          print('\nit is a draw.')
     elif computer_choice == 0 and user_choice == 2:
          print('\nyou lose.')
     elif computer_choice == 2 and user_choice == 1:
          print('\ncomputer win.')
     elif computer_choice > user_choice:
          print('\nyou lose.')
     elif computer_choice < user_choice:
          print('\nyou win')
		 










