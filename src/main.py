import xml.etree.ElementTree as ElementTree

filename = 'data/kangaroo/annots/00001.xml'

tree = ElementTree.parse(filename)
root = tree.getroot()
print(root)

for box in root.findall('.//bndbox'):
    xmin = int(box.find('xmin').text)
    ymin = int(box.find('ymin').text)
    xmax = int(box.find('xmax').text)
    ymax = int(box.find('ymax').text)
    coors = [xmin, ymin, xmax, ymax]
