# TODO refactor this module using buisness logic names


def _row(x):
    # x is one line from file
    p = x.strip().split(",")  # split by comma
    if len(p) != 4:  # if line is bad
        return None  # return nothing

    n = p[0]  # product name
    c = p[1]  # product category
    a = float(p[2])  # price of one item
    q = int(p[3])  # amount of items

    return {"n": n, "c": c, "a": a, "q": q}  # make dict


def read_data(path):
    res = []  # final list
    with open(path, "r", encoding="utf-8") as f:  # open file
        for x in f:  # go over lines
            r = _row(x)  # convert line to dict
            if r is not None:  # if parsing was ok
                res.append(r)  # add to result
    return res  # return result


def total(ds, d=0):
    s = 0  # total sum
    for i in ds:  # loop all rows
        s = s + i["a"] * i["q"]  # add price * quantity
    if d:  # if discount exists
        s = s - s * d / 100  # apply discount
    return s  # give answer


def find_big(ds, t):
    out = []  # rows that are big enough
    for i in ds:  # each row
        x = i["a"] * i["q"]  # row money
        if x >= t:  # compare with threshold
            out.append(i)  # save row
    return out  # done


def by_category(ds):
    m = {}  # category to money
    for i in ds:  # each row
        k = i["c"]  # category name
        if k not in m:  # create if needed
            m[k] = 0  # start from zero
        m[k] += i["a"] * i["q"]  # add row amount
    return m  # return mapping


def report(ds):
    lines = []  # text lines
    lines.append("Report")  # title
    lines.append("------")  # separator

    for k, v in by_category(ds).items():  # category and amount
        lines.append(f"{k}: {v}")  # make line

    lines.append("------")  # separator again
    lines.append(f"Total: {total(ds)}")  # total sum

    return "\n".join(lines)  # merge lines


def write_report(path, txt):
    # TODO better errors
    with open(path, "w", encoding="utf-8") as f:  # open file for writing
        f.write(txt)  # write text