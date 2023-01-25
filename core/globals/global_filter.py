def set_filter(ctx):
    strfilter = dict()
    if not ctx['order_by']:
        ctx['order_by'] = ''
    str_order_by_operator = ''
    ctx['filterfieldvalue'] = dict()
    if "filter" in ctx:
        if ctx['filter']:
            for filterpart in ctx['filter'].split(";"):
                filteritems = filterpart.split("~~")
                if filteritems[2] and filteritems[0] != 'order_by':
                    strfilter.update({filteritems[0] + filteritems[1]: filteritems[2]})
                    ctx['filterfieldvalue'].update({filteritems[0]: filteritems[2]})
                elif filteritems[0] == 'order_by':
                    if filteritems[2]:
                        if filteritems[1] == 'asc':
                            str_order_by_operator = '-'
                        ctx['order_by'] = str_order_by_operator + filteritems[2]
    return strfilter


# def use_global_filter(records, ctx):
#     ctx['filter'] = set_filter(ctx)
#     if ctx['filter']:
#         records = records.filter(**ctx['filter'])
#     if ctx['order_by'] and ctx['order_by'] != "-":
#         records = records.order_by(ctx['order_by'])
#     return records
