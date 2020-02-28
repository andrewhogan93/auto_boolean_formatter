def format(myString):
    myString = str.join(" ", myString.splitlines())
    lined =(myString.replace ('(', '\n' +'('))
    
    Line_number=0 
    Num_of_opens=0
    Total_num_of_opens=0
    Num_of_closes=0
    Total_num_of_closes=0
    Amount_of_tabs=0
    final_rule=""    
    for line in lined.split('\n'):
        Num_of_opens=line.count('(')
        Num_of_closes=line.count(')')
        Total_num_of_opens+=Num_of_opens
        Total_num_of_closes+=Num_of_closes
        Line_number+=1
        New_line=((Amount_of_tabs*"   ") + line)
        final_rule=(final_rule+ '\n' + New_line)
        Line_number+=1
        Amount_of_tabs=Total_num_of_opens-Total_num_of_closes
    return final_rule



from tkinter import *

def show_data():
    txt.delete(0.0, 'end')
    myString = ent.get()
    format(myString)
    
    sentence= str(format(myString))
    txt.insert(0.0, sentence)


root = Tk()
root.geometry("400x500")

l1 = Label(root, text = "Paste unformatted Code here: ")

ent = Entry(root)

l1.grid(row=0)
ent.grid(row=0, column=1)

btn = Button(root, text="Auto-Format", bg="purple", fg="white", command = show_data)
btn.grid(row=2, columnspan=2)

txt = Text(root, width=50, height=20, wrap=WORD)
txt.grid(row=3, columnspan=2, sticky=W)

root.mainloop()