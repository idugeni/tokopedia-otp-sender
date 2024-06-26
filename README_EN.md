# Tokopedia OTP Sender

![Tokopedia OTP Sender](https://opengraph.githubassets.com/0/idugeni/Tokopedia-OTP-Sender)

This Python application allows you to send an OTP (One-Time Password) message to a destination number with an OTP from Tokopedia using their API. This app complies with Tokopedia's policy that limits sending no more than 3 OTPs within 1 hour. You can enter the phone number directly or use a text file with a list of numbers.

<div align="center">
  <img src="https://img.shields.io/badge/python-3.x-blue.svg" alt="Python Version">
  <img src="https://img.shields.io/badge/license-MIT-green" alt="License">
  <img src="https://img.shields.io/github/repo-size/idugeni/Tokopedia-OTP-Sender" alt="GitHub Repo Size">
  <img src="https://img.shields.io/github/last-commit/idugeni/Tokopedia-OTP-Sender" alt="GitHub Last Commit">
</div>

## Requirement

* Python 3.x
* Requests library (`pip install requests`)
* Colorama library (`pip install colorama`)

## How to use

**1. Clone Repository:**

```powershell
git clone https://github.com/idugeni/Tokopedia-OTP-Sender.git
```

```powershell
cd Tokopedia-OTP-Sender
```

**2. Install Dependencies:**

```powershell
pip install -r requirements.txt
```

**3. Run the Script:**

```powershell
python tokopedia.py
```

**4. Follow the Instructions:**

* Choose `option 1` to provide a single phone number.
* Choose `option 2` to provide `numbers.txt` file with multiple phone numbers.
* The script will start sending OTPs and display the progress and will send a maximum of 3 OTPs with a message delay time of 60 seconds. It can be repeated with a grace period of 1 hour due to policy reasons from Tokopedia.

## Features

* Send OTP to destination number with OTP from Tokopedia using their API.
* Respects Tokopedia send rate limitation.
* Supports sending OTP to multiple numbers from `numbers.txt` file.
* Interactive console interface with color-coded output.

## License

This project is licensed under the **MIT License** - see the file [`LICENSE`](https://github.com/idugeni/Tokopedia-OTP-Sender/blob/main/LICENSE) for details.
