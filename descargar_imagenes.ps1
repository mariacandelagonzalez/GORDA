$urls = @(
    @{nombre = "comic1.png"; url = "https://images.unsplash.com/photo-1529156069898-49953e39b3ac?w=600&h=400&fit=crop"},
    @{nombre = "comic2.png"; url = "https://images.unsplash.com/photo-1552821081-f9d737ae5a4f?w=600&h=400&fit=crop"},
    @{nombre = "comic3.png"; url = "https://images.unsplash.com/photo-1611262588024-d12430b98920?w=600&h=400&fit=crop"},
    @{nombre = "comic4.png"; url = "https://images.unsplash.com/photo-1489992257199-12e17278b374?w=600&h=400&fit=crop"},
    @{nombre = "comic5.png"; url = "https://images.unsplash.com/photo-1544078751-58fee2d8a03b?w=600&h=400&fit=crop"},
    @{nombre = "comic6.png"; url = "https://images.unsplash.com/photo-1515395377452-f1e0987861d7?w=600&h=400&fit=crop"},
    @{nombre = "comic7.png"; url = "https://images.unsplash.com/photo-1537081143476-4c5b1fe40d5e?w=600&h=400&fit=crop"},
    @{nombre = "comic8.png"; url = "https://images.unsplash.com/photo-1516534775068-bb55e323e406?w=600&h=400&fit=crop"},
    @{nombre = "comic9.png"; url = "https://images.unsplash.com/photo-1594515621513-43e910f0628f?w=600&h=400&fit=crop"},
    @{nombre = "comic10.png"; url = "https://images.unsplash.com/photo-1508003516284-37f168a93f0d?w=600&h=400&fit=crop"}
)

$dir = "c:\Users\Estudiante\Desktop\amor2\img"
Write-Host "Descargando imágenes para el cómic..." -ForegroundColor Green
Write-Host "--------------------------------------------"

foreach ($item in $urls) {
    $path = Join-Path $dir $item.nombre
    Write-Host "Descargando $($item.nombre)..." -NoNewline
    try {
        Invoke-WebRequest -Uri $item.url -OutFile $path -ErrorAction Stop
        $size = (Get-Item $path).Length
        Write-Host " OK ($size bytes)" -ForegroundColor Green
    } catch {
        Write-Host " ERROR" -ForegroundColor Red
    }
}

Write-Host "--------------------------------------------"
Write-Host "¡Descarga completada!" -ForegroundColor Green
