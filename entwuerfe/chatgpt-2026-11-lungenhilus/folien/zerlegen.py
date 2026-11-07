from PIL import Image, ImageDraw, ImageFont, ImageFilter
import numpy as np, os
D=os.path.dirname(os.path.abspath(__file__))
src=Image.open('/mnt/user-data/attachments/b2aa2457-44e0-5bd9-8541-10933726e0e5/2c8a1e24-image.png').convert('RGB')
a=np.asarray(src).astype(int)
# Fix typo: lines 3+4 neu setzen
fo=ImageFont.truetype('/usr/share/fonts/opentype/noto/NotoSansCJK-Bold.ttc',21)
# baseline of original line 1 (no descender except g): find bottom of 'D' column
fix=src.copy(); d=ImageDraw.Draw(fix)
rng=np.random.default_rng(1)
patch=np.clip(rng.normal(250,1.2,(54,204,3)),0,255).astype('uint8')
fix.paste(Image.fromarray(patch),(40,295))
def bl(y0,y1,txt):  # align glyph-box top of capital/ascender to y0
    t=fo.getbbox(txt)[1]; return y0-t
F4=ImageFont.truetype('/usr/share/fonts/opentype/noto/NotoSansCJK-Medium.ttc',84)
def zeile(txt,ytop,x=41):
    L=Image.new('L',(900,140),0); dd=ImageDraw.Draw(L)
    bb=F4.getbbox(txt,stroke_width=1); dd.text((-bb[0],-bb[1]),txt,font=F4,fill=255,stroke_width=1,stroke_fill=255)
    rb=F4.getbbox('Der Lungenhilus ist',stroke_width=1); k=186/(rb[2]-rb[0])
    m=L.resize((round(900*k),round(140*k)),Image.LANCZOS)
    fix.paste(Image.new('RGB',m.size,(28,29,32)),(x,ytop),m)
zeile('an der Innenseite',297); zeile('jeder Lunge.',325)
# minimal weichzeichnen der neuen Zeilen, damit sie zur Bildschärfe passen
reg=fix.crop((40,295,244,349)).filter(ImageFilter.GaussianBlur(0.2)); fix.paste(reg,(40,295))
fix.crop((0,200,627,380)).resize((1254,360)).save(os.path.join(D,'zoom_fix.png'))
# 4 Quadranten -> 1080x1080 (Gitter bei x/y ~ 622-631 / 590-598)
boxes=[(0,0,621,589),(632,0,1254,589),(0,600,621,1254),(632,600,1254,1254)]
names=['folie1_lungenhilus','folie2_was_verlaeuft_im_hilus','folie3_lage_und_bedeutung','folie4_lumen']
for b,n in zip(boxes,names):
    q=fix.crop(b); w,h=q.size; s=max(w,h)
    bgc=tuple(int(x) for x in np.asarray(q)[:6,:6].reshape(-1,3).mean(0))
    c=Image.new('RGB',(s,s),bgc); c.paste(q,((s-w)//2,(s-h)//2))
    c.resize((1080,1080),Image.LANCZOS).save(os.path.join(D,n+'.png')); print(n,b,q.size,bgc)
