import os, datetime, smtplib, ssl

from email.message import EmailMessage

from reportlab.lib.pagesizes import A4

from reportlab.pdfgen import canvas

INVOICE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "invoices"))


# ---------------------------------------------------------------------------

def create_pdf(order_id: int, customer: dict, items: list[dict], total: float) -> str:
    """Generate PDF invoice and return its absolute path."""

    os.makedirs(INVOICE_DIR, exist_ok=True)

    pdf_path = os.path.join(INVOICE_DIR, f"invoice_{order_id}.pdf")

    c = canvas.Canvas(pdf_path, pagesize=A4)

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

    y = h - 160

    c.setFont("Helvetica-Bold", 10)

    c.drawString(50, y, "Item")

    c.drawString(250, y, "Qty")

    c.drawString(350, y, "Price")

    # Items

    c.setFont("Helvetica", 10)

    y -= 15

    for item in items:
        c.drawString(50, y, item["name"])

        c.drawString(250, y, str(item["qty"]))  # <-- usa 'qty'

        c.drawString(350, y, f"{item['price']:.2f} EUR")

        y -= 15

    # Total

    y -= 10

    c.setFont("Helvetica-Bold", 10)

    c.drawString(50, y, f"Total: {total:.2f} EUR")

    c.save()

    return pdf_path


# ---------------------------------------------------------------------------

def send_email(pdf_path: str, customer: dict):
    """Send invoice as e-mail attachment. SMTP settings read from env vars."""

    smtp_user = os.getenv("MAIL_USER")

    smtp_pw = os.getenv("MAIL_PW")

    if not smtp_user or not smtp_pw:
        raise RuntimeError("MAIL_USER or MAIL_PW not set in environment")

    host = os.getenv("MAIL_HOST", "smtp.gmail.com")

    port = int(os.getenv("MAIL_PORT", "465"))

    secure = os.getenv("MAIL_SECURE", "SSL").upper()

    # Build message

    msg = EmailMessage()

    msg["Subject"] = f"Invoice #{os.path.basename(pdf_path)} – LiliWelt Academy"

    msg["From"] = f"LiliWelt Academy <{smtp_user}>"

    msg["To"] = customer["email"]

    msg.set_content(

        f"""Hello {customer['name']},

Thank you for your purchase! Your invoice is attached as a PDF.

Best regards,

LiliWelt Team

""")

    with open(pdf_path, "rb") as f:

        msg.add_attachment(f.read(),

                           maintype="application", subtype="pdf",

                           filename=os.path.basename(pdf_path))

    print(f"DEBUG-SMTP ➜ connecting to {host}:{port} ({secure})")

    context = ssl.create_default_context()

    if secure == "SSL":

        with smtplib.SMTP_SSL(host, port, context=context) as s:

            s.login(smtp_user, smtp_pw)

            s.send_message(msg)

    elif secure == "STARTTLS":

        with smtplib.SMTP(host, port) as s:

            s.starttls(context=context)

            s.login(smtp_user, smtp_pw)

            s.send_message(msg)

    else:

        raise ValueError("MAIL_SECURE must be 'SSL' or 'STARTTLS'")

    print("DEBUG-SMTP ✔ message sent to", customer["email"])

