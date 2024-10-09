import tkinter as tk
from tkinter import messagebox

# In-memory storage for book data
library = []

# GUI
class LibraryApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Library Management System")

        # Labels
        self.lbl_title = tk.Label(root, text="Title")
        self.lbl_title.grid(row=0, column=0)

        self.lbl_author = tk.Label(root, text="Author")
        self.lbl_author.grid(row=1, column=0)

        self.lbl_year = tk.Label(root, text="Year")
        self.lbl_year.grid(row=2, column=0)

        # Entry fields
        self.title_text = tk.StringVar()
        self.entry_title = tk.Entry(root, textvariable=self.title_text)
        self.entry_title.grid(row=0, column=1)

        self.author_text = tk.StringVar()
        self.entry_author = tk.Entry(root, textvariable=self.author_text)
        self.entry_author.grid(row=1, column=1)

        self.year_text = tk.StringVar()
        self.entry_year = tk.Entry(root, textvariable=self.year_text)
        self.entry_year.grid(row=2, column=1)

        # Listbox and scrollbar
        self.book_list = tk.Listbox(root, height=8, width=50)
        self.book_list.grid(row=3, column=0, rowspan=6, columnspan=2)

        self.scrollbar = tk.Scrollbar(root)
        self.scrollbar.grid(row=3, column=2, rowspan=6)

        self.book_list.configure(yscrollcommand=self.scrollbar.set)
        self.scrollbar.configure(command=self.book_list.yview)

        self.book_list.bind('<<ListboxSelect>>', self.get_selected_row)

        # Buttons
        self.btn_view_all = tk.Button(root, text="View All", width=12, command=self.view_all_books)
        self.btn_view_all.grid(row=3, column=3)

        self.btn_search_entry = tk.Button(root, text="Search Entry", width=12, command=self.search_books)
        self.btn_search_entry.grid(row=4, column=3)

        self.btn_add_entry = tk.Button(root, text="Add Entry", width=12, command=self.add_book)
        self.btn_add_entry.grid(row=5, column=3)

        self.btn_update_selected = tk.Button(root, text="Update Selected", width=12, command=self.update_book)
        self.btn_update_selected.grid(row=6, column=3)

        self.btn_delete_selected = tk.Button(root, text="Delete Selected", width=12, command=self.delete_book)
        self.btn_delete_selected.grid(row=7, column=3)

        self.btn_close = tk.Button(root, text="Close", width=12, command=root.destroy)
        self.btn_close.grid(row=8, column=3)

    def get_selected_row(self, event):
        try:
            global selected_book_index
            index = self.book_list.curselection()[0]
            selected_book_index = index
            selected_book = library[index]

            self.entry_title.delete(0, tk.END)
            self.entry_title.insert(tk.END, selected_book["title"])

            self.entry_author.delete(0, tk.END)
            self.entry_author.insert(tk.END, selected_book["author"])

            self.entry_year.delete(0, tk.END)
            self.entry_year.insert(tk.END, selected_book["year"])
        except IndexError:
            pass

    def view_all_books(self):
        self.book_list.delete(0, tk.END)
        for book in library:
            self.book_list.insert(tk.END, f'{book["title"]}, {book["author"]}, {book["year"]}')

    def search_books(self):
        self.book_list.delete(0, tk.END)
        for book in library:
            if self.title_text.get().lower() in book["title"].lower():
                self.book_list.insert(tk.END, f'{book["title"]}, {book["author"]}, {book["year"]}')

    def add_book(self):
        book = {
            "title": self.title_text.get(),
            "author": self.author_text.get(),
            "year": self.year_text.get(),
        }
        library.append(book)
        self.view_all_books()

    def delete_book(self):
        if len(library) > 0:
            library.pop(selected_book_index)
            self.view_all_books()

    def update_book(self):
        library[selected_book_index] = {
            "title": self.title_text.get(),
            "author": self.author_text.get(),
            "year": self.year_text.get(),
        }
        self.view_all_books()

if __name__ == "__main__":
    root = tk.Tk()
    app = LibraryApp(root)
    root.mainloop()
