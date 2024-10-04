# URL Shortener

A simple URL shortener application built with Python and customtkinter.

## Features

* Shorten URLs using the Cutt.ly API
* Copy shortened URLs to clipboard
* Open shortened URLs in default browser
* View URL history
* Delete URL history
* Clear input fields

## Requirements

* Python 3.x
* customtkinter library
* requests library
* pyperclip library
* Cutt.ly API key (obtain from [Cutt.ly](https://cutt.ly/))

## Installation

1. Clone the repository: `git clone https://github.com/AliGohar2151/url-shortener.git`
2. Install required libraries: `pip install customtkinter requests pyperclip`
3. Create a `data.py` file with your Cutt.ly API key: `api = "your-api-key"`
4. Run the application: `python main.py`

## Usage

1. Enter a URL to shorten in the input field
2. Click the "Shorten URL" button to shorten the URL
3. Click the "Copy to Clipboard" button to copy the shortened URL to clipboard
4. Click the "Open URL" button to open the shortened URL in default browser
5. View URL history by clicking the "URL History" button
6. Delete URL history by clicking the "Delete History" button
7. Clear input fields by clicking the "Clear Fields" button

## Contributing

Contributions are welcome! If you'd like to contribute to this project, please fork the repository and submit a pull request.

## Acknowledgments

* Cutt.ly API for providing a simple URL shortening service
* customtkinter library for providing a modern and customizable GUI framework
* requests library for providing a simple way to make HTTP requests
* pyperclip library for providing a simple way to copy text to clipboard
