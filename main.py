import os
import sys

import polars
import numpy as np

import gradio as gr
import pytesseract
from PIL import Image

import easyocr


class ProductCollecter:

    def __init__(self):
        self.reader = easyocr.Reader(['en'])

    @staticmethod
    def convert_image_to_pil(image):
        return Image.fromarray(image)

    @staticmethod
    def convert_image_to_array(image):
        return np.array(image)

    def ocr_image(self, image):
        image = self.convert_image_to_array(image)
        results = []
        for detection in self.reader.readtext(image):
            results.append(detection[1])
        return results


if __name__ == "__main__":
    pc = ProductCollecter()
    gr_interface = gr.Interface(fn=pc.ocr_image, inputs="image", outputs="text")
    gr_interface.launch(share=True)
