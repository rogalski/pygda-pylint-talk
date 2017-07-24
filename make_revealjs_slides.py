#!/usr/bin/env python3
from lxml import etree
import xml.dom.minidom

with open('template.html') as fh:
    html_doc = etree.parse(fh, parser=etree.HTMLParser(remove_blank_text=True))

with open('SLIDES.md') as fh:
    slides_content = fh.read().split('\n---\n')

div_slides = html_doc.xpath('//div[@class="slides"]')[0]
div_slides.clear()
div_slides.attrib['class'] = 'slides'
for slide_content in slides_content:
    section = etree.SubElement(div_slides, 'section', {'data-markdown': ''})
    script = etree.SubElement(section, 'script', {'type': 'text/template'})
    script.text = '\n' + slide_content

with open('index.html', 'w') as fh:
    fh.write(etree.tounicode(html_doc, method="html", pretty_print=True).replace('data-markdown=""', 'data-markdown'))
