invert-voila
============

A voila app to invert images using imagemagick.

Quickstart
----------

### Local

    conda env create
    conda activate invert-voila
    python -m ipykernel install --user --name invert-voila
    jupytext --to ipynb index.py --set-kernel -
    voila --theme dark index.ipynb

### Binder

[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/thomasgilgenast/invert-voila/HEAD?urlpath=voila%2Frender%2Findex.py)
