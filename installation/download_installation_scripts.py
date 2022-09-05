import gdown
import os
import sys

BASE_PATH = "/home/npntraining/"
ARTIFACT_NAME = "installation_scripts.zip"


def main(arg):
    print("Downloading Installation Scripts")
    gdown.download(id="1GhZ4Bq8pCkvVlk64-4WAJDtj-KvpJjH0",output=BASE_PATH, quiet=False)
    os.system("unzip {}{} -d{}".format(BASE_PATH, ARTIFACT_NAME, BASE_PATH))
    os.system('rm {}{}'.format(BASE_PATH, ARTIFACT_NAME))


if __name__ == '__main__':
    main(sys.argv)
