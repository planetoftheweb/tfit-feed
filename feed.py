import yaml
import xml.etree.ElementTree as ET

with open('feed.yaml', 'r') as f:
    data = yaml.safe_load(f)

rss = ET.Element('rss', {'version': '2.0',
                         'xmlns:itunes': 'http://www.itunes.com/dtds/podcast-1.0.dtd',
                         'xmlns:content': 'http://purl.org/rss/1.0/modules/content/'})
channel = ET.SubElement(rss, 'channel')
link = ET.SubElement(channel, 'link').text = data['link']
format = ET.SubElement(channel, 'format').text = data['format']
ET.SubElement(channel, 'title').text = data['title']
ET.SubElement(channel, 'subtitle').text = data['subtitle']
ET.SubElement(channel, 'description').text = data['description']
ET.SubElement(channel, 'itunes:image', {'href': link + data['image']})
ET.SubElement(channel, 'language').text = data['language']
category = ET.SubElement(channel, 'itunes:category', {'text': data['category']})
ET.SubElement(channel, 'link').text = link
ET.SubElement(channel, 'author').text = data['author']
for item in data['item']:
    item_elem = ET.SubElement(channel, 'item')
    ET.SubElement(item_elem, 'title').text = item['title']
    ET.SubElement(item_elem, 'description').text = item['description']
    ET.SubElement(item_elem, 'itunes:duration').text = item['duration']
    ET.SubElement(item_elem, 'pubDate').text = item['published']
    enclosure = ET.SubElement(item_elem, 'enclosure', {
        'url': link + item['file'],
        'type': format,
        'length': item['length']
    })

# Write XML tree to file
tree = ET.ElementTree(rss)
tree.write('podcast.xml', encoding='UTF-8', xml_declaration=True)
