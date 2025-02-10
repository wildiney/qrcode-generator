import qrcode
import json
import sys
import os


def format_error_message(api_response):
    """Formata a resposta da API para exibição no QR Code."""
    try:
        # Se a entrada for uma string JSON, tentamos converter para dicionário
        if isinstance(api_response, str):
            data = json.loads(api_response)
        else:
            data = api_response  # Já é um dicionário válido

        error_code = str(data.get('status', 'N/A'))  # Captura o código do erro

        formatted_message = (
            f"Erro {error_code}: {data.get('error', 'Desconhecido')}\n"
            f"{data.get('message', 'Sem detalhes disponíveis.')}\n"
            f"Data: {data.get('timestamp', 'N/A')}"
        )
        return formatted_message, error_code  # Retorna mensagem formatada e código do erro

    except json.JSONDecodeError:
        return "Erro ao processar resposta da API. Formato inválido.", "desconhecido"


def generate_qrcode(data, error_code):
    """Gera e salva um QR Code a partir do texto recebido."""
    try:
        qr = qrcode.QRCode(
            version=10,
            error_correction=qrcode.constants.ERROR_CORRECT_H,
            box_size=10,
            border=4
        )
        qr.add_data(data)
        qr.make(fit=True)

        img = qr.make_image(fill_color="black", back_color="white")
        filename = f"{error_code}.jpg"

        if not os.path.exists('./qrcodes/'):
            os.mkdir('qrcodes')

        img.save(f"qrcodes/{filename}")

        print(f"QR Code gerado com sucesso: {filename}")

    except Exception as e:
        print(f"Erro ao gerar o QR Code: {e}", file=sys.stderr)


def main():
    api_response = '''{
        "status": 500,
        "error": "Internal Server Error",
        "message": "Ocorreu um erro interno no servidor",
        "timestamp": "2025-02-10T14:00:00Z"
    }'''

    if not api_response:
        print("Erro: Nenhum dado fornecido.")
        return

    formatted_message, error_code = format_error_message(api_response)
    generate_qrcode(formatted_message, error_code)


if __name__ == '__main__':
    main()
