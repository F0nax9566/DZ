import requests
from bs4 import BeautifulSoup as BS
import re
import tkinter as tk
from tkinter import ttk

class CurrencyConverterApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Currency Conversion")

        self.style = ttk.Style()
        self.style.configure("TButton", padding=6, relief="flat", background="#3498db", foreground="black", font=("Arial", 12))
        self.style.configure("TLabel", padding=6, background="#ecf0f1", font=("Arial", 12))
        self.style.configure("TEntry", padding=6, font=("Arial", 12))

        self.create_widgets()

    def create_widgets(self):
        self.configure(bg="#ecf0f1")

        label = ttk.Label(self, text="Enter the amount of hryvnia you want to convert:", style="TLabel")
        label.pack(pady=10)

        self.entry = ttk.Entry(self, style="TEntry")
        self.entry.pack(pady=10)

        convert_button = ttk.Button(self, text="Convert", command=self.get_currency_conversion, style="TButton")
        convert_button.pack(pady=10)

        self.result_label = ttk.Label(self, text="", style="TLabel")
        self.result_label.pack(pady=10)

    def get_currency_conversion(self):
        url = 'https://www.currency.me.uk/convert/usd/uah'
        r = requests.get(url)
        soup = BS(r.text, 'lxml')
        curs_text = soup.find("span", {"class": "mini ccyrate"}).text

        numeric_part = float(re.search(r'\d+\.\d+', curs_text).group())

        try:
            user_input = float(self.entry.get())
        except ValueError:
            self.result_label.config(text="Please enter a valid numeric value.")
            return

        result = user_input / numeric_part
        self.result_label.config(text=f"{user_input} hryvnia in dollars will be: {result:.2f}$")

if __name__ == "__main__":
    app = CurrencyConverterApp()
    app.mainloop()
