# PowerPoint's own step for round2/make_pptx.py: open the generated deck read-only, export each slide as a PNG (for
# checking against the HTML), and, with -Out, save a copy with the TrueType fonts embedded (Plus Jakarta Sans must be
# installed for the user). make_pptx.py then rewrites the copy's metadata: saving here stamps the signed-in account.
param([string]$In, [string]$Out = "", [string]$PngDir = "")
$ErrorActionPreference = "Stop"
$pp = New-Object -ComObject PowerPoint.Application
try {
  $pres = $pp.Presentations.Open($In, -1, 0, 0)          # ReadOnly, not Untitled, no window
  if ($PngDir) {
    New-Item -ItemType Directory -Force $PngDir | Out-Null
    $i = 1
    foreach ($s in $pres.Slides) { $s.Export((Join-Path $PngDir ("ppt-{0:D2}.png" -f $i)), "PNG", 1920, 1080); $i++ }
    "exported $($i - 1) slides from PowerPoint"
  }
  if ($Out) {
    try { $pres.RemoveDocumentInformation(4) } catch { "note: personal-information removal not available here" }
    $pres.SaveAs($Out, 24, -1)                             # ppSaveAsOpenXMLPresentation, EmbedTrueTypeFonts
    "saved with fonts embedded: $Out"
  }
  $pres.Close()
} finally {
  $pp.Quit()
  [System.Runtime.Interopservices.Marshal]::ReleaseComObject($pp) | Out-Null
}
