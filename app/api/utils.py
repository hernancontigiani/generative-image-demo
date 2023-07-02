import io
import base64
from PIL import Image

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas

def create_stream(image_data):
    ''' 
    Transform raw numpy image to io.BytesIO stream for HTML renderization
    '''
    image = Image.fromarray(image_data)
    # image = Image.open("pokemon.jpg")  # mock

    # Create stream buffer
    stream = io.BytesIO()

    # Save image as JPG inside stream
    image.save(stream, format="JPEG")

    stream.seek(0)
    return stream

