from pyzbar import pyzbar
from pyzbar.pyzbar_error import PyZbarError
from PIL import Image


class BarcodeDecoder:

    @staticmethod
    def decode_barcode_png(path_to_png: str) -> str:
        """
        Decode barcode in picture. If there is none barcode in picture or picture format is wrong
        returning empty string
        :param path_to_png: path to picture with barcode
        :return: str value of barcode or empty str
        """

        try:
            decoded_barcode = pyzbar.decode(Image.open(path_to_png))
            barcode_data = decoded_barcode[0].data.decode()
            return barcode_data
        except PyZbarError:
            return ''

