def dsearch(lod, **kw):
    return list(filter(lambda i: all((i[k] == v for (k, v) in kw.items())), lod))