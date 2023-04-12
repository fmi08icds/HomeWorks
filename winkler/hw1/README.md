# Homework 1

I am using the operating system Linux Mint 20.3. My setup was fairly simple because I have already installed the executable `python3` and `git` as well as the python package `jupyterlab`. I made sure that I have the correct versions installed using these commands:

``` bash
git --version
# git version 2.25.1

python3 --version
# Python 3.8.10

pip3 freeze | grep jupyterlab
# jupyterlab==3.5.0
# jupyterlab-pygments==0.2.2
# jupyterlab-server==2.16.3
```

There I noticed that my python version is lower than version 3.9, so I installed it using `sudo apt install python3.9`. After that I reinstalled the `jupyterlab` package for the new python version using the command:

```
python3.9 -m pip install jupyterlab
```

I can start the jupyterlab server now with `python3.9 -m jupyterlab`.

