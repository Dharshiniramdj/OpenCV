from PIL import Image, ImageFilter

img = Image.open(r"C:\PROGRAM\Open CV\Zara_011.jpg")

sharp = img.filter(
    ImageFilter.UnsharpMask(
        radius=3,
        percent=200,
        threshold=5
    )
)

sharp.show()
