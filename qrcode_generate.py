import qrcode


def main():
    data = ''

    while data == '':
        data = input("Digite a URL para gerar o QRCode: ")

    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=100,
        border=4
    )
    qr.add_data(data)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")
    img.save(data.replace("http://", "") + ".jpg")


if __name__ == '__main__':
    main()
