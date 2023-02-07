import fitz
import os
from .barcode_decoder import BarcodeDecoder


class PdfHandler:

    def __init__(self, path_to_file: str):
        self.path_to_file = path_to_file
        self.document_instance = fitz.open(self.path_to_file)
        self.page = self.document_instance.load_page(0)
        self.default_cropbox = (0, 0, 282, 282)
        self.text_dict = self.page.get_text('dict')

    def get_text_params_from_dict(self, block: int, line: int, span: int = 0) -> dict:
        """
        Method taking key's position in document (block, line, span).
        For key default span = 0, for key's value  span = 1
        Returning dict of key parameters like:
        coordinates key in pdf document,
        name of key on this position in document
        key's font
        key's font size

        :param block:
        :param line:
        :param span:
        :return:
        """
        return {'coords':self.text_dict['blocks'][block]['lines'][line]['spans'][span]['bbox'],
                'font': self.text_dict['blocks'][block]['lines'][line]['spans'][span]['font'],
                'font_size': round(self.text_dict['blocks'][block]['lines'][line]['spans'][span]['size'], 1),
                'name': self.text_dict['blocks'][block]['lines'][line]['spans'][span]['text']}

    def get_text_from_page(self) -> dict:
        """
        Method getting all text from pdf document
        Returning dict{key's name : key's value}
        :return:
        """
        self.page.set_cropbox(fitz.Rect(*self.default_cropbox))
        text_string = self.page.get_text('text')
        splited_text = text_string.split('\n')

        # Adding in dict title value
        text_dict = {'title': splited_text[0]}

        # Now other keys
        for i in range(1, len(splited_text) - 1):
            if splited_text[i].find(':', 0, -1) != -1:  # Branch for keys with values
                key, value = splited_text[i].split(":")
                text_dict[key] = value.replace(' ', '')
            elif splited_text[i][-1] == ':':  # Branch for keys without values
                text_dict[splited_text[i]] = ''

        # Value of NOTES is placed in separate form in the end document, so it needs to be added apart
        last_index = len(splited_text)-1
        note_index = splited_text.index('NOTES:')+1
        text_dict['NOTES'] = splited_text[note_index] if note_index < last_index else ''

        return text_dict

    def get_data_from_barcode(self, barcode_coords: tuple[int]) -> str:
        """
        Method getting barcode value from document in given coordinates.
        Returning string value of barcode if it is existing in given coords.
        And empty string if there isn't barcode.
        :param barcode_coords: expected coord of barcode.
        :return:
        """
        self.page.set_cropbox(fitz.Rect(*barcode_coords))
        path_to_dir = os.path.abspath(os.path.dirname(__file__))
        pic_name = 'barcode.png'
        path_to_pic = os.path.join(path_to_dir, pic_name)
        self.page.get_pixmap().save(path_to_pic)
        barcode_data = BarcodeDecoder.decode_barcode_png(path_to_pic)
        if os.path.exists(path_to_pic):
            os.remove(path_to_pic)
        return barcode_data





