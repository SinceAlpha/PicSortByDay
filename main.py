import os
import shutil
from PIL import Image
from pyexiv2 import Image as ExImage
from PyQt5.QtWidgets import QApplication, QFileDialog


def get_date_taken(path):
    try:
        exiv_image = ExImage(path)
        exif_data = exiv_image.read_exif()
        return exif_data['Exif.Photo.DateTimeOriginal'].split()[0].replace(":", "-")
    except:
        return None


def organize_photos(folder_path):
    for filename in os.listdir(folder_path):
        if filename.endswith(
                ('.jpg', '.png', '.jpeg', '.JPG', '.PNG', '.JPEG')):  # add extention here if needed
            file_path = os.path.join(folder_path, filename)
            date_taken = get_date_taken(file_path)

            if date_taken:
                new_folder_path = os.path.join(folder_path, date_taken)

                if not os.path.exists(new_folder_path):
                    os.makedirs(new_folder_path)

                shutil.move(file_path, os.path.join(new_folder_path, filename))


def main():
    app = QApplication([])
    folder_path = QFileDialog.getExistingDirectory(None, "Select Folder")

    if folder_path:
        organize_photos(folder_path)


if __name__ == "__main__":
    main()
