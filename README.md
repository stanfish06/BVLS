# BVLS

## Description
This is a python wrapper for the bounded variable least squares (BVLS) 
solver (the fortran source code has been distributed under the GNU LGPL 
license and can be found [here](https://people.sc.fsu.edu/~jburkardt/f_src/bvls/bvls.html)). 
The algorithm finds the vector `m` such that `G.dot(m)` is the best 
prediction to the observation vector `d` in a least squares sense 
with the constraint that `bounds[0] >= m` and `bounds[1] <= m`.

## Installation
Compiling the Fortran code and creating the python wrapper is done 
with the following shell commands
``` 
$ git clone http://www.github.com/treverhines/BVLS 
$ cd BVLS 
$ python setup.py install 
``` 
This will install a python module named `bvls` which gives access to 
all the subroutines in `bvls.f90`.

### The above method is deprecated
use
```
uv build
# then install the wheel with pip
```

## Usage
The following python code sets up and solves a bounded value least 
squares problem
```python
import BVLS
import numpy as np
G = np.random.random((10,2))
m = np.array([1.0,2.0])
d = G.dot(m)    
lower_bounds = np.array([0.0,0.0])
upper_bounds = np.array([1.5,1.5])
bounds = [lower_bounds,upper_bounds]
soln = BVLS.bvls(G,d,bounds)
```
See the documentation in `bvls.f90` for additional details