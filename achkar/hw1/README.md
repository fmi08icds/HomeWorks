## HW1

OS: macOS Monterey

1- Installing MiniConda:

```bash
crul https://repo.anaconda.com/miniconda/Miniconda3-latest-MacOSX-x86_64.sh -o Miniconda3.sh
```
```bash
bash Miniconda3.sh
```

2- Creating Conda environment:
```bash
conda create --name icds python=3.10
```
3- Installing Jupyterlabs:
```bash
conda activate icds
pip install jupyterlab
```