confluent local load sink-1 -- -d sink-postgres.json
curl -X DELETE http://localhost:8083/connectors/sink-1
