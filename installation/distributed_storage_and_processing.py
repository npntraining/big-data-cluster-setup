import gdown
import os

print("Downloading and Installing Hadoop")
id = "1-Blx0jokYbdZD4WMxdlNqeYXaMLDAF_S"
output="/home/npntraining/hadoop-2.10.1.zip"
gdown.download(id=id, output=output, quiet=False)
os.system('unzip hadoop-2.10.1.zip')
os.system('rm /home/npntraining/hadoop-2.10.1.zip')

print("Downloading and Installing Hive")
id = "1mKoM4b3Eu0QorDCY9fB22XGuW91lApOz"
output = "/home/npntraining/hive-3.1.2.zip"
gdown.download(id=id, output=output, quiet=False)
os.system('unzip /home/npntraining/hive-3.1.2.zip')
os.system('rm /home/npntraining/hive-3.1.2.zip')

print("Downloading and Installing Sqoop")
id = "1TKxBo4d57zo87youqqC6F1nJBAGcra4U"
output = "/home/npntraining/sqoop-1.4.4.zip"
gdown.download(id=id, output=output, quiet=False)
os.system('unzip /home/npntraining/sqoop-1.4.4.zip')
os.system('rm /home/npntraining/sqoop-1.4.4.zip')

print("Updating bashrc")
id = "1oBbj5N8M7-LMsTZTxXCeZEDJvCp57f7w"
output = "/home/npntraining/bashrc"
gdown.download(id=id, output=output, quiet=False)
os.system('cp /home/npntraining/bashrc ~/.bashrc')
os.system('rm /home/npntraining/bashrc')

print("Downloading and Installing Spark")
id = "1s-7sjTFIjU4OLaJa6-JyBstbcrO7KIy3"
output="/home/npntraining/spark-3.1.3.zip"
gdown.download(id=id, output=output, quiet=False)
os.system('unzip spark-3.1.3.zip')
os.system('rm /home/npntraining/spark-3.1.3.zip')
