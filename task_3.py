lst = [1, 3, 123, "ya", [123, 3, " lub", ["ly ", 1231, ["azure "]]], "botov"]

def recstr(lst, s: str):
    if isinstance(lst, str):
        s += lst
    elif isinstance(lst, list):
            for i in lst:
                s = recstr(i, s)
    return s

print(recstr(lst, ""))
