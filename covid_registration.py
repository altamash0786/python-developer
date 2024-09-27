import tkinter as tk
from tkinter import messagebox

class CovidRegistrationForm:
    def __init__(self, master):
        self.master = master
        self.master.title("COVID-19 Registration Form")
        self.master.geometry("300x300")

        # Create and place labels and entry fields
        tk.Label(master, text="Full Name:").pack(pady=5)
        self.name_entry = tk.Entry(master)
        self.name_entry.pack(pady=5)

        tk.Label(master, text="Age:").pack(pady=5)
        self.age_entry = tk.Entry(master)
        self.age_entry.pack(pady=5)

        tk.Label(master, text="Contact Number:").pack(pady=5)
        self.contact_entry = tk.Entry(master)
        self.contact_entry.pack(pady=5)

        tk.Label(master, text="Symptoms:").pack(pady=5)
        
        self.symptoms_var = tk.StringVar(value="None")
        tk.Radiobutton(master, text="Fever", variable=self.symptoms_var, value="Fever").pack(anchor="w")
        tk.Radiobutton(master, text="Cough", variable=self.symptoms_var, value="Cough").pack(anchor="w")
        tk.Radiobutton(master, text="None", variable=self.symptoms_var, value="None").pack(anchor="w")

        # Submit button
        tk.Button(master, text="Submit", command=self.submit_form).pack(pady=20)

    def submit_form(self):
        name = self.name_entry.get()
        age = self.age_entry.get()
        contact = self.contact_entry.get()
        symptoms = self.symptoms_var.get()

        # Validate input
        if name and age and contact:
            result = f"Name: {name}\nAge: {age}\nContact: {contact}\nSymptoms: {symptoms}"
            messagebox.showinfo("Registration Successful", result)
        else:
            messagebox.showwarning("Input Error", "Please fill all the fields")

if __name__ == "__main__":
    root = tk.Tk()
    app = CovidRegistrationForm(root)
    root.mainloop()
