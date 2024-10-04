import requests
import urllib.parse
import customtkinter as ctk
from tkinter import messagebox
import webbrowser
import pyperclip
import data
import os


class URLShortener:
    def __init__(self, master):
        self.master = master
        self.master.title("Custom URL Shortener")
        self.master.geometry("600x600")
        self.master.configure(fg_color="#2b2b2b")

        self.font_header = ctk.CTkFont(family="Helvetica", size=20, weight="bold")
        self.font_normal = ctk.CTkFont(family="Arial", size=14)
        self.button_color = "#4CAF50"

        self.header_label = ctk.CTkLabel(
            self.master, text="URL Shortener", font=self.font_header, text_color="white"
        )
        self.header_label.pack(pady=20)

        self.label_url = ctk.CTkLabel(
            self.master,
            text="Enter the URL to shorten:",
            font=self.font_normal,
            text_color="white",
        )
        self.label_url.pack(pady=10)

        self.entry_url = ctk.CTkEntry(
            self.master,
            width=350,
            font=self.font_normal,
            fg_color="#e0e0e0",
            text_color="#333333",
        )
        self.entry_url.pack(pady=10)

        self.shortened_link = ctk.StringVar()

        self.label_shortened_url = ctk.CTkLabel(
            self.master,
            text="Shortened URL:",
            font=self.font_normal,
            text_color="white",
        )
        self.label_shortened_url.pack(pady=10)

        self.entry_shortened_url = ctk.CTkEntry(
            self.master,
            textvariable=self.shortened_link,
            state="readonly",
            width=350,
            font=self.font_normal,
            fg_color="#e0e0e0",
            text_color="#333333",
        )
        self.entry_shortened_url.pack(pady=10)

        # Frame to hold the buttons horizontally
        self.button_frame = ctk.CTkFrame(self.master, fg_color="#2b2b2b")
        self.button_frame.pack(pady=20)

        self.button_shorten = ctk.CTkButton(
            self.button_frame,
            text="Shorten URL",
            command=self.shorten_url,
            fg_color=self.button_color,
            text_color="white",
            hover_color="#45a049",
            font=self.font_normal,
        )
        self.button_shorten.grid(row=0, column=0, padx=5)

        self.button_copy = ctk.CTkButton(
            self.button_frame,
            text="Copy to Clipboard",
            command=self.copy_to_clipboard,
            fg_color=self.button_color,
            text_color="white",
            hover_color="#45a049",
            font=self.font_normal,
            state="disabled",
        )
        self.button_copy.grid(row=0, column=1, padx=5)

        self.button_open_url = ctk.CTkButton(
            self.button_frame,
            text="Open URL",
            command=self.open_shortened_url,
            fg_color=self.button_color,
            text_color="white",
            hover_color="#45a049",
            font=self.font_normal,
            state="disabled",
        )
        self.button_open_url.grid(row=0, column=2, padx=5)

        self.button_clear = ctk.CTkButton(
            self.button_frame,
            text="Clear Fields",
            command=self.clear_fields,
            fg_color="#FF5733",
            text_color="white",
            hover_color="#e74c3c",
            font=self.font_normal,
        )
        self.button_clear.grid(row=0, column=3, padx=5)

        self.button_delete_history = ctk.CTkButton(
            self.button_frame,
            text="Delete History",
            command=self.delete_history,
            fg_color="#FF5733",
            text_color="white",
            hover_color="#e74c3c",
            font=self.font_normal,
        )
        self.button_delete_history.grid(row=0, column=4, padx=5)

        self.url_history = []
        self.label_history = ctk.CTkLabel(
            self.master,
            text="URL History:",
            font=self.font_normal,
            text_color="white",
        )
        self.label_history.pack(pady=10)

        self.history_listbox = ctk.CTkTextbox(
            self.master, width=350, height=100, state="normal", font=self.font_normal
        )
        self.history_listbox.pack(pady=10)

        self.load_history()

    def shorten_url(self):
        original_url = self.entry_url.get()

        if not original_url:
            messagebox.showwarning("Input Error", "Please enter a URL.")
            return

        try:
            encoded_url = urllib.parse.urlencode({"short": original_url})
            api_url = f"https://cutt.ly/api/api.php?key={data.api}&{encoded_url}"

            response = requests.get(api_url).json()

            status = response["url"]["status"]
            if status == 7:
                short_url = response["url"]["shortLink"]
                self.shortened_link.set(short_url)
                self.url_history.append(short_url)
                self.update_history()
                self.save_history()
                self.button_open_url.configure(state="normal")
                self.button_copy.configure(state="normal")
                messagebox.showinfo("Success", "URL shortened successfully!")
            else:
                messagebox.showerror(
                    "Error", f"Status {status} - {response['url']['title']}"
                )
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {str(e)}")

    def copy_to_clipboard(self):
        short_url = self.shortened_link.get()
        if short_url:
            pyperclip.copy(short_url)
            messagebox.showinfo("Copied", "Shortened URL copied to clipboard.")
        else:
            messagebox.showwarning("Error", "No shortened URL to copy.")

    def open_shortened_url(self):
        short_url = self.shortened_link.get()
        if short_url:
            webbrowser.open(short_url)
        else:
            messagebox.showwarning("Error", "No shortened URL to open.")

    def clear_fields(self):
        self.entry_url.delete(0, "end")
        self.shortened_link.set("")
        self.button_copy.configure(state="disabled")
        self.button_open_url.configure(state="disabled")

    def update_history(self):
        self.history_listbox.delete("1.0", "end")
        for url in self.url_history:
            self.history_listbox.insert("end", f"{url}\n")

    def save_history(self):
        with open("url_history.txt", "w") as f:
            for url in self.url_history:
                f.write(url + "\n")

    def load_history(self):
        if os.path.exists("url_history.txt"):
            with open("url_history.txt", "r") as f:
                self.url_history = f.read().splitlines()
            self.update_history()

    def delete_history(self):
        if messagebox.askyesno(
            "Delete History", "Are you sure you want to delete the URL history?"
        ):
            self.url_history.clear()
            self.update_history()
            if os.path.exists("url_history.txt"):
                os.remove("url_history.txt")
                messagebox.showinfo("History Deleted", "URL history has been deleted.")


if __name__ == "__main__":
    app = ctk.CTk()
    url_shortener = URLShortener(app)
    app.mainloop()
