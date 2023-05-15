import tkinter as tk
from tkinter import ttk
import mysql.connector
import customtkinter as ctk
import os

class CarFormFill:
    
    def add_car(self, car):

        cnx = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="carinventory"
        )

        cursor = cnx.cursor()

        if cnx.is_connected():
         print("Connected to the database!")
        else:
         print("Failed to connect to the database!")

        query = "INSERT INTO cars (mark, model, year, carburetor_type, number_of_places, transmission, price_per_day, availability, image) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"
        values = (car['mark'], car['model'], car['year'], car['carburetor'], car['places'], car['transmission'], car['price'], car['availability'], car['image'])
        cursor.execute(query, values)

        cnx.commit()

        cursor.close()
        cnx.close()


    def __init__(self, master):
        def open_car_inventory():
            master.destroy()
            os.system('python inventory.py')

        title_label = ctk.CTkLabel(master, text="ADD CAR TO INVENTORY", font=ctk.CTkFont(size=20, weight="bold"))
        title_label.pack(padx=10, pady=(40, 20))

        self.scrollable_frame = ctk.CTkScrollableFrame(root, width=500, height=250)
        self.scrollable_frame.pack()


        self.mark_entry = ctk.CTkEntry(self.scrollable_frame, placeholder_text="Add Mark",font=ctk.CTkFont(size=14), height=35)
        self.mark_entry.pack(fill="x")
        self.model_entry = ctk.CTkEntry(self.scrollable_frame, placeholder_text="Add Model",font=ctk.CTkFont(size=14), height=35)
        self.model_entry.pack(fill="x")
        self.year_entry = ctk.CTkEntry(self.scrollable_frame, placeholder_text="Add Year",font=ctk.CTkFont(size=14), height=35)
        self.year_entry.pack(fill="x")
        self.carburetor_entry = ctk.CTkEntry(self.scrollable_frame, placeholder_text="Add Carburetor",font=ctk.CTkFont(size=14), height=35)
        self.carburetor_entry.pack(fill="x")
        self.places_entry = ctk.CTkEntry(self.scrollable_frame, placeholder_text="Add Number of Places",font=ctk.CTkFont(size=14), height=35)
        self.places_entry.pack(fill="x")
        self.transmission_entry = ctk.CTkEntry(self.scrollable_frame, placeholder_text="Add Transmission",font=ctk.CTkFont(size=14), height=35)
        self.transmission_entry.pack(fill="x")
        self.price_entry = ctk.CTkEntry(self.scrollable_frame, placeholder_text="Add Rent Price",font=ctk.CTkFont(size=14), height=35)
        self.price_entry.pack(fill="x")
        self.availability_entry = ctk.CTkEntry(self.scrollable_frame, placeholder_text="Add Availability",font=ctk.CTkFont(size=14), height=35)
        self.availability_entry.pack(fill="x")
        self.image_entry = ctk.CTkEntry(self.scrollable_frame, placeholder_text="Add Image Path",font=ctk.CTkFont(size=14), height=35)
        self.image_entry.pack(fill="x")

        ttk.Separator(orient="horizontal").pack(fill="x", padx=200, pady=20)


        self.scrollable_frame1 = ctk.CTkScrollableFrame(root, width=1000, height=400,orientation="horizontal")
        self.scrollable_frame1.pack(padx=100,pady=10)
       
        submit_button = ctk.CTkButton(root, text="Add", width=500, command=self.submit_form)
        submit_button.pack(pady=10,side=tk.TOP)

        done_button = ctk.CTkButton(root, text="Done", width=100, command=open_car_inventory)
        done_button.pack(side=tk.BOTTOM)


    def submit_form(self):
        mark = self.mark_entry.get()
        model = self.model_entry.get()
        year = self.year_entry.get()
        carburetor = self.carburetor_entry.get()
        places = self.places_entry.get()
        transmission = self.transmission_entry.get()
        price = self.price_entry.get()
        availability = self.availability_entry.get()
        image = self.image_entry.get()
        
        if not all([mark, model, year, carburetor, places, transmission, price, availability, image]):
            tk.messagebox.showerror("Error", "Please fill in all fields")
            return

        # Validate that year and price are numbers
        if not year.isdigit():
            tk.messagebox.showerror("Error", "Please enter a valid year")
            self.year_entry.delete(0, ctk.END)
            return

        if not price.isdigit():
            tk.messagebox.showerror("Error", "Please enter a valid price")
            self.price_entry.delete(0, ctk.END)
            return

        if not places.isdigit():
            tk.messagebox.showerror("Error", "Please enter a valid number of places")
            self.places_entry.delete(0, ctk.END)
            return
       
        new_car = {
            "mark" : self.mark_entry.get(),
            "model" : self.model_entry.get(),
            "year" : self.year_entry.get(),
            "carburetor" : self.carburetor_entry.get(),
            "places" : self.places_entry.get(),
            "transmission" : self.transmission_entry.get(),
            "price" : self.price_entry.get()+"$",
            "availability" : self.availability_entry.get(),
            "image" : "cars/"+self.image_entry.get()+".png"
        }

        self.add_car(new_car)

        car_frame = ctk.CTkFrame(self.scrollable_frame1)
        car_frame.pack(fill="x", pady=3)

        # add labels for the car information to the new frame
        ctk.CTkLabel(car_frame, text=f"{new_car['mark']}", font=ctk.CTkFont(size=15), width=80, anchor='center').pack(pady=1,side="left", padx=50, fill='y')
        ctk.CTkLabel(car_frame, text=f"{new_car['model']}", font=ctk.CTkFont(size=15), width=70, anchor='w').pack(side="left",pady=1, padx=50, fill='y')
        ctk.CTkLabel(car_frame, text=f"{new_car['year']}", font=ctk.CTkFont(size=15), width=50, anchor='center').pack(side="left",pady=1, padx=50, fill='y')
        ctk.CTkLabel(car_frame, text=f"{new_car['carburetor']}", font=ctk.CTkFont(size=15), width=70, anchor='center').pack(side="left",pady=1, padx=50, fill='y')
        ctk.CTkLabel(car_frame, text=f"{new_car['places']} places", font=ctk.CTkFont(size=15), width=140, anchor='center').pack(side="left",pady=1, padx=50, fill='y')
        ctk.CTkLabel(car_frame, text=f"{new_car['transmission']}", font=ctk.CTkFont(size=15), width=100, anchor='center').pack(side="left",pady=1, padx=50, fill='y')
        ctk.CTkLabel(car_frame, text=f"{new_car['price']}", font=ctk.CTkFont(size=15), width=65, anchor='center').pack(side="left",pady=1, padx=50, fill='y')
        ctk.CTkLabel(car_frame, text=f"{new_car['availability']}", font=ctk.CTkFont(size=15), width=90, anchor='center').pack(side="left",pady=1, padx=50, fill='y')


        car_frame.pack()

        self.mark_entry.delete(0, ctk.END)
        self.model_entry.delete(0, ctk.END)
        self.year_entry.delete(0, ctk.END)
        self.carburetor_entry.delete(0, ctk.END)
        self.places_entry.delete(0, ctk.END)
        self.transmission_entry.delete(0, ctk.END)
        self.price_entry.delete(0, ctk.END)
        self.availability_entry.delete(0, ctk.END)
        self.image_entry.delete(0, ctk.END)


        # Print the values to the console
        print("Mark:", mark)
        print("Model:", model)
        print("Year:", year)
        print("Type of carburetor:", carburetor)
        print("Number of places:", places)
        print("Transmission:", transmission)


root = ctk.CTk()
root.geometry("1000x950")
root.title("ADD CAR")
add_car= CarFormFill(root)
root.mainloop()
