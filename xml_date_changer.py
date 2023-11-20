import xml.etree.ElementTree as ET
from sys import argv
from os import listdir, path

directory = argv[1]
TAG = 'transfer_lto_date'

def change_xml_value(xml_record):
    print("busy with {}".format(xml_record))
    tree = ET.parse(xml_record)
    root = tree.getroot()
    transfer_date = root.find(TAG)
    print("> wrong {} is {}".format(TAG, transfer_date.text))
    [day, month, year] = transfer_date.text.split('-')
    correct_date = '{}-{}-{}'.format(year, month.zfill(2), day.zfill(2))
    print("> change {} to {}".format(TAG, correct_date))
    transfer_date.text = correct_date
    tree.write(xml_record, encoding="utf-8", xml_declaration=True)
    print("{} DONE".format(xml_record))

for filename in listdir(directory):
    if filename.endswith('.xml') and not filename.startswith('._'):
        change_xml_value(path.join(directory,filename))
