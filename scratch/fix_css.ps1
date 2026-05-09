$content = Get-Content css\city.css -Raw
$pattern = '(?s)max-width: 500px;.*?margin: 0 auto;.*?display: block;.*?\}'
$replacement = 'max-width: 500px;`r`n        margin: 0 auto;`r`n        display: block;`r`n    }`r`n}'
$newContent = $content -replace $pattern, $replacement
Set-Content css\city.css $newContent -NoNewline
