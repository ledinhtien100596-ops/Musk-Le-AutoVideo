"""Materialize pinned upstream source and apply the auditable branding patch."""
from pathlib import Path
import hashlib,tarfile,tempfile,urllib.request,shutil,subprocess,zipfile,os
ROOT=Path(__file__).resolve().parents[1]
URL='https://codeload.github.com/jub0t/Concat/tar.gz/refs/tags/v0.2.7'
SHA='09228e486f19091a84406bf1e473ea686a2921f0585dcf4011a866790f1f9736'
with tempfile.TemporaryDirectory(prefix='muskle-source-') as temp:
 temp=Path(temp);archive=temp/'source.tar.gz'
 print('Downloading Concat v0.2.7 source',flush=True)
 with urllib.request.urlopen(URL,timeout=120) as response,archive.open('wb') as f:shutil.copyfileobj(response,f)
 actual=hashlib.sha256(archive.read_bytes()).hexdigest()
 if actual!=SHA:raise RuntimeError('Upstream archive checksum mismatch: '+actual)
 with tarfile.open(archive) as t:t.extractall(temp/'unpacked',filter='data')
 upstream=temp/'unpacked/Concat-0.2.7'
 for p in upstream.iterdir():
  if p.name in ('.github','.git'):continue
  dst=ROOT/p.name
  if p.is_dir():shutil.copytree(p,dst,dirs_exist_ok=True)
  else:shutil.copy2(p,dst)
 subprocess.run(['git','apply','--check',str(ROOT/'musk/branding.patch')],cwd=ROOT,check=True)
 subprocess.run(['git','apply',str(ROOT/'musk/branding.patch')],cwd=ROOT,check=True)
 for name in ['MUSK_LE_CHANGES.md','BUILD_STATUS.md']:shutil.copy2(ROOT/'musk'/name,ROOT/name)
 subprocess.run(['python','scripts/locales.py','--check'],cwd=ROOT,check=True)
 # Snapshot all corresponding source before dependency downloads/build directories exist.
 files=[p for p in ROOT.rglob('*') if p.is_file() and '.git' not in p.relative_to(ROOT).parts]
 stage=ROOT/'stage';stage.mkdir(exist_ok=True)
 with zipfile.ZipFile(stage/'Musk-Le-AutoVideo-corresponding-source.zip','w',zipfile.ZIP_DEFLATED) as z:
  for p in files:z.write(p,p.relative_to(ROOT))
 print('Verified upstream hash; patch and locale checks passed.',flush=True)
