from tkinter import Canvas, Frame, Button, ttk, Tk, END, simpledialog, CENTER, Toplevel, Checkbutton
from tkcalendar import DateEntry
from DataBaseHandler import DataBaseHandler

class AppGui:

    def __init__(self):
        self.master = Tk()

        canvas = Canvas(self.master, height=800, width=500, background='grey65')
        canvas.pack()

        self.createFrames()

        self.master.mainloop()

    def createFrames(self):
        self.createNotesTable()
        self.createAddTaskButton()
        self.createDeleteButton()
        self.createSaveButton()

    def createAddTaskButton(self):
        def addTask():
            selectedDate = None

            def getSelectedDate():
                nonlocal selectedDate
                selectedDate = dateEntry.get_date()
                datePicker.destroy()

            datePicker = Toplevel(self.master)
            datePicker.title('Choose Date')
            datePicker.geometry('200x100')

            dateEntry = DateEntry(datePicker)
            dateEntry.pack(padx=10, pady=10)

            chooseButton = Button(datePicker, text='Choose', command=getSelectedDate)
            chooseButton.pack()
            datePicker.wait_window()

            task = simpledialog.askstring('Task', 'Task')

            if selectedDate != None and task != '':
                self.table.insert('', END, values=(selectedDate, task))




        addButtonFrame = Frame(self.master, background='snow')
        addButtonFrame.place(relx=0.06, rely=0.05, relwidth=0.2, relheight=0.03)
        addButton = Button(addButtonFrame, text='Add Task', command=addTask)
        addButton.pack(fill='both')

    def createDeleteButton(self):
        def delete():
            selectedItem = self.table.focus()
            if selectedItem:
                self.table.delete(selectedItem)
        
        deleteButtonFrame = Frame(self.master, background='snow')
        deleteButtonFrame.place(relx=0.32, rely=0.05, relwidth=0.2, relheight=0.03)
        deleteButton = Button(deleteButtonFrame, text='Delete', command=delete)
        deleteButton.pack(fill='both')

    def createSaveButton(self):
        def save():
            database = DataBaseHandler()
            database.clearTable()
            for item in self.table.get_children():
                date, task= self.table.item(item)['values']
                database.insertItem(date, task)
            database.closeConnection()

        saveButtonFrame = Frame(self.master, background='snow')
        saveButtonFrame.place(relx=0.74, rely=0.05, relwidth=0.2, relheight=0.03)
        saveButton = Button(saveButtonFrame, text='Save', command=save)
        saveButton.pack(fill='both')
    
    def createNotesTable(self):
        self.tableFrame = Frame(self.master, background='snow')
        self.tableFrame.place(relx=0.06, rely=0.1, relwidth=0.88, relheight=0.87)

        self.table = ttk.Treeview(self.tableFrame, height=1000, column=('date', 'task'), show='headings')
        self.table.pack(fill='x')

        self.table.column('# 1', anchor=CENTER, width=100)
        self.table.heading('# 1', text='Date')
        self.table.column('# 2', anchor=CENTER, width=300)
        self.table.heading('# 2', text='Task')

        database = DataBaseHandler()
        records = database.fetchAllItems()
        for record in records:
            self.table.insert('', END, values=record)
        database.closeConnection()