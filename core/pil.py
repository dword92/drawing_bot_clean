import cv2

font = cv2.FONT_HERSHEY_SIMPLEX
font_scale = 1
thickness = 2
text = "Hello, World!"

# измеряем размер текста
text_size, baseline = cv2.getTextSize(text, font, font_scale, thickness)

print("Ширина текста:", text_size[0], "пикселей")
print("Высота текста:", text_size[1], "пикселей")
