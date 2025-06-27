from flask import Blueprint, request, Response, render_template_string
import os, json
from xhtml2pdf import pisa
from io import BytesIO

download_pdf = Blueprint("download_pdf", __name__)

@download_pdf.route("/download-pdf", methods=["GET"])
def generate_pdf():
    email = request.args.get("email")
    if not email:
        return Response("Email parameter is missing", status=400)

    user_dir = os.path.join("static", "user_data", email)

    try:
        with open(os.path.join(user_dir, "step1.json")) as f1:
            step1 = json.load(f1)
        with open(os.path.join(user_dir, "step2.json")) as f2:
            step2 = json.load(f2)
        with open(os.path.join(user_dir, "step3.json")) as f3:
            step3 = json.load(f3)
    except FileNotFoundError:
        return Response("User data incomplete or missing", status=404)

    html_template = """
    <html>
    <head>
        <style>
            body {
                font-family: Helvetica, sans-serif;
                padding: 40px;
                font-size: 14px;
                color: #2c3e50;
            }
            h1 {
                text-align: center;
                font-size: 26px;
                color: #1a1a1a;
                margin-bottom: 40px;
                border-bottom: 2px solid #ddd;
                padding-bottom: 10px;
            }
            h2 {
                font-size: 18px;
                color: #2c3e50;
                margin-top: 30px;
                margin-bottom: 10px;
                border-bottom: 1px solid #ccc;
                padding-bottom: 4px;
            }
            table {
                width: 100%;
                table-layout: fixed;
                border-collapse: collapse;
                margin-top: 10px;
                margin-bottom: 20px;
                word-wrap: break-word;
            }
            th, td {
                border: 1px solid #ddd;
                padding: 10px;
                vertical-align: top;
                word-break: break-word;
            }
            th {
                background-color: #f4f4f4;
                font-weight: bold;
                width: 35%;
            }
            td {
                width: 65%;
            }
        </style>
    </head>
    <body>
        <h1>Capsule Collection Tech Pack</h1>

        <h2>Capsule Summary</h2>
        <table>
            <tr><th>Pieces</th><td>{{ step1.pieces }}</td></tr>
            <tr><th>Types</th><td>{{ ', '.join(step1.types) }}</td></tr>
            <tr><th>Price Range</th><td>{{ step1.priceRange }}</td></tr>
        </table>

        <h2>Brand Inspiration</h2>
        <table>
            <tr><th>Reference Brand</th><td>{{ step2.brand }}</td></tr>
            <tr><th>Style Notes</th><td>{{ step2.styleNotes }}</td></tr>
        </table>

        <h2>Product Details</h2>
        <table>
            <tr><th>Product Type</th><td>{{ step3.productType }}</td></tr>
            <tr><th>Feeling</th><td>{{ step3.feeling or 'None' }}</td></tr>
            <tr><th>Target Price</th><td>${{ step3.targetPrice }}</td></tr>
            <tr><th>Quantity</th><td>{{ step3.quantity }}</td></tr>
            <tr><th>Material</th><td>{{ step3.material }}</td></tr>
            <tr><th>Manufacturing Preference</th><td>{{ step3.manufacturing }}</td></tr>
        </table>
    </body>
    </html>
    """

    rendered_html = render_template_string(
        html_template,
        email=email,
        step1=step1,
        step2=step2,
        step3=step3
    )

    pdf = BytesIO()
    pisa.CreatePDF(rendered_html, dest=pdf)
    pdf.seek(0)

    return Response(
        pdf.read(),
        mimetype="application/pdf",
        headers={"Content-Disposition": f"attachment;filename={email}_techpack.pdf"}
    )
