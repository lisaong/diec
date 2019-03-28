# Install on Raspberry Pi
```
sudo apt-get install libssl-dev

pip install packages/*
pip install –r requirements.txt

```

# Install on Windows
PyOTA is not compatible with python 3.7. See https://stackoverflow.com/questions/52971244/import-filters-typeerror-type-doesnt-support-mro-entry-resolution

```
conda create -n iota python=3.6
conda activate iota

pip install -r requirements.txt
```

# References
- https://github.com/iotaledger/iota.lib.py (curl extension not available for Raspberry Pi)

