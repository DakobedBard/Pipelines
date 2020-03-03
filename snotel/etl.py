from data_utils.cassandra_utils import createCassandraConnection, createKeySpace
from snotel.scrape import extract_snowpack_data
from data_utils.mongoConnection import getMongoClient


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
        print(e)

# execute_query(createLocationTableQuery, dbsession)
# execute_query(createBasinAggregateTableQuery, dbsession)

regions_dictionary = extract_snowpack_data()
client = getMongoClient()
snow_db = client['Snow-Pack-Data']
snow_collection = snow_db['snow_collection']
snow_collection.insert_one(regions_dictionary)






# createLocationTableQuery = """CREATE TABLE IF NOT EXISTS location_data (
#                  id int,
#                  elevation int,
#                  snowCurrent int,
#                  snowMedian int ,
#                  snowPctAvg int,
#                  waterCurrent int,
#                  waterAverage int,
#                  waterPctAvg int,
#                  locationName text,
#                  basinName text,
#                  PRIMARY KEY (id))"""
#
# createBasinAggregateTableQuery = """CREATE TABLE IF NOT EXISTS basin_data (
#                  id int,
#                  pctmedian int,
#                  pctavg int
#                  basinName text,
#                  PRIMARY KEY (basinName)"""