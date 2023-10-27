# built-in modules
from os import getcwd, sep, walk
from os.path import exists, split
from pathlib import Path
from zipfile import ZipFile, ZIP_DEFLATED

# pip modules
from PIL.Image import open

# local modules
from compress import compress
from utilities import formatted_sizeof, zipdir

if __name__ == "__main__":
    file_input = input('File: ')
    if file_input.endswith('/'):
        file_input = file_input.removesuffix('/')

    percentage_input = int(input('Compression % (Default 40, 0-100): ') or 40)

    if not file_input == '' and exists(file_input) and file_input.endswith('.epub'):
        head, tail = split(file_input)
        ext_dir = getcwd() + sep + 'extracted_epub'

        with ZipFile(file_input, 'r') as zipf:
            zipf.extractall(ext_dir)

        for root, dirs, files in walk(ext_dir):
            for index, file in enumerate(files):
                if file.endswith('.png') or file.endswith('.jpg') or file.endswith('.jpeg'):
                    extension = file.split('.')[1]
                    print(f'[INFO]: Found .{extension}')

                    image = open(root + sep + file)
                    file_path = Path(root + sep + file)

                    old_size = formatted_sizeof(file_path.stat().st_size)
                    compress(root, file, image, percentage_input)
                    new_size = formatted_sizeof(file_path.stat().st_size)

                    print(f'[INFO]: Compressed {file} from {old_size} to {new_size}')
        print('[INFO]: Done!')
        print('[INFO]: Overwrote the original .epub.')

        with ZipFile(file_input, 'w', ZIP_DEFLATED) as zipf:
            zipdir(ext_dir, zipf)
    else:
        print('File does not exist at the provided path or is not a .epub.')