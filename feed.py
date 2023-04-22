import yaml
import xml.etree.ElementTree as ET

# Load feed.yaml file
with open('feed.yaml', 'r') as f:
    data = yaml.safe_load(f)

# Create XML tree
rss = ET.Element('rss', {'version': '2.0',
                         'xmlns:itunes': 'http://www.itunes.com/dtds/podcast-1.0.dtd',
                         'xmlns:content': 'http://purl.org/rss/1.0/modules/content/'})
channel = ET.SubElement(rss, 'channel')
ET.SubElement(channel, 'title').text = data['title']
ET.SubElement(channel, 'language').text = 'en-us'
ET.SubElement(channel, 'category').text = data['category']
ET.SubElement(channel, 'description').text = data['description']
ET.SubElement(channel, 'image', {'href': data['image']})
for item in data['item']:
    item_elem = ET.SubElement(channel, 'item')
    ET.SubElement(item_elem, 'title').text = item['title']
    ET.SubElement(item_elem, 'description').text = item['description']
    ET.SubElement(item_elem, 'pubDate').text = item['published']
    enclosure = ET.SubElement(item_elem, 'enclosure', {
        'url': 'https://example.com/' + item['file'],
        'type': 'audio/mpeg',
        'length': '0'
    })

# Write XML tree to file
tree = ET.ElementTree(rss)
tree.write('podcast.xml', encoding='UTF-8', xml_declaration=True)
