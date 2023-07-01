import io
import base64

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas


def graph(image):
    ''' 
    Transform raw numpy image to io.BytesIO for HTML renderization
    '''
    fig, ax = plt.subplots(figsize=(20, 20))
    plt.axis("off")
    plt.imshow(image)

    image_html = io.BytesIO()
    FigureCanvas(fig).print_png(image_html)
    plt.close(fig)
    return image_html
