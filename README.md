
<br>

**Varietal**

<br>
<br>

### Notes

The package [dask-ml](https://ml.dask.org) installs ``numba`` & ``llvmlite``.  However, the installations fail.  Hence, after installing ``dask-ml``

````shell
  conda install -c anaconda dask-ml
````

re-install ``numba`` & ``llvmlite`` via the ``numba`` channel

````shell
  conda install -c numba numba llvmlite
````

This rep's virtual environment is [miscellaneous](https://github.com/briefings/energy#development-notes).

<br>

For ``matplotlib`` graphs [PyQt5](https://pypi.org/project/PyQt5/) is required

````shell
  python -m pip install PyQt5 
````

[About twins](https://matplotlib.org/stable/gallery/subplots_axes_and_figures/two_scales.html).

<br>
<br>

<br>
<br>

<br>
<br>

<br>
<br>