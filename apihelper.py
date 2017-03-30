def info(object, spacing=10, collapse=1):
    """Print methods and doc strings.

    Takes module, class, list, dictionary, or string.
    It collapses multi-line doc strings into a single line.

    processFunc is a function, but which function it is depends 
    on the value of the collapse variable. If collapse is true, 
    processFunc(string) will collapse whitespace; otherwise, 
    processFunc(string) will return its argument unchanged.
    """
    methodList = [method for method in dir(object) if callable(getattr(object,method))]
    processFunc = collapse and (lambda s: " ".join(s.split())) or (lambda s: s)
    print "\n".join(["%s %s" %
                      (method.ljust(spacing),
                       processFunc(str(getattr(object, method).__doc__)))
                     for method in methodList])

if __name__== "__main__":
    print info.__doc__
