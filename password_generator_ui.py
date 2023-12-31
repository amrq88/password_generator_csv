import tkinter as tk
import csv
from password_generator import PasswordGenerator

class PasswordGeneratorUI:
    def __init__(self, root):
        self.root = root
        self.root.title('Random Password Generator')
        
        # Create input fields
        self.purpose_label = tk.Label(root, text='Password for:')
        self.purpose_entry = tk.Entry(root)
        
        self.url_label = tk.Label(root, text='URL:')
        self.url_entry = tk.Entry(root)
        
        self.email_label = tk.Label(root, text='Email:')
        self.email_entry = tk.Entry(root)
        
        # Create generate button
        self.generate_button = tk.Button(root, text='Generate', command=self.generate_password)
        
        # Place input fields and button in the UI
        self.purpose_label.pack()
        self.purpose_entry.pack()
        self.url_label.pack()
        self.url_entry.pack()
        self.email_label.pack()
        self.email_entry.pack()
        self.generate_button.pack()
        
    def generate_password(self):
        # Get input values
        purpose = self.purpose_entry.get()
        url = self.url_entry.get()
        email = self.email_entry.get()
        
        # Generate password
        password_gen = PasswordGenerator()
        password = password_gen.generate_password()
        
        # Save information in CSV
        with open('passwords.csv', 'a', newline='') as file:
            # Add headers if the file is empty
            if file.tell() == 0:
                writer = csv.writer(file)
                writer.writerow(['Purpose', 'Email', 'URL (optional)', 'Password'])
            writer = csv.writer(file)
            writer.writerow([purpose,url, email, password])
            
        # Display the generated password
        password_display = tk.Label(self.root, text=f'Generated Password: {password}')
        password_display.pack()

# Create the root window
root = tk.Tk()

# Initialize the UI
password_ui = PasswordGeneratorUI(root)

# Run the UI
root.mainloop()