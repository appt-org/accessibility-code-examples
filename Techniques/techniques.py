import glob
import os


folders = ['Android', 'iOS', 'Flutter', 'React-Native', 'Xamarin']
languages = ['en']

# Read all text from a file
def read_file(file):
    print('Reading file {}'.format(file))
    text = None
    with open(file) as f:
        text = f.read()
    return text

# Write text to a file
def write_file(file, text):
    print('Writing to file {}'.format(file))
    with open(file, 'w') as f:
        f.write(text)

for folder in folders:
    for language in languages:
        pattern = '{}/{}/*.md'.format(folder, language)
        files = glob.glob(pattern)
        for file in files:
            text = read_file(file)
            file_name = os.path.basename(file)
            file_out = 'Techniques/{}'.format(file_name)
            write_file(file_out, text)
            break
    break