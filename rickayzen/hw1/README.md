# Environment Setup
## Environment
WSL was aready installed. In a terminal I installed the ubuntu environment with the  command `wsl --install` which I also use to log in.
## Python and pip 
* `sudo apt update`
* `sudo apt install python`
* `sudo apt install python3-pip`
## install JupyterLab
JupyterLab
* `pip install jupyterlab`
* I also set the path variable with `export PATH="$HOME/.local/bin:$PATH"`

Because Jupyter Lab wouldn't open I also installed xdg-utils to see an overview over the browsers with `xdg-open`
* `sudo apt install xdg-utils`

Because trying to open a browser with the command `xdg-open https://www.google.com` returned `Permission denied` for every browser I changed the rights
* `chown -R username:username /home/username`
* `find /home/pipi -type d -print0 | xargs -0 chmod 775`

Then, it said that no browser was installed. So  I installed Firefox. Because `sudo apt install firefox` and via snap didn't work, I used the following:
* `sudo add-apt-repository ppa:mozillateam/ppa`
* `sudo apt install firefox-esr`

Jupyter lab could now be started with the command `jupyter lab` which opens a new Firefox tab.
