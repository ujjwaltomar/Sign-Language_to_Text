import tkinter as tk
import tkinter.messagebox
a=""

def button_click(index):
    global a
    a=a + button_texts[index]+" "
#    print(a)
    

    current_data = label.cget("text")
    updated_data = current_data + " " + button_texts[index]
    label.config(text=updated_data)
    
    with open('str.txt','w') as f:	
        f.write("")

root = tk.Tk()
root.geometry("500x400")  
root.title("Button GUI")
frame = tk.Frame(root, width=800, height=400)
frame.pack(side="top")  # Adjust the side parameter to your preference
button_texts = []


def print_first_seven_words(character):
    with open('dictionary.txt', 'r') as file:
        count = 0
        for line in file:
            word = line.strip()
            if word.startswith(character):
                button_texts.append(word)
                count += 1
                if count == 7:
                    break

def remove_last_word():
    current_text = label.cget("text")
    if current_text:
        words = current_text.split()
        modified_text = " ".join(words[:-1])
        label.config(text=modified_text)

# Create a button to remove the last word
button = tk.Button(root, text="Delete", command=remove_last_word)
button.pack()
button.config(font=('Ink Free',20,'bold'))
button.config(bg='#f23333')
button.pack(pady=30)



# Array of button texts
buttons = []

def update_button_texts():
    x = 'a'
    with open('str.txt', 'r') as f:
        x = f.read()
        #print(x)
        print_first_seven_words(x)

    for i in range(len(button_texts)):
        button = tk.Button(frame, text=button_texts[i], command=lambda index=i: button_click(index))
        button.pack(side="left")  # Arrange buttons horizontally
        buttons.append(button)
        button.config(font=('Ink Free',20,'bold'))
        button.config(bg='#95cccf')
        button.pack(padx=5)




    #print(button_texts)


# Update button texts initially
update_button_texts()

def dcpy():
    copiedLabel.config(text="")

def func():
    copiedLabel.pack()
    root.clipboard_clear()
    root.clipboard_append(a)
    label.config(text="Text=>")
    copiedLabel.config(text="Text Copied!!!")
    copiedLabel.pack()

    


# Function to update button texts periodically
cnter=0
def update_periodically():
    des()
    global cnter
    cnter=cnter+1
    if(cnter>3):
        dcpy()
        
        cnter=0
        #print(cnter)
    update_button_texts()
    root.after(1000, update_periodically)  # Update every 1 second (adjust as needed)

def des():
    for b in buttons:
        b.destroy()
    del button_texts[:]
 



label = tk.Label(root, text="Text => ",font=('aerial'))
label.config(fg='#14800a')
label.pack()

button = tk.Button(root, text="Copy", command=func)
button.pack()
button.config(font=('Ink Free',20,'bold'))
button.pack(pady=20)


copiedLabel= tk.Label(root, text="Text Copied !!!",font=('aerial'))
copiedLabel.config(fg='#14800a')

# Start updating button texts periodically
update_periodically()

root.mainloop()
