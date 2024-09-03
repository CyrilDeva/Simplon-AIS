#!/bin/bash
#Script to Auto install Snort 3 on Debian 12
#Based on https://docs.snort.org/start/installation and https://snort-org-site.s3.amazonaws.com/production/document_files/files/000/012/147/original/Snort_3.1.8.0_on_Ubuntu_18_and_20.pdf
# v0.9 By Cyril D.

echo "Starting Auto Install script"

# Exit on error
set -e 

# Update package lists
sudo apt update

# Install from Debian repo
sudo apt install -y git cmake build-essential flex libhwloc-dev libluajit-5.1-dev openssl libssl-dev libpcap-dev libpcre2-dev pkg-config zlib1g-dev libsafec-dev libgoogle-perftools-dev ragel libflatbuffers-dev

mkdir -p ~/snort_src
cd ~/snort_src

# Install daq from source
cd ~/snort_src
git clone https://github.com/snort3/libdaq
cd libdaq
./bootstrap
./configure
make -j $(nproc)
sudo make install
cd ..

#Install dnet from source
cd ~/snort_src
git clone https://github.com/dugsong/libdnet
cd libdnet
./configure
make -j $(nproc)
sudo make install
cd ..

# Install boost + HyperScan
cd ~/snort_src
wget https://archives.boost.io/release/1.86.0/source/boost_1_86_0.tar.gz
tar -xvzf boost_1_86_0.tar.gz

cd ~/snort_src
git clone https://github.com/intel/hyperscan

mkdir ~/snort_src/hyperscan-build
cd hyperscan-build/
cmake -DCMAKE_INSTALL_PREFIX=/usr/local -DBOOST_ROOT=~/snort_src/boost_1_86_0/ ../hyperscan
make -j $(nproc)
sudo make install

#Update shared libraries
sudo ldconfig

#Install Snort
cd ~/snort_src
git clone https://github.com/snort3/snort3.git
cd snort3
./configure_cmake.sh --prefix=/usr/local --enable-tcmalloc
cd build
make -j $(nproc)
sudo make install


sudo mkdir /usr/local/etc/rules
sudo mkdir /usr/local/etc/so_rules/
sudo mkdir /usr/local/etc/lists/
sudo touch /usr/local/etc/rules/local.rules
sudo touch /usr/local/etc/lists/default.blocklist
sudo mkdir /var/log/snort


/usr/local/bin/snort -V

echo "End of script"