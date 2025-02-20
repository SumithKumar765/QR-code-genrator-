import qrcode
import base64
import os
from PIL import Image, ImageDraw

def generate_colored_qr(data, output_path="colored_qrcode.png", fill_color="blue", back_color="white"):
    """Generates a colorful QR code with custom foreground and background colors."""
    qr = qrcode.QRCode(
        version=None,  # Auto-select version
        error_correction=qrcode.constants.ERROR_CORRECT_L,  # Low correction for more data
        box_size=10, 
        border=4
    )
    qr.add_data(data)
    qr.make(fit=True)

    img = qr.make_image(fill_color=fill_color, back_color=back_color)
    img.save(output_path)
    print(f"✅ QR Code saved as {output_path}")

def split_data(data, chunk_size=1000):
    """Splits large data into smaller chunks for multiple QR codes."""
    return [data[i:i+chunk_size] for i in range(0, len(data), chunk_size)]

def generate_qr_from_file(file_path):
    """Encodes file content into one or multiple QR codes."""
    if not os.path.exists(file_path):
        print("❌ Error: File not found!")
        return
    
    with open(file_path, "rb") as file:
        file_data = file.read()
        encoded_data = base64.b64encode(file_data).decode("utf-8")  # Base64 encoding to handle binary data

    chunks = split_data(encoded_data)

    for i, chunk in enumerate(chunks):
        output_filename = f"file_qrcode_{i+1}.png"
        generate_colored_qr(chunk, output_filename, fill_color="purple", back_color="lightyellow")
        print(f"✅ QR Code {i+1}/{len(chunks)} saved: {output_filename}")

def generate_qr_from_url(url):
    """Generates a QR code from a URL."""
    generate_colored_qr(url, "url_qrcode.png", fill_color="darkgreen", back_color="lightblue")

if __name__ == "__main__":
    print("📌 Select an option:")
    print("1️⃣ Convert a file to QR Code")
    print("2️⃣ Convert a URL to QR Code")

    choice = input("Enter your choice (1 or 2): ")

    if choice == "1":
        file_path = input("Enter the file path: ").strip().replace("\\", "/")
        generate_qr_from_file(file_path)

    elif choice == "2":
        url = input("Enter the URL: ").strip()
        generate_qr_from_url(url)

    else:
        print("❌ Invalid choice! Please enter 1 or 2.")
