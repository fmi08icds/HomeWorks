## Setting up the enviroment
I am using miniconda un Linux. To install miniconda you first have to download the installer [here](https://docs.conda.io/en/latest/miniconda.html#linux-installers). 
After downloading it is important to verify the hash:
```
sha256sum Miniconda3-latest-Linux-x86_64.sh
```
You find the hash on the download page.
If all is fine you can run the following command to install miniconda:
```
bash Miniconda3-latest-Linux-x86_64.sh
```
If you are unsure about anything you can accept the defaults for know, you can change them later.
After installation is done reopen your terminal.
To verify if the installation was successful execute the following command which lists all installed packages:
```
conda list
```