
"""
Download script for data stored remotely
----------------------------------------

author: Alexandre Boucaud <aboucaud@apc.in2p3.fr>
license: BSD (3-clause)

"""
import os
import sys
import tarfile

try:
    from urllib.request import urlretrieve
except ImportError:
    from urllib import urlretrieve

URL = "https://www.apc.univ-paris7.fr/Downloads/comput/aboucaud"
FOLDER = "ed127"
FILES = [
    "test_blends_mini.npy",
    "test_target_img_mini.npy",
    "test_target_masks_mini.npy",
    "train_blends_mini.npy",
    "train_target_img_mini.npy",
    "train_target_masks_mini.npy",

]
BIG_FILES = [
    "masks.tar.gz",
    "single_imgs.tar.gz",
    "blends.tar.gz",
]


def main(output_dir, delete=False, full=False):
    if full:
        files = BIG_FILES
    else:
        files = FILES

    urls = [
        f"{URL}/{FOLDER}/{filename}"
        for filename in files
    ]

    if not os.path.exists(output_dir):
        print(f"Creating directory {output_dir}")
        os.mkdir(output_dir)

    for url, filename in zip(urls, files):
        output_file = os.path.join(output_dir, filename)

        if os.path.exists(output_file):
            print(f"{filename} already downloaded.")
            continue

        print(f"Downloading from {url} ...")
        urlretrieve(url, filename=output_file)
        print(f"=> File saved as {output_file}")

        if filename.endswith("tar.gz"):
            print("Extracting tarball..")
            with tarfile.open(output_file, "r:gz") as f:
                def is_within_directory(directory, target):
                    
                    abs_directory = os.path.abspath(directory)
                    abs_target = os.path.abspath(target)
                
                    prefix = os.path.commonprefix([abs_directory, abs_target])
                    
                    return prefix == abs_directory
                
                def safe_extract(tar, path=".", members=None, *, numeric_owner=False):
                
                    for member in tar.getmembers():
                        member_path = os.path.join(path, member.name)
                        if not is_within_directory(path, member_path):
                            raise Exception("Attempted Path Traversal in Tar File")
                
                    tar.extractall(path, members, numeric_owner=numeric_owner) 
                    
                
                safe_extract(f, output_dir)
            print("Done.")

            if delete:
                os.remove(output_file)
                print(f"=> File {output_file} removed.")


if __name__ == '__main__':
    import sys
    try:
        full = sys.argv[1].lower() == 'full'
    except:
        full = False
    main(output_dir='data', delete=True, full=full)
