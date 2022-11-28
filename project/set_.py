def set_(coll, path, value):
    list_endict = []
    len_path = len(path)
    if len_path >= 2:
        for k in path:
            if len_path == 0:
                break
            len_path -= 1
            list_endict.append({k: None})
        for k in list_endict[-1].keys():
            list_endict.append({k: value})
        list_endict.pop(-2)
        for endict in reversed(list_endict):
            for k in list_endict[-2].keys():
                list_endict[-2][k] = endict
            if len(list_endict) == 2:
                break
            list_endict.pop(-1)
        for k in list_endict[0].keys():
            coll[k] = list_endict[1]
    else:
        for k in path:
            coll[k] = value
    return coll

if __name__ == "__main__":
    set_(coll, path, value)






        

