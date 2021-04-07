import data_access.db_utils as utils

'''
It inserts measured value given the sample, bin id and island id
'''
def add_measurement_value(bin_id, island_id, val):
    add_to_table = f"""
    INSERT INTO load_sensor (bin_id, island_id, value) VALUES ({bin_id},{island_id},{val});
    """
    utils.execute_insert_query(add_to_table)