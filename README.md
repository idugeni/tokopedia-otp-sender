# Tokopedia OTP Sender

![Tokopedia OTP Sender](https://opengraph.githubassets.com/ba48cab225ef8354c71500544e98b338/idugeni/tokopedia-otp-sender)

Aplikasi Python ini memungkinkan Anda untuk mengirimkan pesan OTP (One-Time Password) ke nomor tujuan dengan OTP dari Tokopedia menggunakan API mereka. Aplikasi ini mematuhi kebijakan Tokopedia yang membatasi pengiriman tidak lebih dari 3 OTP dalam waktu 1 jam. Anda dapat memasukkan nomor telepon secara langsung atau menggunakan file teks dengan daftar nomor.

<div align="center">
  <img src="https://img.shields.io/badge/python-3.x-blue.svg" alt="Python Version">
  <img src="https://img.shields.io/badge/license-MIT-green" alt="License">
  <img src="https://img.shields.io/github/repo-size/idugeni/tokopedia-otp-sender" alt="GitHub Repo Size">
  <img src="https://img.shields.io/github/last-commit/idugeni/tokopedia-otp-sender" alt="GitHub Last Commit">
</div>

## Requirement

* Python 3.x
* Requests library (`pip install requests`)
* Colorama library (`pip install colorama`)

## Cara Penggunaan

**1. Clone Repository:**

```powershell
git clone https://github.com/idugeni/tokopedia-otp-sender.git
```

```powershell
cd tokopedia-otp-sender
```

**2. Install Dependencies:**

```powershell
pip install -r requirements.txt
```

**3. Jalankan Script:**

```powershell
python tokopedia.py
```

**4. Ikuti Petunjuk:**

* Pilih `opsi 1` untuk memasukkan nomor telepon tunggal.
* Pilih `opsi 2` untuk menyediakan file `numbers.txt` dengan beberapa nomor telepon.
* Script akan mulai mengirimkan OTP dan menampilkan kemajuan dan akan mengirim maksimal 3 OTP dengan waktu tunda pesan 60 detik. Dapat diulang dengan tenggang waktu 1 jam karena alasan kebijakan dari Tokopedia.

## Fitur

* Mengirimkan OTP ke nomor tujuan dengan OTP dari Tokopedia menggunakan API mereka.
* Menghormati batasan tingkat kirim Tokopedia.
* Mendukung pengiriman OTP ke beberapa nomor dari file `numbers.txt`.
* Antarmuka konsol interaktif dengan output berkode warna.

## Lisensi

Proyek ini dilisensikan di bawah **Lisensi MIT** - lihat file [`LICENSE`](https://github.com/idugeni/tokopedia-otp-sender/blob/main/LICENSE) untuk detailnya.
