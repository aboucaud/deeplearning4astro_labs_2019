
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
    "masks.tar.gz",
    "single_imgs.tar.gz",
    "blends.tar.gz",
]


def main(output_dir, delete):
    urls = [
        f"{URL}/{FOLDER}/{filename}"
        for filename in FILES
    ]

    if not os.path.exists(output_dir):
        print(f"Creating directory {output_dir}")
        os.mkdir(output_dir)

    for url, filename in zip(urls, FILES):
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
                f.extractall(output_dir)
            print("Done.")

            if delete:
                os.remove(output_file)
                print(f"=> File {output_file} removed.")


if __name__ == '__main__':
    main(output_dir='data', delete=True)
