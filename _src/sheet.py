import sys,glob,re
from PIL import Image
name=sys.argv[1]; per=int(sys.argv[2]) if len(sys.argv)>2 else 4
fs=sorted(glob.glob(f'_src/sh_{name}_[0-9]*.png'),key=lambda f:int(re.findall(r'_(\d+)\.png',f)[0]))
for k in range(0,len(fs),per):
    ims=[Image.open(f) for f in fs[k:k+per]]; w,h=ims[0].size; s=0.5 if w>700 else 0.6
    tw,th=int(w*s),int(h*s); cols=2 if w>700 else 4
    rows=(len(ims)+cols-1)//cols
    sh=Image.new('RGB',(tw*cols+10*(cols-1),th*rows+10*(rows-1)),'red')
    for i,im in enumerate(ims): sh.paste(im.resize((tw,th)),((i%cols)*(tw+10),(i//cols)*(th+10)))
    sh.save(f'_src/S_{name}_{k//per}.png'); print(f'_src/S_{name}_{k//per}.png')
