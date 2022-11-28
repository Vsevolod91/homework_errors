def get_val(coll, key, default=None):
    if key in coll:
        return coll[key]
    else:
        return default

if __name__ == "__main__":
    get_val(coll, key, default)

