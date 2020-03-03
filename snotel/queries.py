createLocationTableQuery = """CREATE TABLE IF NOT EXISTS location_data (
                 id int, 
                 elevation int, 
                 snowCurrent int,
                 snowMedian int ,
                 snowPctAvg int,  
                 waterCurrent int, 
                 waterAverage int, 
                 waterPctAvg int,
                 locationName text,
                 basinName text,  
                 PRIMARY KEY (id)"""

createBasinAggregateTableQuery = """CREATE TABLE IF NOT EXISTS basin_data (
                 id int, 
                 pctmedian int,
                 pctavg int 
                 basinName text, 
                 PRIMARY KEY (basinName)"""

def execute_query(query, session):
    """
    This function will try to execute the query passed by function parameter, or
    print exception if execution of CQL query fails
    Parameter:
        query: CQL query to be executed
    """
    try:
        session.execute(query)
    except Exception as e:

        print("dfdf")
        print(e)
