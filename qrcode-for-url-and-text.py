from os.path import exists

import qrcode
import re
import os
import sys
from urllib.parse import urlparse

def is_valid_url(data):
    parsed_url = urlparse(data)
    return all([parsed_url.scheme, parsed_url.netloc])

def sanitize_filename(data):
    if is_valid_url(data):
        filename = re.sub(r"[^\w\-]", "_", urlparse(data).netloc)
    else:
        filename = re.sub(r"[^\w\-]", "_", data[:20])
    return filename + ".jpg"

def generate_qrcode(data):
    try:
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_H,
            box_size= 10,
            border=4
        )
        qr.add_data(data)
        qr.make(fit=True)

        img = qr.make_image(fill_color="black", back_color="white")

        if not os.path.exists('./qrcodes/'):
            os.mkdir('qrcodes')

        filename=sanitize_filename(data)
        img.save(f"qrcodes/{filename}")

        print(f"QR Code salvo com sucesso como {filename}")

    except Exception as e:
        print(f"Erro ao gerar o QR Code: {e}", file=sys.stderr)


def main():
    while True:
        data = input("Digite a URL ou um texto para gerar o QRCode: ").strip()

        if not data:
            print("Erro: A entrada não pode estar vazia.")
            continue

        generate_qrcode(data)
        break


if __name__ == '__main__':
    main()
