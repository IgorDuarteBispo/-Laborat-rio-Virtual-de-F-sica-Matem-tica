import zipfile, os
zip_name = "Laboratorio_Fisica_Matematica_Frontend.zip"
with zipfile.ZipFile(zip_name, 'w', zipfile.ZIP_DEFLATED) as zipf:
    zipf.write("index.html")
    zipf.write("style.css")
    zipf.write("app.js")
print(f"📦 ZIP criado: {zip_name} - {os.path.getsize(zip_name)} bytes")