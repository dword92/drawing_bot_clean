import PILasOPENCV as Image
import PILasOPENCV as ImageDraw
import PILasOPENCV as ImageFont2
from PIL import ImageFont
from core.processing import genering
import core.basic
import logging


logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)
roboto_bold = 'font/roboto_bold.ttf'
roboto_regular = 'font/roboto_regular.ttf'


def image_draw(summa, name, surname_initial, phone):
    completed_path = "completed/"
    end_str = 928
    id_transaction, file_name, status_bar_time, date_time, my_name = genering()
    im = Image.open("source/source2.jpg")
    draw = ImageDraw.Draw(im)

    logger.info("Opened image source2.jpg")

    font = ImageFont2.truetype(roboto_bold, 32)
    draw.text((55, 40), status_bar_time, font=font, fill=(72, 72, 72))
    font = ImageFont2.truetype(roboto_bold, 68)
    draw.text((140, 1024), str(summa) + " " + u"\u20B8", font=font, fill=(251, 251, 251))
    font = ImageFont2.truetype(roboto_regular, 37)
    draw.text((140, 772), name.title() + " " + surname_initial.title() + ".", font=font, fill=(72, 72, 72))
    draw.text((140, 814), phone, font=font, fill=(72, 72, 72))
    font = ImageFont.truetype(roboto_regular, 30)
    size = font.getsize(my_name)
    size = size[0]
    result = (end_str - size)
    font = ImageFont2.truetype(roboto_regular, 29)
    draw.text((result + 3, 1520), my_name, font=font, fill=(72, 72, 72))
    font = ImageFont.truetype(roboto_regular, 30)
    size = font.getsize(date_time)
    size = size[0]
    result = (end_str - size)
    font = ImageFont2.truetype(roboto_regular, 29)
    draw.text((result, 1316), date_time, font=font, fill=(72, 72, 72))
    font = ImageFont2.truetype(roboto_regular, 30)
    draw.text((736, 1212), str(id_transaction), font=font, fill=(72, 72, 72))
    output_filename = f'{completed_path}{file_name}.jpg'
    im.save(output_filename)

    logger.info("Image saved successfully: %s", output_filename)

    core.basic.put = output_filename
