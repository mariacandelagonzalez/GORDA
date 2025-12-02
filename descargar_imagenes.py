import urllib.request
import os

# Directorio donde guardar las imágenes
img_dir = r"c:\Users\Estudiante\Desktop\amor2\img"

# URLs de imágenes de Unsplash (relevantes para cada escena del cómic)
urls = {
    "comic1.png": "https://images.unsplash.com/photo-1529156069898-49953e39b3ac?w=600&h=400&fit=crop",  # Miradas/Encuentro
    "comic2.png": "https://images.unsplash.com/photo-1552821081-f9d737ae5a4f?w=600&h=400&fit=crop",  # Personas en bici
    "comic3.png": "https://images.unsplash.com/photo-1611262588024-d12430b98920?w=600&h=400&fit=crop",  # Redes sociales
    "comic4.png": "https://images.unsplash.com/photo-1489992257199-12e17278b374?w=600&h=400&fit=crop",  # Noche en plaza
    "comic5.png": "https://images.unsplash.com/photo-1544078751-58fee2d8a03b?w=600&h=400&fit=crop",  # Encuentro frío
    "comic6.png": "https://images.unsplash.com/photo-1515395377452-f1e0987861d7?w=600&h=400&fit=crop",  # Beso tímido
    "comic7.png": "https://images.unsplash.com/photo-1537081143476-4c5b1fe40d5e?w=600&h=400&fit=crop",  # Primer beso
    "comic8.png": "https://images.unsplash.com/photo-1516534775068-bb55e323e406?w=600&h=400&fit=crop",  # Momentos juntas
    "comic9.png": "https://images.unsplash.com/photo-1594515621513-43e910f0628f?w=600&h=400&fit=crop",  # Proposición
    "comic10.png": "https://images.unsplash.com/photo-1508003516284-37f168a93f0d?w=600&h=400&fit=crop"  # Amor
}

print("Descargando imágenes para el cómic...")
print("-" * 50)

for filename, url in urls.items():
    filepath = os.path.join(img_dir, filename)
    try:
        print(f"Descargando {filename}...", end=" ")
        urllib.request.urlretrieve(url, filepath)
        file_size = os.path.getsize(filepath)
        print(f"✓ OK ({file_size} bytes)")
    except Exception as e:
        print(f"✗ Error: {str(e)}")

print("-" * 50)
print("¡Descarga completada!")

# Verificar archivos descargados
print("\nArchivos en la carpeta img:")
for file in os.listdir(img_dir):
    if file.startswith("comic") and file.endswith(".png"):
        size = os.path.getsize(os.path.join(img_dir, file))
        print(f"  ✓ {file} - {size} bytes")
