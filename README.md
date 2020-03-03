confluent local load sink-1 -- -d sink-postgres.json
curl -X DELETE http://localhost:8083/connectors/sink-1

An Airflow DAG with a start_date, possibly an end_date, and a schedule_interval defines a series of intervals which the scheduler turn into individual Dag Runs and execute. A key capability of Airflow is that these DAG Runs are atomic, idempotent items, and the scheduler, by default, will examine the lifetime of the DAG (from start to end/now, one interval at a time) and kick off a DAG Run for any interval that has not been run (or has been cleared). This concept is called Catchup.

If your DAG is written to handle its own catchup (IE not limited to the interval, but instead to “Now” for instance.), then you will want to turn catchup off (Either on the DAG itself with dag.catchup = False) or by default at the configuration file level with catchup_by_default = False. What this will do, is to instruct the scheduler to only create a DAG Run for the most current instance of the DAG interval series.


airflow webserver -p 8081
airflow scheduler 