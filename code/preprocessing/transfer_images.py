import os
import shutil

def move_and_rename_png_files(root_dir, target_dir):
    """
    Move all PNG files from the nested directory structure to a single folder,
    renaming them based on their original location.
    """
    if not os.path.exists(target_dir):
        os.makedirs(target_dir)

    # i = 0
    for root, dirs, files in os.walk(root_dir):
        for file in files:
            if file.endswith(".png"):
                # Construct the new filename
                path_parts = root.split(os.sep)
                # case_part = path_parts[-3]  
                case_day_part = path_parts[-2] 
                new_filename = f"{case_day_part}_{file}"

                # if i == 10:
                #     break
                # # print(path_parts)
                # print(file)
                # # print(case_part)
                # print(case_day_part)
                # print()
                # i += 1

                # Move and rename the file
                src_file_path = os.path.join(root, file)
                dest_file_path = os.path.join(target_dir, new_filename)
                shutil.move(src_file_path, dest_file_path)

root_dir = '/Users/echingkho/Desktop/University/Master/1st_year/Fall/dl_cisc_867/project/uw-madison-gi-tract-image-segmentation/train_copy'
target_dir = '/Users/echingkho/Desktop/University/Master/1st_year/Fall/dl_cisc_867/project/uw-madison-gi-tract-image-segmentation/dataset'
move_and_rename_png_files(root_dir, target_dir)
print("Images have been moved and renamed.")
