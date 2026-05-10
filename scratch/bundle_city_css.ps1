$files = @(
    "css/globalCss/navbarGlobal.css",
    "css/navbar.css",
    "css/homeNavbar.css",
    "css/common.css",
    "css/city.css",
    "css/service.css",
    "css/homepage.css",
    "css/modal.css",
    "css/footer.css"
)

$outputFile = "css/city-bundle.min.css"
New-Item -Path (Split-Path $outputFile) -ItemType Directory -Force | Out-Null
New-Item -Path $outputFile -ItemType File -Force | Out-Null

foreach ($file in $files) {
    if (Test-Path $file) {
        Write-Host "Adding $file..."
        $filename = Split-Path $file -Leaf
        Add-Content -Path $outputFile -Value "/* === $filename === */"
        $content = [System.IO.File]::ReadAllText((Resolve-Path $file))
        Add-Content -Path $outputFile -Value $content
        Add-Content -Path $outputFile -Value "`n"
    } else {
        Write-Warning "File $file not found!"
    }
}
Write-Host "Successfully created $outputFile"
