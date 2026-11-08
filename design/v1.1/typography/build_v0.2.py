#!/usr/bin/env python3
"""Reproduce VICENSAE Typefaces v0.2 from local SIL OFL Noto fonts.
Requires fonttools[woff], brotli, and locally installed Noto TTFs.
Review source licenses, reserved names, spacing and glyphs before release.
"""
from pathlib import Path
from fontTools.ttLib import TTFont
import argparse, hashlib, json

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("--noto-dir",required=True,help="Directory containing NotoSans-{Light,Regular,Bold}.ttf, NotoSerif-..., NotoSansMono-...")
    ap.add_argument("--out",default="dist")
    args=ap.parse_args()
    src=Path(args.noto_dir)
    out=Path(args.out)
    out.mkdir(parents=True,exist_ok=True)
    specs={"UI":("NotoSans",1.015,8),"Text":("NotoSans",1.045,16),"Display":("NotoSerif",.95,4),"Mono":("NotoSansMono",1.,0),"Canon":("NotoSerif",1.08,14)}
    weights={"Light":300,"Regular":400,"Bold":700}
    files=[]
    for family,(base,scale,tracking) in specs.items():
        for style,weight in weights.items():
            source=src/f"{base}-{style}.ttf"
            if not source.is_file():
                raise FileNotFoundError(source)
            font=TTFont(source)
            for glyph,(advance,lsb) in list(font["hmtx"].metrics.items()):
                font["hmtx"].metrics[glyph]=(advance if family=="Mono" else round(advance*scale+tracking),lsb)
            familyname=f"VICENSAE {family}"
            ps=f"VICENSAE{family}-{style}"
            for rec in font["name"].names:
                if rec.nameID in (1,16): value=familyname
                elif rec.nameID in (2,17): value=style
                elif rec.nameID==4: value=f"{familyname} {style}"
                elif rec.nameID==6: value=ps
                elif rec.nameID==3: value=f"VICENSAE-v0.2-{family}-{style}"
                else: continue
                rec.string=value.encode("utf-16-be") if rec.isUnicode() else value.encode("latin-1","replace")
            font["OS/2"].usWeightClass=weight
            font["OS/2"].fsSelection=(font["OS/2"].fsSelection & ~0x60) | (0x20 if weight==700 else 0x40 if weight==400 else 0)
            font["head"].macStyle=1 if weight==700 else 0
            for fmt in ("ttf","woff2"):
                font.flavor="woff2" if fmt=="woff2" else None
                dest=out/f"{ps}.{fmt}"
                font.save(dest)
                files.append({"path":dest.name,"source":source.name,"bytes":dest.stat().st_size,"sha256":hashlib.sha256(dest.read_bytes()).hexdigest()})
            font.close()
    (out/"MANIFEST.json").write_text(json.dumps({"status":"OFL_DERIVATIVE_PROTOTYPE","files":files},indent=2)+"\n",encoding="utf-8")
    print(f"Built {len(files)} files in {out}")

if __name__=="__main__":
    main()
