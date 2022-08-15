import glob
import os
import re

folders = ['Android', 'iOS', 'Flutter', 'React-Native', 'Xamarin']
languages = ['en', 'nl']

# Read all text from a file
def read_file(file):
    print('Reading file {}'.format(file))
    text = None
    with open(file, encoding='utf-8') as f:
        text = f.read()
        # Increase heading 2 and higher by one.
        text = re.sub('(##+ [\w]+)', '#\\1', text)
    return text

# Write text to a file
def write_file(file, text, mode):
    print('Writing to file {}'.format(file))
    with open(file, mode, encoding='utf-8') as f:
        f.write(text)

# Write techniques to a file
def write_techniques(folder, language, file):       
    text = read_file(file)
    file_name = os.path.basename(file)
    file_out = 'Techniques/{}/{}'.format(language, file_name)
    list = text.split('\n')
    mode = 'w'
    insert = 1
    if os.path.exists(file_out):
        list.pop(0)
        mode = 'a'
        insert = 0

    language = folder.replace('-', ' ')
    list.insert(insert, '\n## {}'.format(language))
    text = '\n'.join(list)
    write_file(file_out, text, mode)

# For each folder, for each language, join code examples into one file
for folder in folders:
    for language in languages:
        # Make directories to put the files in
        os.makedirs('Techniques/{}'.format(language), exist_ok=True)
        pattern = '{}/{}/*.md'.format(folder, language)
        files = glob.glob(pattern)
        for file in files:
            write_techniques(folder, language, file)