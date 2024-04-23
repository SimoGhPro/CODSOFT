from tkinter import * 
from PIL import Image, ImageTk  #insert images
from tkinter import messagebox , ttk   #ttk:table for view contacts
from tkinter.simpledialog import askstring    #ask user to input something

#variables interface
label_font = ("times new roman", 40, "bold")
button_font = ("helvetica", 15, "bold")

########################### CONTACT APP CLASS ##############################
class Contact(Tk):
    def __init__(self, *args, **kwargs):
        Tk.__init__(self, *args, **kwargs)
        
        #list to store data contact
        self.__data = {}

        #Favicon and app title
        self.title("Contact Book")
        self.iconbitmap(r'images/contact.ico')

        #Insert Pages with initialized frame (Nothing to display yet)
        self.home_frame = Frame(self)
        self.add_frame = Frame(self)
        self.view_frame= Frame(self)
        self.delete_frame = Frame(self)
        self.search_frame = Frame(self)
        self.update_frame= Frame(self)
        
        #Call the main page: homepage
        self.show_home()


########### HOMEPAGE FUNCTIONS ###############
    #Insert the home frame page
    def show_home(self):
        self.search_frame.grid_remove()
        self.update_frame.grid_remove()
        self.view_frame.grid_remove()
        self.add_frame.grid_remove()
        self.home_frame.grid()
        self.homepage()

    #HomePage
    def homepage(self):
        self.title("Contact Book")
        first_label = Label(self.home_frame, text="Welcome to",font=label_font, bg="purple3", foreground="white")
        first_label.grid(row=0, column=1)
        second_label = Label(self.home_frame, text="Contact Book",font=label_font, bg="purple3", foreground="white")
        second_label.grid(row=0, column=2)

        #Load images
        self.add_image = Image.open("images/add.png")
        self.add_photo = ImageTk.PhotoImage(self.add_image)
        
        self.delete_image = Image.open("images/delete.png")
        self.delete_photo = ImageTk.PhotoImage(self.delete_image)
        
        self.search_image = Image.open("images/search.png")
        self.search_photo = ImageTk.PhotoImage(self.search_image)
        
        self.update_image = Image.open("images/update.png")
        self.update_photo = ImageTk.PhotoImage(self.update_image)
        
        self.view_image = Image.open("images/view.png")
        self.view_photo = ImageTk.PhotoImage(self.view_image)
        
        # Create labels
        self.add_pic = Label(self.home_frame, image=self.add_photo)
        self.add_pic.grid(row=2, column=1, padx=2, pady=2)
        
        self.delete_pic = Label(self.home_frame, image=self.delete_photo)
        self.delete_pic.grid(row=3, column=1, padx=2, pady=2)
        
        self.search_pic = Label(self.home_frame, image=self.search_photo)
        self.search_pic.grid(row=4, column=1, padx=2, pady=2)
        
        self.update_pic = Label(self.home_frame, image=self.update_photo)
        self.update_pic.grid(row=5, column=1, padx=2, pady=2)
        
        self.view_pic = Label(self.home_frame, image=self.view_photo)
        self.view_pic.grid(row=6,column=1, padx=2, pady=2)

        #Buttons
        add_button = Button(self.home_frame, text="Add Contact", font=button_font, bg="white", foreground="purple1", width=15, command=self.show_add_page)
        add_button.grid(row=2, column=2)
        delete_button = Button(self.home_frame, text="Delete Contact", font=button_font, bg="white", foreground="purple1", width=15, command=self.show_delete_page)
        delete_button.grid(row=3, column=2)
        search_button = Button(self.home_frame, text="Search Contact",font=button_font, bg="white", foreground="purple1", width=15, command=self.show_search_page)
        search_button.grid(row=4, column=2)
        update_button = Button(self.home_frame, text="Update Contact", font=button_font, bg="white", foreground="purple1", width=15, command=self.show_update_page)
        update_button.grid(row=5, column=2)
        view_button = Button(self.home_frame, text="View Contact", font=button_font, bg="white", foreground="purple1", width=15, command=self.show_view_page)
        view_button.grid(row=6, column=2)

   
########### VIEW CONTACT FUNCTIONS ###############
    #Insert the view frame page
    def show_view_page(self):
        self.home_frame.grid_remove()
        self.view_frame.grid()
        self.viewpage()

    #Display the table
    def view_contact(self , data) :
        columns = ('Name', 'Email', 'Phone Number', 'Adress' )
        tree = ttk.Treeview(self.view_frame, columns=columns, show='headings')
        tree.heading('Name', text='Name')
        tree.heading('Email', text='Email')
        tree.heading('Phone Number', text='Phone Number')
        tree.heading('Adress', text='Adress')
        tree.grid(row=0,column=0)
        for child_data in data:
            tree.insert("", "end", values=child_data)
        
        #Back to home
        back_button = Button(self.view_frame, text="Back to Home", font=button_font, bg="white", foreground="purple1", width=15, command=self.show_home)
        back_button.grid(row=6, column=0)

    #ViewPage
    def viewpage(self):
        self.title("View Contact Page")
        new_data = []
        for key, val in self.__data.items():
            new_data.append(val)
        self.view_contact(new_data)

########### ADD CONTACT FUNCTIONS ###############
    #Insert the add frame page
    def show_add_page(self):
        self.home_frame.grid_remove()
        self.add_frame.grid()
        self.addpage()

    #Add Contact Process
    def add_contact(self, name, email, phone_number, address):
        if name != "" and address != "" and phone_number != "" and email != "":
            if phone_number not in self.__data:
                self.__data[phone_number] = [name, email , phone_number, address]
                messagebox.showinfo("Success", "Added successfully")
            else:
                messagebox.showwarning("Warning", "Number already exists")
        else:
            messagebox.showerror("Error" , "Please enter all the values")

    #Add Contact Page 
    def addpage(self):
        self.title("Add Contact Page")
        Name = Label(self.add_frame, text="Name:")
        Name.grid(row=1, column=0)
        Name_input = Entry(self.add_frame)
        Name_input.grid(row=1, column=1)
        
        Email = Label(self.add_frame, text="Email:")
        Email.grid(row=2, column=0)
        Email_input = Entry(self.add_frame)
        Email_input.grid(row=2, column=1)

        Phone = Label(self.add_frame, text="Phone Number:")
        Phone.grid(row=3, column=0)
        Phone_input = Entry(self.add_frame)
        Phone_input.grid(row=3, column=1)

        Adress = Label(self.add_frame, text="Adress:")
        Adress.grid(row=4, column=0)
        Adress_input = Entry(self.add_frame)
        Adress_input.grid(row=4, column=1)

        #Call the Process
        add_button = Button(self.add_frame, text="ADD", font=button_font, bg="white", foreground="purple1", width=15, command=lambda: self.add_contact(Name_input.get(),Email_input.get(),Phone_input.get(),Adress_input.get()))
        add_button.grid(row=5, column=1)

        #Back to home
        back_button = Button(self.add_frame, text="Back to Home", font=button_font, bg="white", foreground="purple1", width=15, command=self.show_home)
        back_button.grid(row=6, column=1)


########### UPDATE CONTACT FUNCTIONS ###############
    #Insert the update frame page
    def show_update_page(self):
        self.home_frame.grid_remove()
        self.update_frame.grid()
        self.updatepage()

    #Update Process
    def update_contact(self, name, email , phone_number ,address):
        if phone_number != "" and phone_number in self.__data:
            lst_info = self.__data[phone_number]
            if name != "":
                lst_info[0] = name
            if address != "":
                lst_info[1] = email
            if email != "":
                lst_info[3] = address
            self.__data[phone_number] = lst_info
            messagebox.showinfo("Success" , "Data updated successfully")
        else:
            messagebox.showerror("Error" , "Phone number does not exists in the database")

    #UpdatePage
    def updatepage(self):
        self.title("Update Contact Page")
        Name = Label(self.update_frame, text="Name:")
        Name.grid(row=1, column=0)
        Name_input = Entry(self.update_frame)
        Name_input.grid(row=1, column=1)
        
        Email = Label(self.update_frame, text="Email:")
        Email.grid(row=2, column=0)
        Email_input = Entry(self.update_frame)
        Email_input.grid(row=2, column=1)

        Phone = Label(self.update_frame, text="Phone Number:")
        Phone.grid(row=3, column=0)
        Phone_input = Entry(self.update_frame)
        Phone_input.grid(row=3, column=1)

        Adress = Label(self.update_frame, text="Adress:")
        Adress.grid(row=4, column=0)
        Adress_input = Entry(self.update_frame)
        Adress_input.grid(row=4, column=1)

        #Call the Process
        update_button = Button(self.update_frame, text="UPDATE", font=button_font, bg="white", foreground="purple1", width=15, command=lambda: self.update_contact(Name_input.get(),Email_input.get(),Phone_input.get(),Adress_input.get()))
        update_button.grid(row=5, column=1)

        #Back to home
        back_button = Button(self.update_frame, text="Back to Home", font=button_font, bg="white", foreground="purple1", width=15, command=self.show_home)
        back_button.grid(row=6, column=1)


########### DELETE CONTATCT FUNCTIONS ###############
    #Insert the delete frame page
    def show_delete_page(self):
        self.home_frame.grid_remove()
        self.delete_frame.grid()
        self.deletepage()

    #Delete Process
    def delete_contact(self, phone_number):
        if phone_number != "":
            if phone_number in self.__data:
                del self.__data[phone_number]
                messagebox.showinfo("Success", "Deleted successfully")
                self.show_home()
            else:
                messagebox.showwarning("Warning","Phone number does not exists in the database")
                self.show_home()
        else:
            messagebox.showerror("Error","Please enter phone number")
            self.show_home()

    #DeletePage (it's about an askstring)
    def deletepage(self):
        phone_num = askstring('DeletePage' , 'Enter your number Phone:')
        self.delete_contact(phone_num)


########### SEARCH CONTACT FUNCTIONS ###############
    #Insert the search frame page
    def show_search_page(self):
        self.home_frame.grid_remove()
        self.search_frame.grid()
        self.searchpage()

    #Search Page
    def search_contact(self, query):
        if query != "":
            if query in self.__data:
                messagebox.showinfo("Contact Found !", "Name: " + self.__data[query][0]+ "\nEmail:" + self.__data[query][1]+ "\nAddress:" + self.__data[query][3])            
                self.show_home()
        else:
            messagebox.showerror("Contact UnFound !", "Please check view contact page")
            self.show_view_page()

    #SearchPage
    def searchpage(self):
        #Let input a query as number phone to search contact information:
        query = Label(self.search_frame, text="Enter Number Phone:")
        query.grid(row=3, column=0)
        query_input = Entry(self.search_frame)
        query_input.grid(row=3, column=1)

        #Call the Process
        search_button = Button(self.search_frame, text="SEARCH", font=button_font, bg="white", foreground="purple1", width=15, command=lambda: self.search_contact(query_input.get()))
        search_button.grid(row=5, column=1)

        #Back to home
        back_button = Button(self.search_frame, text="Back to Home", font=button_font, bg="white", foreground="purple1", width=15, command=self.show_home)
        back_button.grid(row=6, column=1)
        


########################### Main Function ##############################
App = Contact()
App.configure(background="white")
App.mainloop()