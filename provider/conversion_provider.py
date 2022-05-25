def get_value(org:str):
    rates = [{'key': 'USD', 'value': 1},{'key': 'COL', 'value': 3930.55},{'key': 'BTC', 'value': 0.000034}]
    list_filter = list(filter(lambda x: x['key'] == org, rates))
    list_filter_count = len(list_filter)
    if(list_filter_count<1):
        raise Exception("Invalid org")
    org_value = list_filter[0]['value']
    return org_value

def get_conversion(org: str,dest: str,amount: int):
    result_org = get_value(org)
    result_dest = get_value(dest)
    return (result_dest/result_org) * amount