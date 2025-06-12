# gui/invoicing.py

import os, datetime, smtplib, ssl

from email.message import EmailMessage

from reportlab.lib.pagesizes import A4

from reportlab.pdfgen import canvas

INVOICE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "invoices"))


# ---------- 1. Generate PDF ----------

def create_pdf(order_id: int, customer: dict, items: list[dict], total: float) -> str:
    """

    customer = {"name": "...", "email": "..."}

    items    = [{"name": "...", "qty": 1, "price": 30.0}, ...]

    Returns the path of the generated PDF.

    """

    os.makedirs(INVOICE_DIR, exist_ok=True)

    file_path = os.path.join(INVOICE_DIR, f"invoice_{order_id}.pdf")

    c = canvas.Canvas(file_path, pagesize=A4)

    w, h = A4

    # Header

    c.setFont("Helvetica-Bold", 16)

    c.drawString(50, h - 50, "LiliWelt Academy")

    c.setFont("Helvetica", 10)

    c.drawString(50, h - 70, f"Invoice No. {order_id}")

    c.drawString(50, h - 85, f"Date: {datetime.date.today():%d.%m.%Y}")

    # Customer

    c.drawString(50, h - 115, f"Bill to: {customer['name']}")

    c.drawString(50, h - 130, f"Email: {customer['email']}")

    # Table header

    c.drawString(50, h - 165, "Description")

    c.drawString(300, h - 165, "Qty")

    c.drawString(360, h - 165, "Price")

    y = h - 180

    # Items

    for it in items:
        c.drawString(50, y, it["name"])

        c.drawRightString(330, y, str(it["qty"]))

        c.drawRightString(420, y, f"€{it['price']:.2f}")

        y -= 15

    # Total

    c.setFont("Helvetica-Bold", 12)

    c.drawRightString(420, y - 10, f"Total: €{total:.2f}")

    c.showPage()

    c.save()

    return file_path


# ---------- 2. Send e-mail ----------

def send_email(pdf_path: str, customer: dict):
    """

    Send invoice to customer via SMTP

    It requires environment variables:

        MAIL_USER -> SMTP account (e.g. Gmail)

        MAIL_PW   -> app-password

    """

    smtp_user = os.getenv("MAIL_USER")

    smtp_pw = os.getenv("MAIL_PW")

    if not smtp_user or not smtp_pw:
        raise RuntimeError("MAIL_USER o MAIL_PW no definidos")

    msg = EmailMessage()

    msg["Subject"] = "Your LiliWelt invoice"

    msg["From"] = smtp_user

    msg["To"] = customer["email"]

    msg.set_content(

        f"""Hello {customer['name']},

Thank you for your purchase! Your invoice is attached as a PDF.

Best regards,

LiliWelt Team"""

    )

    with open(pdf_path, "rb") as f:
        msg.add_attachment(f.read(),

                           maintype="application",

                           subtype="pdf",

                           filename=os.path.basename(pdf_path))

    # Gmail SSL (change host/port for other providers)

    context = ssl.create_default_context()

    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
        server.login(smtp_user, smtp_pw)

        server.send_message(msg)

