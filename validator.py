from common import PdfHandler, PdfTemplate
import json


def extracting_data_from_pdf(pdf_handler: PdfHandler) -> dict:
    # Getting all text from pdf doc in dict
    text_dict = pdf_handler.get_text_from_page()

    # Adding barcodes values in dict
    text_dict['PN_BARCODE'] = pdf_handler.get_data_from_barcode(PdfTemplate.pn_barcode['coords'])
    text_dict['QTY_BARCODE'] = pdf_handler.get_data_from_barcode(PdfTemplate.qty_barcode['coords'])
    return text_dict


def params_and_styles_validation(params_list: list, pdf_handler: PdfHandler):
    for param in params_list:
        # Getting key param properties(coords, name, font, font_size) from document dict
        # by expected position (num block and line)
        param_from_pdf = pdf_handler.get_text_params_from_dict(block=param['block'], line=param['line'])

        # Comparing properties with template
        assert param['name'] in param_from_pdf['name'], f'Wrong parameter on position {param["name"]}'
        assert param_from_pdf['coords'] == param['coords'], f"{param['name']} is located on wrong coords"
        assert param_from_pdf['font'] == param['font'], f'Wrong font in parameter {param["name"]}'
        assert param_from_pdf['font_size'] == param['font_size'], f'Wrong font size in parameter {param["name"]}'


if __name__ == '__main__':
    path_to_pdf_file = input('Enter absolute path to pdf file:')

    pdf_hand = PdfHandler(path_to_pdf_file)

    # extracting text and barcode data from pdf to dict
    data_dict = extracting_data_from_pdf(pdf_hand)
    print(f'File contains:\n{json.dumps(data_dict, indent=4)}')

    # Asserting values in barcodes
    assert data_dict['PN_BARCODE'] == data_dict['PN'], f"Wrong value {data_dict['PN_BARCODE']} in PN barcode"
    assert data_dict['QTY_BARCODE'] == data_dict['Qty'], f"Wrong value {data_dict['QTY_BARCODE']} in Qty barcode"

    # Asserting document structure and styles
    params_and_styles_validation(PdfTemplate.REQUIREMENT_TEXT_PARAMS, pdf_hand)

    print('Congratulations! PDF file is correct')

