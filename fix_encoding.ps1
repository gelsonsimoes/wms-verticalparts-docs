# ═══════════════════════════════════════════════════════════════
#  SCRIPT DE CORREÇÃO DE LINKS E ENCODING EM ARQUIVOS EXISTENTES
# ═══════════════════════════════════════════════════════════════

$baseDir = $PSScriptRoot
if (-not $baseDir) { $baseDir = Get-Location }

$utf8NoBom = New-Object System.Text.UTF8Encoding $false

$files = Get-ChildItem -Path $baseDir -Filter *.html -Recurse

foreach ($file in $files) {
    $content = Get-Content -Path $file.FullName -Raw -Encoding UTF8
    
    # Substituir link do GitHub pelo Site Oficial
    $content = $content -replace '<a href="https://github.com/gelsonsimoes/wms-verticalparts" target="_blank">GitHub</a>', '<a href="https://www.wmsverticalparts.com.br" target="_blank">Site Oficial</a>'
    $content = $content -replace '<a href="https://github.com/gelsonsimoes/wms-verticalparts" target="_blank">GitHub Web</a>', '<a href="https://www.wmsverticalparts.com.br" target="_blank">Site Oficial</a>'
    
    # Garantir que o link no footer também mude (caso exista algum diferente)
    $content = $content -replace 'GitHub Web', 'Site Oficial'
    
    # Salvar com UTF-8 SEM BOM para limpar os caracteres estranhos
    [System.IO.File]::WriteAllText($file.FullName, $content, $utf8NoBom)
    Write-Host "✅ Corrigido: $($file.FullName)" -ForegroundColor Green
}
