import os
import re
from bs4 import BeautifulSoup

for f in os.listdir('.'):
    if not f.endswith('.html'): continue
    with open(f, 'r', encoding='utf-8') as file:
        content = file.read()

    # Fast regex replace to just kill the figure tag's class but keep the tag itself
    content = content.replace('class="wpb_wrapper vc_figure"', 'class="my-4"')
    content = re.sub(r'class="vc_single_image-wrapper[^"]*"', '', content)
    content = content.replace('class="vc_single_image-img attachment-full"', 'class="rounded-xl shadow-lg"')
    content = content.replace('class="vc_single_image-img attachment-medium"', 'class="rounded-xl shadow-lg"')
    content = content.replace('class="vc_single_image-img attachment-large"', 'class="rounded-xl shadow-lg"')

    # Make sure we didn't leave any other wp_ / vc_ classes
    content = re.sub(r'class="vc_[^"]*"', '', content)
    content = re.sub(r'class="wpb_[^"]*"', '', content)

    with open(f, 'w', encoding='utf-8') as out:
        out.write(content)
