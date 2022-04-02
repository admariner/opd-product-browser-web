import os.path

from browser.models import Gtin, Gtin_img, Brand, Brand_img

def run():

    #list_gtin = Gtin.objects.filter(GTIN_CD__startswith = '083609')
    list_brand = Brand.objects.all().order_by('BSIN')
    img_path_base = 'C:/Users/Philippe/media/brand/';

    for brandobj in list_brand:
        bsin = brandobj.BSIN
        img_name = f'{str(bsin)}.jpg'

        img_path_full = img_path_base + img_name

        if os.path.isfile(img_path_full):
            #with open(img_path_full, "rb") as image_file:
                #filedata = base64.b64encode(image_file.read())
                #filedata = image_file.encode("base64")

            with open(img_path_full,'rb') as f:
                filedata = f.read()
            print(f'{img_name} OK')

            if Brand_img.objects.filter(pk=str(bsin)).exists():
                current_bsin = Brand_img.objects.get(pk=str(bsin))
                current_bsin.BSIN_IMG = filedata
                current_bsin.save()
            else:
                new_entry = Brand_img(BSIN = str(bsin), BSIN_IMG = filedata)
                new_entry.save()


                    #Gtin_img.objects.create(GTIN_CD = str(gtin) , GTIN_IMG = filedata )
        else:
            print(f'{img_name} :({img_path_full}')
