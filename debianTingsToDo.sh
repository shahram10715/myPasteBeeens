# things to do after installing lovely debian

# update packages
sudo apt update

# remove extra packages
sudo apt -y purge \
xiterm+thai \
mlterm mlterm-common mlterm-tools \
xterm \
thunderbird \
gnome-maps \
goldendict \
hdate-applet \
gnome-todo \
rhythmbox \
mozc-* \
transmission-* \
shotwell \
gnome-sound-recorder \
gnome-software \
software-properties-gtk \
gnome-games


# autoremove
sudo apt -y autoremove

# upgrade packages
sudo apt -y upgrade

# install needed packages
sudo apt -y install \
bash-completion \
git \
neofetch \
network-manager-openvpn-gnome \
vlc


echo "bind 'set completion-ignore-case on'" >> ~/.bashrc










