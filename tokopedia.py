import requests
import time
from datetime import datetime
import re
from colorama import init, Fore, Style
import sys

# Inisialisasi colorama untuk Windows
init(autoreset=True)

# Fungsi untuk mendapatkan token OTP dari Tokopedia
def get_otp_token(nomor):
    token_url = f'https://accounts.tokopedia.com/otp/c/page?otp_type=116&msisdn={nomor}&ld=https%3A%2F%2Faccounts.tokopedia.com%2Fregister%3Ftype%3Dphone%26phone%3D{nomor}%26status%3DeyJrIjp0cnVlLCJtIjp0cnVlLCJzIjpmYWxzZSwiYm90IjpmYWxzZSwiZ2MiOmZhbHNlfQ%253D%253D'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Linux; Android 5.1.1; SM-G600S Build/LMY47V; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/59.0.3071.125 Mobile Safari/537.36',
        'Accept-Encoding': 'gzip, deflate',
        'Connection': 'keep-alive',
        'Origin': 'https://accounts.tokopedia.com',
        'Accept': 'application/json, text/javascript, */*; q=0.01',
        'X-Requested-With': 'XMLHttpRequest',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8'
    }
    
    try:
        token_response = requests.get(token_url, headers=headers)
        token_response.raise_for_status()
        token_match = re.search(r'\<input\ id=\"Token\"\ value=\"(.*?)\"\ type\=\"hidden\"\>', token_response.text)
        if token_match:
            return token_match.group(1)
        else:
            print_color(f'Failed to find token for {nomor}.', Fore.RED)
            return None
    except requests.exceptions.RequestException as e:
        print_color(f'Failed to get token for {nomor}. Error: {e}', Fore.RED)
        return None

# Fungsi untuk mengirim OTP menggunakan token yang telah didapatkan
def kirim_otp_tokopedia(nomor, token):
    otp_url = 'https://accounts.tokopedia.com/otp/c/ajax/request-wa'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Linux; Android 5.1.1; SM-G600S Build/LMY47V; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/59.0.3071.125 Mobile Safari/537.36',
        'Accept-Encoding': 'gzip, deflate',
        'Connection': 'keep-alive',
        'Origin': 'https://accounts.tokopedia.com',
        'Accept': 'application/json, text/javascript, */*; q=0.01',
        'X-Requested-With': 'XMLHttpRequest',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8'
    }

    data = {
        "otp_type": "116",
        "msisdn": nomor,
        "tk": token,
        "email": '',
        "original_param": "",
        "user_id": "",
        "signature": "",
        "number_otp_digit": "6"
    }
    
    successes = 0
    failures = 0
    
    try:
        while True:
            try:
                # Kirim OTP
                otp_response = requests.post(otp_url, headers=headers, data=data)
                otp_response.raise_for_status()
                
                response_data = otp_response.json()
                success = response_data.get('success', False)
                error_message = response_data.get('error_message', '')
                
                if success:
                    print_color(f'Successfully sent OTP to {nomor}.', Fore.GREEN)
                    successes += 1
                else:
                    print_color(f'Failed to send OTP to {nomor}. Error message: {error_message}', Fore.RED)
                    failures += 1
                    if "Anda sudah melakukan 3 kali pengiriman kode, silakan coba lagi dalam" in error_message:
                        print_color('Reached OTP sending limit. Stopping script.', Fore.RED)
                        break
                
                # Pause 60 detik setelah pengiriman OTP
                print_color(f'Waiting for 60 seconds before sending the next OTP...', Fore.YELLOW)
                for countdown in range(60, 0, -1):
                    print_progress(countdown, 60)
                    time.sleep(1)
                print_color('', Fore.YELLOW)  # Baris baru setelah countdown
            
            except requests.exceptions.RequestException as e:
                print_color(f'Failed to send OTP to {nomor}. Error: {e}', Fore.RED)
            
    except KeyboardInterrupt:
        print_color('\nProcess interrupted by user. Exiting...', Fore.RED)
        sys.exit(0)  # Keluar dari program

# Fungsi untuk menampilkan pesan ke terminal dengan warna
def print_color(message, color=Fore.WHITE, end='\n', flush=False):
    print(color + f'{message}' + Style.RESET_ALL, end=end, flush=flush)

# Fungsi untuk menampilkan progress bar
def print_progress(countdown, total):
    percent = (total - countdown) / total * 100
    bar = '#' * int(percent / 2) + '-' * (50 - int(percent / 2))
    sys.stdout.write(f'\r[{bar}] {percent:.2f}%')
    sys.stdout.flush()

# Fungsi untuk menampilkan deskripsi dalam bentuk box
def print_description():
    description = [
        "+------------------------------------------------------------+",
        "|               Tokopedia OTP Sender by @idugeni             |",
        "|                                                            |",
        "| This script sends OTP (One-Time Password) messages to a    |",
        "| specified phone number using Tokopedia's API.              |",
        "|                                                            |",
        "| Instructions:                                              |",
        "| 1. Enter the phone number where OTP should be sent or      |",
        "|    provide a file with multiple numbers.                   |",
        "| 2. The script will respect Tokopedia's policy of not       |",
        "|    sending more than 3 OTPs within 3 minutes.              |",
        "| 3. Press Ctrl + C to stop the script at any time.          |",
        "+------------------------------------------------------------+",
        "| For more information, visit:                               |",
        "| https://github.com/idugeni/ or https://idugeni.github.io/  |",
        "+------------------------------------------------------------+",
    ]
    
    for line in description:
        print_color(line, Fore.GREEN)

# Fungsi untuk membaca nomor telepon dari file
def read_phone_numbers_from_file(filename):
    try:
        with open(filename, 'r') as file:
            numbers = [line.strip() for line in file.readlines()]
        return numbers
    except Exception as e:
        print_color(f'Error reading file: {e}', Fore.RED)
        return []

# Main program
def main():
    print_color("=" * 60, Fore.GREEN)
    print_description()
    print_color("=" * 60, Fore.GREEN)
    print("")  # Baris kosong
    
    # Memilih antara memasukkan nomor langsung atau dari file
    choice = input(Fore.CYAN + 'Pilih 1 untuk memasukkan nomor langsung, atau 2 untuk mengambil dari file (.txt): ' + Style.RESET_ALL)
    
    if choice == '1':
        # Meminta nomor langsung
        nomor_tujuan = input(Fore.CYAN + 'Masukkan nomor tujuan (contoh: 08123456789): ' + Style.RESET_ALL)
        phone_numbers = [nomor_tujuan]
    elif choice == '2':
        # Meminta nama file
        filename = input(Fore.CYAN + 'Masukkan nama file (.txt) yang berisi nomor telepon: ' + Style.RESET_ALL)
        phone_numbers = read_phone_numbers_from_file(filename)
    else:
        print_color('Pilihan tidak valid. Harap pilih 1 atau 2.', Fore.RED)
        return
    
    for nomor_tujuan in phone_numbers:
        print_color(f'\nProcessing number: {nomor_tujuan}', Fore.CYAN)
        token = get_otp_token(nomor_tujuan)
        if token:
            # Memulai pengiriman OTP
            kirim_otp_tokopedia(nomor_tujuan, token)
        else:
            print_color(f'Unable to proceed without token for {nomor_tujuan}.', Fore.RED)

# Menjalankan program utama
if __name__ == "__main__":
    main()
