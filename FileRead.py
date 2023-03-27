import xml.etree.ElementTree as ET
import os
c = input('Enter s to search for a word. Enter q to quit:')
while(1):
  if(c == 's'):
    number = 0
    keyword = input('Enter the word to search for: ')
    path = input('Enter directory: ')
    for filename in os.listdir(path):
        if not filename.endswith('.xml'): continue
        fullname = os.path.join(path, filename)
        tree = ET.parse(fullname)
        root = tree.getroot()
        for x in root.findall('object'):
          name = x.find('name').text
          if(name == keyword):
            number = number + 1

    print('There were',number,'occurrences of the word',keyword,'found.')
    c = input('Enter s to search for a word. Enter q to quit:')
  else: 
    break
    
print("Goodbye!")


