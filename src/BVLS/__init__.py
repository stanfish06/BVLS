from . import _bvls, _bvls_mod2


def bvls(G, d, bounds):
    """
    Bounded Value Least Squares

    Parameters
    ----------
      G : (M,N) array
        System matrix which maps the parameter space to the observation
        space

      d : (M,) array
        Observation vector

      bounds : (2,N) array
        lower and upper bounds on the solution

    Returns
    -------
      m : (N,) array
        solution to the bounded least squares problem

    """
    # only return the first object from the fortran routine and discard
    # the rest
    return _bvls.bvls(G, d, bounds)[0]


def bvls_mod2(G, d, bounds, ridge_coef):
    """
    Bounded Value Least Squares

    Parameters
    ----------
      G : (M,N) array
        System matrix which maps the parameter space to the observation
        space

      d : (M,) array
        Observation vector

      bounds : (2,N) array
        lower and upper bounds on the solution

    Returns
    -------
      m : (N,) array
        solution to the bounded least squares problem

    """
    # only return the first object from the fortran routine and discard
    # the rest
    return _bvls_mod2.bvls(G, d, bounds, ridge_coef)[0]
