import tkinter as tk
import string


def check_password():
    password = txt.get()
   

    upper_case = any([1 if i in string.ascii_uppercase else 0 for i in password])
    lower_case = any([1 if i in string.ascii_lowercase else 0 for i in password])
    special = any([1 if i in string.punctuation else 0 for i in password])
    digits = any([1 if i in string.digits else 0 for i in password])
    length = len(password)

    if length >= 10:
        length = True
    else:
        length = False

    characters = [upper_case, lower_case, special, digits, length]

    score = 0

    for i in range(len(characters)):
        if characters[i]:
            score += 1
    if score == 1:
       strength =('That\'s a very bad password.')
           
    elif score == 2:
       strength =('That\'s a weak password.')
           
    elif score == 3:
       strength =('Your password is okay, but it can be improved.')
    elif score == 4:
       strength =('Your password is hard to guess.')
       
    elif score == 5:
      strength =('Now that\'s one of a strong password!!!')
     
   
    result.config(text=strength)


window = tk.Tk()

window.eval('tk::PlaceWindow . center')

window.title('Password Checker')
window.geometry('350x100')

label = tk.Label(window, text='Enter the password:', font=('Arial Bold', 10))
label.grid(column=0, row=0)

txt = tk.Entry(window, width=20)
txt.grid(column=1, row=0)

button = tk.Button(window, text='Check password', command=check_password)
button.grid(column=2, row=0)

result = tk.Label(window, text='', font=('Arial Bold', 10))
result.grid(column=0, row=2, columnspan=3)

window.mainloop()