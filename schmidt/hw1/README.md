
# Environment setup
## Starting point
- I created the environment on my laptop with Ubuntu 20.04. 
- Conda was already installed as I use it for most of my coding

## Environment creation
The first step was creating the environment itself. 
Given the requirements for this course, I chose Python 3.10.

As the environment name, I chose icds based on the name of the module.

```  
conda create --name icds python=3.10
```

## Installing jupyter
To benefit from condas package management, I installed jupyter using conda install instead of pip install.
Initially, I used the wrong command that return the following error:

```
conda install juypter
PackagesNotFoundError: The following packages are not available from current channels:

jupyter
```

After looking at the [official website](https://anaconda.org/anaconda/jupyter) for conda, I found the correct command:

```
conda install -c anaconda jupyter
```

Finally, to ensure that jupyter's version was meeting the requirements, I ran this command in bash: 

```
jupyter --version
```

This returned the following versions and among them `jupyterlab: 3.5.3` which meets the requirements:

```
IPython          : 8.8.0
ipykernel        : 6.19.2
ipywidgets       : 7.6.5
jupyter_client   : 7.4.8
jupyter_core     : 5.1.1
jupyter_server   : 1.23.4
jupyterlab       : 3.5.3
nbclient         : 0.5.13
nbconvert        : 6.5.4
nbformat         : 5.7.0
notebook         : 6.5.2
qtconsole        : 5.4.0
traitlets        : 5.7.
```
