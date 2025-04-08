def split(inp, split):
    out = []
    string = []
    for i in range(len(inp)):
        if inp[i] != split:
            string.append(inp[i])
        else:
            out.append(string)
            string = []
    out.append(string)
    string = []
    for i in range(len(out)):
        out[i] = ''.join(out[i])
    return out