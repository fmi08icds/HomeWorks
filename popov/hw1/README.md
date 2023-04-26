## Environment: 

OS - Linux 
Editor - Jupyter lab 


## Process: 

### 1. Install conda 

Download latest conda installation file for linux from (https://docs.conda.io/en/latest/miniconda.html#linux-installers)
Install using 
    sudo sh Miniconda3-latest-Linux-x86_64.sh
Install jupyterlab using 
    conda install -c conda-forge jupyterlab
Prompt: "conda: command not found"
Retry installation with 
    bash Miniconda3-latest-Linux-x86_64.sh
Checking installation, conda is now a recognised command. 

### 2. Install Jupyterlab 

Install jupyterlab using 
    conda install -c conda-forge jupyterlab
Run using 
    jupyter lab

### 3. Install git 

First update packages using 
    sudo apt-get update
Install git with 
    sudo apt-get install git-all
Check the installation is successful by git version

Set username and email by typing the following in the terminal 
    git config -global user.name "tomashkin"
    git config -global user.email "tomislav.popov98@gmail.com"

clone repository by using 
    git clone https://github.com/fmi08icds/HomeWorks.git

cd to homeworks folder and create subfolders using mkdir command

    mkdir popov 
    cd popov
    mkdir hw1

### 4. Open jupyterlab in hw1 folder and create readme :) 
Look at https://www.markdownguide.org/basic-syntax/ for some markdown syntax 


