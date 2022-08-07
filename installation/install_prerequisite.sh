#!/bin/bash

#installing Java
sudo apt update
sudo apt install unzip
sudo apt install openjdk-8-jdk -y
java -version
javac -version

printf "Java installation is done\n"


#installing Python
python_cmd=("sudo apt update" "sudo apt install software-properties-common" "sudo add-apt-repository ppa:deadsnakes/ppa" "sudo apt install python3-pip" "pip3 install gdown")
for i in "${python_cmd[@]}"; do
    $i
done
printf "Python installation is done\n"

#installing SSH
sudo apt install openssh-server openssh-client -y
ssh-keygen -t rsa -P '' -f ~/.ssh/id_rsa
cat ~/.ssh/id_rsa.pub >> ~/.ssh/authorized_keys
chmod 0600 ~/.ssh/authorized_keys
sudo apt-get install ssh
sudo ssh-keygen -A
sudo service ssh restart
sudo service ssh status

printf "SSH installation is done\n"



