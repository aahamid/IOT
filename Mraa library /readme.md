# Installing MRAA Python Library in Different Linux Systems

MRAA is a C/C++ library that provides an easy-to-use API for accessing GPIO, I2C, SPI, and other interfaces on a variety of platforms. In addition to the C/C++ API, MRAA also provides a Python API for accessing these interfaces. In this guide, we will show you how to install the MRAA Python library on different Linux systems.

## Installing MRAA Python on Debian and Ubuntu

Open the terminal and run the following commands:

```
sudo apt-get update
sudo apt-get install python3-pip
sudo pip3 install mraa

```

This will install the MRAA Python library on your system.

## Installing MRAA Python on Fedora

Open the terminal and run the following command:

```
sudo dnf install python3-pip
sudo pip3 install mraa
```

This will install the MRAA Python library on your system.

## Installing MRAA Python on Arch Linux

Open the terminal and run the following command:

```
sudo pacman -S python-pip
sudo pip install mraa
```

This will install the MRAA Python library on your system.

## Installing MRAA Python on CentOS

Open the terminal and run the following command:

```
sudo yum install epel-release
sudo yum install python36-pip
sudo pip3 install mraa
```

This will install the MRAA Python library on your system.

## Installing MRAA Python from Source

If you prefer to install the MRAA Python library from source, you can follow these steps:

1. Download the latest source code from the MRAA GitHub repository: <https://github.com/eclipse/mraa/releases>

2. Extract the downloaded archive and navigate to the extracted directory.

3. Run the following commands in the terminal:

```
mkdir build
cd build
cmake -DBUILDSWIGNODE=OFF ..
make
sudo make install
sudo pip3 install ./python
```

This will build and install the MRAA library and development headers on your system, as well as the Python bindings.

## Conclusion

MRAA is a powerful library for accessing GPIO, I2C, SPI, and other interfaces on a variety of platforms. With this guide, you should now be able to install the MRAA Python library on your Linux system.
