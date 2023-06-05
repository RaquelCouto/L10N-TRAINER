from tkinter import *
from tkinter import ttk

root = Tk()
root.geometry("400x250")
root.title("L10n trainer")

stringPath = Label(root, text="Path to xml file: ")
campoStringPath = Entry(root,)

stringPath.grid(column=0, row=0)
campoStringPath.grid(column=1, row=0)
#loadButton.grid(column=2, row=0)

stringNumberoffaults = Label(root, text = "Number of random faults: ")
campoNumberofFaults = Entry(root,)

stringNumberoffaults.grid(column=0, row=1)
campoNumberofFaults.grid(column=1, row=1)


stringSelectLanguage = Label(root, text="Target Language for translation: ")
stringLanguages = StringVar()
dropButton = ttk.Combobox(root,textvariable= stringLanguages, values = ['Spanish', 'Hindi','Portuguese', 'French', 'Russian', 'Italian', 'Urdu','Japanese','Turkish', 'Chinese', 'German', 'Serbian','Arabic'])
stringSelectLanguage.grid(column=0, row=3)
dropButton.grid(column=1, row=3)

stringManualStrings = Label(root, text="Manually change strings values")
campoManuallyStrings = Entry(root,)
addButton = Button(root,text="Add")
stringManualStrings.grid(column=0, row=4)
campoManuallyStrings.grid(column=1, row=4)
addButton.grid(column=2, row=4)



listofManualStrings = Listbox(root,height=6, width=35,selectmode=EXTENDED)
deleteButton = Button(root, text="Delete")
listofManualStrings.grid(column=0, row=5)
deleteButton.grid(column=1, row=5)
#listofManualStrings.insert(1, "Error = Erro inesperado")
#listofManualStrings.insert(1, "Home = Página Inicial")
#listofManualStrings.insert(1, "Settings = Configurações do dispositivo")


loadButton = Button(root, text="Generate seeded faults")
loadButton.grid(column=0,row=6)


#dropButton['values'] = ['Spanish', 'Hindi','Portugues', 'French', 'Russian', 'Italian', 'Urdu','Japanese','Turkish', 'Chinese', 'German', 'Serbian','Arabic']








root.mainloop()