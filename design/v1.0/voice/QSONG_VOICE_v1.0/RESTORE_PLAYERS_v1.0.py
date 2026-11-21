"""Restore byte-identical archived players and their embedded audio."""
import base64, hashlib, re
from pathlib import Path
root=Path(__file__).resolve().parent/'history'
base='QSONG_VICENSAE_EL_PORVENIR_NO_ESTA_ESCRITO_'
spec=[
 ('v0.1',6,'1cb41381b60460a121e11e0f5c7b610ba8774f0be2b3d481a05e5bcc17bf7e7b','2e4e38c467bdb2bf80e36888eafbd54e9b34fdd2505377ad5ea28fea6b996a56'),
 ('v0.2_CANTADA',8,'459557440f730fc5fd6a38a34cb2a52c6a8362bd64915ee3d5e8323ca8274129','008e1803f4a96ddaca4471c8a5b1d418cf1a11298379507cdc9f5fa4c321272f')]
def safe_write(p,b,expected):
    if hashlib.sha256(b).hexdigest()!=expected: raise ValueError(f'Hash mismatch {p}')
    if p.exists() and p.read_bytes()!=b: raise FileExistsError(p)
    p.write_bytes(b)
for v,n,hsha,asha in spec:
    chunks=root/'html-parts'/v
    h=b''.join((chunks/f'part-{i:03}.txt').read_bytes() for i in range(n))
    safe_write(root/(base+v+'.html'),h,hsha)
    audio=base64.b64decode(re.search(rb'data:audio/[^;]+;base64,([A-Za-z0-9+/=]+)',h)[1],validate=True)
    safe_write(root/(base+v+'.mp3'),audio,asha)
    print(v,'verified and restored')
