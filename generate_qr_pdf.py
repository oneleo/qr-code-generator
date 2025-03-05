import os
import pandas as pd
import qrcode
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from dotenv import load_dotenv
from pathlib import Path

# Load environment variables
dotenv_path = Path(".env")
load_dotenv(dotenv_path=dotenv_path)


def generate_qr_pdf(csv_filename):
    # Check if the file exists
    if not os.path.exists(csv_filename):
        raise FileNotFoundError(f"CSV file not found: {csv_filename}")

    # Read CSV file
    df = pd.read_csv(csv_filename, header=None)

    # PDF settings
    pdf_filename = "output.pdf"
    c = canvas.Canvas(pdf_filename, pagesize=A4)
    width, height = A4

    # QR Code layout
    cols, rows = 5, 7
    qr_size = 100
    padding = 15
    x_start, y_start = 20, height - 125

    # Generate QR Codes
    for i, row in enumerate(df.iterrows()):
        url = row[1][0].strip()
        print("i: ", i, "url: ", url)
        qr = qrcode.make(url)
        qr_path = f"qr_{i}.png"
        qr.save(qr_path)

        # Calculate QR Code position
        # page_index = i // (cols * rows)
        row_in_page = (i % (cols * rows)) // cols
        col_in_page = (i % (cols * rows)) % cols

        x = x_start + col_in_page * (qr_size + padding)
        y = y_start - row_in_page * (qr_size + padding)

        # Page break logic
        if i > 0 and i % (cols * rows) == 0:
            print("next")
            c.showPage()
            x = x_start
            y = y_start

        c.drawImage(qr_path, x, y, qr_size, qr_size)
        os.remove(qr_path)  # Delete temp image immediately

    c.save()
    print(f"PDF generated: {pdf_filename}")


def main():
    csv_filename = os.getenv("CSV_FILE_PATH", "").strip()
    print("csv_filename: ", csv_filename)

    if not csv_filename:
        print("CSV file path not set. Please define CSV_FILE_PATH in the .env file.")
        return

    try:
        generate_qr_pdf(csv_filename)
    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
