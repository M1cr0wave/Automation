# Chrome Undetected and Selenium Script

This repository contains a Python script that utilizes `undetected_chromedriver` and Selenium to automate Google Meet interactions for multiple users.

## Prerequisites

Before running the script, make sure you have the following installed:

- Python: [Download Python](https://www.python.org/downloads/)
- Pip: [Installation Guide](https://pip.pypa.io/en/stable/installation/)
- Chrome Browser: [Download Chrome](https://www.google.com/chrome/)
- Chromedriver: [Download Chromedriver](https://sites.google.com/chromium.org/driver/)

## Installation

1. Clone the repository:

```bash
git clone https://github.com/your-username/your-repository.git
cd your-repository
```
2. Install the required Python packages:
```bash
pip install undetected-chromedriver selenium
```
## Usage
1. Open the script file (your_script.py) in a text editor.
2. Set the name list with the desired usernames.
   ```bash
   name = ["User1", "User2", "User3", "User4", "User5", "User6"]
   ```
3. Change the URL in the driver.get() function
4. Run the script
   ```bash
   python your_script.py
   ```
   
## Script Overview

- The script utilizes `undetected_chromedriver` to bypass automated bot detection mechanisms.
- A new Chrome instance is created for each user in the provided list.
- The Google Meet link is opened, and microphone settings are configured.
- The user's name is inputted, and the "Join" button is clicked.
- Adjust the script as needed based on your requirements.

## Disclaimer

This script is for educational and testing purposes only. Ensure compliance with the terms of service of the websites you interact with.

## License

This project is licensed under the [MIT License](LICENSE).
