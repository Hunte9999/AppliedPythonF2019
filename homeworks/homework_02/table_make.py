def represents_int(s):
    try:
        int(s)
        return True
    except ValueError:
        return False


def make_table(txt_dict):
    res_row = ''
    keys = list(txt_dict[0].keys())
    max_wid = [len(key) for key in keys]
    vals = [sdict.values() for sdict in txt_dict]
    for vall in vals:
        for nm, el in enumerate(vall):
            max_wid[nm] = max(max_wid[nm], len(str(el)))

    lead_trail = '-' * (sum(max_wid) + 6 + 5 * (len(max_wid) - 1)) + '\n'
    res_row += lead_trail

    for nm, key in enumerate(keys):
        keys[nm] = key.center(max_wid[nm])
    res_row += '|  ' + "  |  ".join(keys) + '  |\n'

    for vall in vals:
        row_prnt = []
        for nm, val in enumerate(vall):
            if represents_int(val):
                row_prnt.append(str(val).rjust(max_wid[nm]))
            else:
                row_prnt.append(str(val).ljust(max_wid[nm]))
        res_row += '|  ' + "  |  ".join(row_prnt) + '  |\n'
    res_row += lead_trail
    return res_row
