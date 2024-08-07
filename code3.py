"""
write a script that will ask user to enter yes or no as answer. 
If the user answer is not either yes or no, the script should keep asking for a valid entry.
And if the entry is Yes or No it sould display valid entry.
"""


user_answer=""
while True:
    if user_answer not in ['yes', 'no']:
        user_answer=input("Do you want COVID shot? please enter (yes or no): ").strip().lower()
    else:
        print("valid choice")
        break    


