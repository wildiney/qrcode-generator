# QRCode Generator

![Python](https://img.shields.io/badge/Python-FFD43B?style=for-the-badge&logo=python&logoColor=blue)

This project is a QRCode generator made in Python. It provides scripts to generate QR codes for JSON API responses, URLs, and text inputs.

## Features

- Generate QR codes from JSON API responses with error formatting.
- Generate QR codes from URLs and text inputs.
- Save generated QR codes as image files in the `qrcodes` directory.

## Requirements

To install the required dependencies, run:

```sh
pip install -r requirements.txt
```

## Usage

### Generate QR Code for Texts and URLs

Run the script `qrcode-for-url-and-text.py` to generate a QR Code from the data that you input:

```sh
python qrcode-for-url-and-text.py
```

### Generate QR Code for JSON API Response

Run the script `qrcode-for-json.py` to generate a QR code from a JSON API response:

```sh
python qrcode-for-json.py
```

## License

This project is licensed under the MIT License.
