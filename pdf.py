from weasyprint import HTML
import os
from pathlib import Path

def sauve_pdf(html_content, save_directory="export", file_name="export.pdf", titre="exemple", link=""):
    os.makedirs(save_directory, exist_ok=True)
    output_path = os.path.join(save_directory, file_name)

    qrcode_path = Path("qrcode.png").absolute().as_uri()

    # ✅ Header simple en table, prévu pour être capté par element(header)
    header_element = f"""
    <div id="my-header">
      <table style="width:100%; border-collapse:collapse;">
        <tr>
          <td style="width:30px; vertical-align:middle;">
          <a href="{link}">
            <img src="{qrcode_path}" class="qrcode" /></a>
          </td>
          <td style="text-align:left; font-size:20pt; color:#d62828;">
            <strong>Site2wouf.fr</strong><br>
            {titre}
          </td>
        </tr>
      </table>
    </div>
    """

    # ✅ Footer simple
    footer_element = """
    <div id="my-footer">
      <div style="font-size:10pt; text-align:center; color:gray;">
        Page <span class="page-number"></span> / <span class="total-pages"></span><br>
        <a href="https://site2wouf.fr">(C)2019–2025 Wouf Prod</a>
      </div>
    </div>
    """

    # ✅ Full HTML : header + footer attachés via CSS @page
    full_html = f"""
    <html>
    <head>
      <meta charset="utf-8">
      <style>
      img.qrcode {{
  width: 100px !important;
  height: 100px !important;
  object-fit: contain;
}}
        @page {{
          size: A4;
          margin: 50mm 15mm 30mm 15mm;
          @top-center {{
            content: element(header);
          }}
          @bottom-center {{
            content: element(footer);
          }}
        }}

        .page-number::before {{
          content: counter(page);
        }}
        .total-pages::before {{
          content: counter(pages);
        }}
        .page {{
  page-break-after: always;
  page-break-inside: avoid;
}}
.page:last-of-type {{
  page-break-after: auto;
}}


.break-before {{
  break-before: page;
}}

.section.break {{
  page-break-before: always;
}}
        body {{
          font-family: Arial, sans-serif;
          margin: 0;
        }}

        #my-header {{
          position: running(header);
        }}

        #my-footer {{
          position: running(footer);
        }}
      </style>
    </head>
    <body>
      {header_element}
      {footer_element}
      <main>
        {html_content}
      </main>
    </body>
    </html>
    """

    HTML(string=full_html).write_pdf(output_path)

def lit_div_html(fichier="index.html"):
    with open(fichier, "r", encoding='utf-8') as f:
        contenu = f.read()
    return contenu

sauve_pdf(lit_div_html(),titre="Nombres décimaux et opérations",link="""https://site2wouf.fr/decimaux&operations.php""")