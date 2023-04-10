from File.creator import random_files_creator_ex
from File.renamer import files_rename

if __name__ == '__main__':
    random_files_creator_ex("files", img=3, png=4, jpg=5, avi=4, mk4=9, py=1, html=5, txt=6, md=2)
    files_rename("files", extensions=["img", "png", "jpg"], new_extension="image", old_name_range=(0, 3),
                 new_name="_this_image")