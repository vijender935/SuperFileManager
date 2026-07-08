from PIL import Image, ImageFilter


def enhance_image(source, destination):
    try:
        with Image.open(source) as img:

            enhanced = img.filter(ImageFilter.DETAIL)
            enhanced = enhanced.filter(ImageFilter.SHARPEN)

            enhanced.save(destination)

        return True, destination

    except Exception as e:
        return False, str(e)
