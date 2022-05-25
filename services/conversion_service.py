import provider.conversion_provider as conversion_provider 

def get_conversion(org: str,dest: str,amount: int):
    return conversion_provider.get_conversion(org,dest,amount)