import gdown
import os
import sys

BASE_PATH = "/mnt/c/Users/Naveen/"
ARTIFACT_NAME = "big-data-masters-program-template.zip"


def main(arg):
    print("Downloading Big Data Masters Program Template")
    id = arg[1]
    gdown.download(id=id, output=BASE_PATH, quiet=False)
    os.system("unzip {}{} -d{}".format(BASE_PATH, ARTIFACT_NAME, BASE_PATH))
    os.system("unzip {}{}".format(BASE_PATH, ARTIFACT_NAME))
    os.system('rm {}{}'.format(BASE_PATH, ARTIFACT_NAME))


if __name__ == '__main__':
    main(sys.argv)
