import rawpy
from PIL import Image
def convert_cr2_to_png(cr2_path, png_path, z):
      # Открываем CR2-файл с помощью библиотеки rawpy/Opening a CR2 file using the rawpy library
      with rawpy.imread(cr2_path) as raw:
         # Получаем RGB-изображение из RAW-данных/Getting an RGB image from RAW data
         rgb = raw.postprocess()
         # Создаем объект изображения PIL/Create a PIL Image Object
         image = Image.fromarray(rgb)
         # Сохраняем изображение в формате PNG/Save the image in PNG format
         image.save(f'{png_path}\Img_png{z}.png')