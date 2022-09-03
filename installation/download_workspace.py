import gdown
import os
import sys

BASE_PATH = "/mnt/c/Users/{}/"
ARTIFACT_NAME = "big-data-masters-program-template.zip"


def main(arg):
    print("Downloading Big Data Masters Program Template")
    id = arg[1]
    base_path = BASE_PATH.format(arg[2])
    gdown.download(id=id, output=BASE_PATH, quiet=False)
    os.system("unzip {}{} -d{}".format(base_path, ARTIFACT_NAME, base_path))
    os.system("unzip {}{}".format(base_path, ARTIFACT_NAME))
    os.system('rm {}{}'.format(base_path, ARTIFACT_NAME))


if __name__ == '__main__':
    main(sys.argv)
