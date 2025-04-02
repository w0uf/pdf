import fitz  # PyMuPDF

# Charger le fichier PDF
pdf_path = "export/export.pdf"
output_svg_path = "export/export.svg"
doc = fitz.open(pdf_path)

# Début du SVG
svg_header = '<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" width="100%" height="100%" viewBox="0 0 595 842">\n'
svg_footer = '</svg>\n'

svg_content = [svg_header]

# Parcourir chaque page et ajouter dans un calque
for page_number in range(len(doc)):
    page = doc[page_number]
    svg_layer = f'<g id="page_{page_number + 1}">\n'
    svg_layer += page.get_svg_image()  # Extraire le contenu SVG de la page
    svg_layer += '\n</g>\n'
    svg_content.append(svg_layer)

# Ajout du pied de fichier SVG
svg_content.append(svg_footer)

# Sauvegarder le fichier SVG unique avec tous les calques
with open(output_svg_path, "w", encoding="utf-8") as svg_file:
    svg_file.writelines(svg_content)

print(f"Fichier SVG généré avec toutes les pages en calques : {output_svg_path}")
