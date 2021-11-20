import data_access.db_utils as utils

'''
It retrieves the bin id and the type of the given sensor id
'''
def get_sensor(sensor_id):
    get_from_table = f"""
    SELECT bin_id, type FROM sensor WHERE id = {sensor_id} ;
    """
    res = utils.execute_select_one_query(get_from_table)
    print(res)
    return res