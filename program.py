import os
from xml.etree import ElementTree

file_name = 'current-activity.xml'
full_file = os.path.abspath(os.path.join('data', file_name))
print(full_file)

dom = ElementTree.parse(full_file)
print(dom)

activity = dom.findall('channel')

for a in activity:
    title = a.find('title').text
    des = a.find('description').text
    link = a.find('link').text

    print(' * {} [{}] {} '.format(title, des, link))