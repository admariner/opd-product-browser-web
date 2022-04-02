import base64
from browser.models import Gtin, Gtin_img

import os.path

def run():

    #list_gtin = Gtin.objects.filter(GTIN_CD__startswith = '083609')
    list_gtin = Gtin.objects.all().order_by('GTIN_CD')
    img_path_base = 'C:/Users/Philippe/git/opd-product-browser-web/opd/media/gtin/';

    for gtinobj in list_gtin:
        gtin = gtinobj.GTIN_CD
        img_name = f'gtin-{str(gtin)[:3]}/{str(gtin)}.jpg'

        img_path_full = img_path_base + img_name

        if os.path.isfile(img_path_full):
            #with open(img_path_full, "rb") as image_file:
                #filedata = base64.b64encode(image_file.read())
                #filedata = image_file.encode("base64")


            with open(img_path_full,'rb') as f:
                filedata = f.read()
            print(f'{img_name} OK')

            if Gtin_img.objects.filter(pk=str(gtin)).exists():
                current_gtin = Gtin_img.objects.get(pk=str(gtin))
                current_gtin.GTIN_IMG = filedata
                current_gtin.save()
            else:
                new_entry = Gtin_img(GTIN_CD = str(gtin), GTIN_IMG = filedata)
                new_entry.save()


                    #Gtin_img.objects.create(GTIN_CD = str(gtin) , GTIN_IMG = filedata )
        else:
            print(f'{img_name} :(')
