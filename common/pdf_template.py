

class PdfTemplate:

    title: dict = {'coords': (6.005304336547852, 6.250148773193359, 184.74594116210938, 17.99098777770996),
                   'font': 'Arial-BoldMT',
                   'font_size': 10.5,
                   'name': 'GRIFFON AVIATION SERVICES LLC',
                   'block': 0,
                   'line': 0}

    pn_barcode: dict = {'coords': (0, 17, 270, 40)}

    qty_barcode: dict = {'coords': (10, 153, 93, 186)}

    pn: dict = {'coords': (13.511934280395508, 41.24687957763672, 37.78092956542969, 49.63319396972656),
                'font': 'Arial-BoldMT',
                'font_size': 7.5,
                'name': 'PN:',
                'block': 1,
                'line': 0}

    sn:  dict = {'coords': (141.49998474121094, 41.24687957763672, 156.3468475341797, 49.63319396972656),
                 'font': 'Arial-BoldMT',
                 'font_size': 7.5,
                 'name': 'SN:',
                 'block': 1,
                 'line': 1}

    description: dict = {'coords': (13.511934280395508, 52.50682830810547, 69.64525604248047, 60.89313888549805),
                         'font': 'Arial-BoldMT',
                         'font_size': 7.5,
                         'name': 'DESCRIPTION:',
                         'block': 2,
                         'line': 0}

    location: dict = {'coords': (13.511934280395508, 63.76676940917969, 56.13331985473633, 72.15308380126953),
                      'font': 'Arial-BoldMT',
                      'font_size': 7.5,
                      'name': 'LOCATION:',
                      'block': 2,
                      'line': 1}

    condition: dict = {'coords': (141.49998474121094, 63.76676940917969, 187.87469482421875, 72.15308380126953),
                       'font': 'Arial-BoldMT',
                       'font_size': 7.5,
                       'name': 'CONDITION:',
                       'block': 2,
                       'line': 2}

    receiver: dict = {'coords': (13.511934280395508, 75.02671813964844, 61.387962341308594, 83.41303253173828),
                      'font': 'Arial-BoldMT',
                      'font_size': 7.5,
                      'name': 'RECEIVER#: ',
                      'block': 3,
                      'line': 0}

    uom: dict = {'coords': (141.49998474121094, 75.02671813964844, 163.10281372070312, 83.41303253173828),
                 'font': 'Arial-BoldMT',
                 'font_size': 7.5,
                 'name': 'UOM:',
                 'block': 3,
                 'line': 1}

    exp_date: dict = {'coords': (13.511934280395508, 86.28665924072266, 55.382659912109375, 94.6729736328125),
                      'font': 'Arial-BoldMT',
                      'font_size': 7.5,
                      'name': 'EXP DATE: ',
                      'block': 4,
                      'line': 0}

    po: dict = {'coords': (141.49998474121094, 86.28665924072266, 157.09750366210938, 94.6729736328125),
                'font': 'Arial-BoldMT',
                'font_size': 7.5,
                'name': 'PO:',
                'block': 4,
                'line': 1}

    cert_source: dict = {'coords': (13.511934280395508, 97.5466079711914, 72.64790344238281, 105.93292236328125),
                         'font': 'Arial-BoldMT',
                         'font_size': 7.5,
                         'name': 'CERT SOURCE: ',
                         'block': 5,
                         'line': 0}

    rec_date: dict = {'coords': (13.511934280395508, 108.80655670166016, 55.382659912109375, 117.19287109375),
                      'font': 'Arial-BoldMT',
                      'font_size': 7.5,
                      'name': 'REC.DATE:',
                      'block': 6,
                      'line': 0}

    mfg: dict = {'coords': (141.49998474121094, 108.80655670166016, 162.35214233398438, 117.19287109375),
                 'font': 'Arial-BoldMT',
                 'font_size': 7.5,
                 'name': 'MFG: ',
                 'block': 6,
                 'line': 1}

    batch: dict = {'coords': (13.511934280395508, 120.06649780273438, 49.37735366821289, 128.45281982421875),
                   'font': 'Arial-BoldMT',
                   'font_size': 7.5,
                   'name': 'BATCH# : ',
                   'block': 7,
                   'line': 0}

    dom: dict = {'coords': (141.49998474121094, 120.06649780273438, 163.10281372070312, 128.45281982421875),
                 'font': 'Arial-BoldMT',
                 'font_size': 7.5,
                 'name': 'DOM:',
                 'block': 7,
                 'line': 1}

    remark: dict = {'coords': (13.511934280395508, 131.32644653320312, 48.29021453857422, 139.71275329589844),
                    'font': 'Arial-BoldMT',
                    'font_size': 7.5,
                    'name': 'REMARK:',
                    'block': 8,
                    'line': 0}

    lot: dict = {'coords': (141.49998474121094, 131.32644653320312, 167.60678100585938, 139.71275329589844),
                 'font': 'Arial-BoldMT',
                 'font_size': 7.5,
                 'name': 'LOT# : ',
                 'block': 8,
                 'line': 1}

    tagged_by: dict = {'coords': (13.511934280395508, 142.58639526367188, 61.387962341308594, 150.9727020263672),
                       'font': 'Arial-BoldMT',
                       'font_size': 7.5,
                       'name': 'TAGGED BY: ',
                       'block': 9,
                       'line': 0}

    qty: dict = {'coords': (17.265249252319336, 186.87551879882812, 37.95466995239258, 195.26182556152344),
                 'font': 'ArialMT',
                 'font_size': 7.5,
                 'name': 'Qty:',
                 'block': 11,
                 'line': 0}

    notes: dict = {'coords': (141.49998474121094, 142.58639526367188, 170.27296447753906, 150.9727020263672),
                   'font': 'Arial-BoldMT',
                   'font_size': 7.5,
                   'name': 'NOTES:',
                   'block': 12,
                   'line': 0}

    REQUIREMENT_TEXT_PARAMS = [title, pn, sn, description, location, condition, receiver, uom, exp_date, po,
                               cert_source, rec_date, mfg, batch, dom, remark, lot, tagged_by, qty, notes]


















