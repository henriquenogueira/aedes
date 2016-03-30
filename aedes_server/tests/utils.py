import tempfile

from PIL import Image


def generate_test_image(size=(100, 100), extension='.jpg'):
    '''Generates a random image and creates a physical file for it.'''
    image = Image.new('RGB', size)
    tmp_file = tempfile.NamedTemporaryFile(suffix=extension)
    image.save(tmp_file.name)
    return tmp_file
