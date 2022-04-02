from PIL import Image
from browser.models import Gtin, Gtin_img
from io import BytesIO

import os.path

def run():

    gtin = '0004900005539'

    img_path_base = 'C:/Users/Philippe/media/gtin-new/';

    img_name = f'{gtin}.png'



    img_path_full = img_path_base + img_name

    if os.path.isfile(img_path_full):
        print ('------------------START'   )
        image = Image.open(img_path_full)

        THUMBNAIL_SIZE = (150, 150)
        image.thumbnail(THUMBNAIL_SIZE, Image.ANTIALIAS)

        if image.mode not in ('L', 'RGB'):
            image = image.convert('RGB')

        output = BytesIO()
        image.save(output, format='JPEG')
        filedata = output.getvalue()

        #print ('------------------- Content :'  + str(filedata) )

        #THUMBNAIL_SIZE = (150, 150)
        #filedata = image.thumbnail(THUMBNAIL_SIZE, Image.ANTIALIAS)

        #f = open(img_path_full,'rb')
        #filedata = f.read()
        #f.close()

        if Gtin_img.objects.filter(pk=gtin).exists():
            current_gtin = Gtin_img.objects.get(pk=gtin)
            current_gtin.GTIN_IMG = filedata
            current_gtin.save()
        else:
            new_entry = Gtin_img(GTIN_CD =  gtin, GTIN_IMG = filedata)
            new_entry.save()

        print(f'{img_name} OK')
    else:

        print(f'{img_name} KO')
