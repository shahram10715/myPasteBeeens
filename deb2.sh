# things to do after installing lovely debian

# update packages
sudo apt update


# upgrade packages
sudo apt -y upgrade


# autoremove
sudo apt -y autoremove


# install needed packages
sudo apt -y install \
bash-completion \
gnome-multi-writer \
git \
neofetch \
network-manager-openvpn-gnome \
vlc


echo "bind 'set completion-ignore-case on'">>~/.bashrc



