"""Render and check the candidate using installed Chrome, without extra Python packages."""
from pathlib import Path
import html
import json
import os
import re
import subprocess
import uuid

HERE = Path(__file__).resolve().parent
chrome = Path(os.environ.get('PROGRAMFILES', 'C:/Program Files')) / 'Google/Chrome/Application/chrome.exe'
scratch = HERE / 'build'
scratch.mkdir(exist_ok=True)
result = subprocess.run([
    str(chrome), '--headless=new', '--disable-gpu', '--no-first-run', '--no-default-browser-check',
    '--hide-scrollbars', '--force-device-scale-factor=1', '--window-size=1280,720',
    '--user-data-dir=' + str(scratch / ('render-' + uuid.uuid4().hex[:8])),
    '--screenshot=' + str(HERE / 'Axis.png'), '--dump-dom', '--virtual-time-budget=2000',
    (HERE / 'Axis.html').as_uri(),
], capture_output=True, timeout=45, creationflags=getattr(subprocess, 'CREATE_NO_WINDOW', 0))
dom = result.stdout.decode('utf-8', errors='replace')
(scratch / 'qa.html').write_text(dom, encoding='utf-8')
match = re.search(r'data-layout-check="([^"]*)"', dom)
if result.returncode or not match:
    raise RuntimeError('Chrome did not return layout results: ' + result.stderr.decode('utf-8', errors='replace')[-1800:])
check = json.loads(html.unescape(match.group(1)))
print(json.dumps(check))
assert check['fontLoaded'], 'Deck font did not load'
assert check['width'] == 1280 and check['height'] == 720, 'Unexpected canvas size'
assert not check['outside'], 'Content outside slide: ' + repr(check['outside'])
source = (HERE / 'slide.html').read_text(encoding='utf-8')
spoken = source.split('FAHTAI:', 1)[1].split('[Notes:', 1)[0]
print('Spoken words:', len(spoken.split()))
print('Rendered and checked', HERE / 'Axis.png')
