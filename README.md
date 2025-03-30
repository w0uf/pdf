# 📄 HTML to PDF with WeasyPrint

This project automates the generation of PDFs from HTML fragments using **WeasyPrint**, with support for:

- ✅ Custom **header** (including an image)
- ✅ Custom **footer** with page numbers
- ✅ Clean separation of content and layout
- ⚠️ Note: WeasyPrint does **not yet fully support persistent headers** (as xhtml2pdf used to), so this repo includes workarounds

## 🚀 Features

- Simple HTML fragment input
- Adds consistent header and footer
- Image support in the header
- Output ready for printing or archiving

## 🛠️ Requirements

- Python 3.8+
- WeasyPrint
- Flask *(if using the demo app)*

Install dependencies:

```bash
pip install -r requirements.txt
pdf/
├── templates/
│   ├── base.html         # HTML layout with header/footer
│   └── fragment.html     # Your custom content goes here
├── static/
│   └── img/
│       └── logo.png      # Image used in header
├── render.py             # Script to generate the PDF
└── README.md


```markdown
# 📄 HTML vers PDF avec WeasyPrint

Ce projet automatise la génération de fichiers **PDF à partir de fragments HTML**, en utilisant **WeasyPrint**, avec les fonctionnalités suivantes :

- ✅ **En-tête personnalisé** (avec image)
- ✅ **Pied de page** avec numérotation des pages
- ✅ Séparation claire entre le contenu et la mise en forme
- ⚠️ Remarque : WeasyPrint **ne gère pas encore complètement les en-têtes persistants** (comme le faisait xhtml2pdf), donc ce dépôt inclut des contournements.

## 🚀 Fonctionnalités

- Entrée sous forme de fragment HTML
- Ajout automatique d’un en-tête et d’un pied de page
- Support des images dans l’en-tête
- Sortie propre, prête à être imprimée ou archivée

## 🛠️ Prérequis

- Python 3.8+
- WeasyPrint
- Flask *(optionnel pour l’application de démo)*

Installer les dépendances :

```bash
pip install -r requirements.txt

