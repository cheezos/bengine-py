import cProfile, pstats, io
from typing import Callable

def profile(fun: Callable) -> Callable:
    def inner(*args, **kwargs) -> Callable:
        pr = cProfile.Profile()
        pr.enable()
        retval = fun(*args, **kwargs)
        pr.disable()
        s = io.StringIO()
        sortby = "cumulative"
        ps = pstats.Stats(pr, stream=s).sort_stats(sortby)
        ps.print_stats()
        print(s.getvalue())
        return retval

    return inner