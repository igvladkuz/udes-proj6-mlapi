# Prerequisite: a Linux VM with Ubuntu
# In Azure cloud shell:
# ssh to the VM
# 1. Download and instal the VSTS agent for Linux
curl -O https://vstsagentpackage.azureedge.net/agent/2.210.1/vsts-agent-linux-x64-2.210.1.tar.gz
mkdir myagent && cd myagent
tar zxvf ../vsts-agent-linux-x64-2.210.1.tar.gz

# install docker
sudo snap install docker
# add a group and add the current user
sudo groupadd docker
sudo usermod -aG docker $USER
exit

# configuration
./config.sh
sudo ./svc.sh install
sudo ./svc.sh start

