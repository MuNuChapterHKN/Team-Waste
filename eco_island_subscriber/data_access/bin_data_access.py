import data_access.db_utils as utils

'''
It retrieves the island id of the given bin id
'''
def get_bin_island_id(bin_id):
    get_from_table = f"""
    SELECT island_id FROM bin WHERE id = {bin_id} ;
    """
    res = utils.execute_select_one_query(get_from_table)
    island_id = res[0]
    return island_id