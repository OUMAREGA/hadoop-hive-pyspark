#!/bin/sh

/entrypoint.sh /run.sh &

until $(jps | grep -q "NameNode")
do
	echo "HDFS not operationnal : waiting..."
	sleep 2
done

hdfs dfs -mkdir -p /user/hadoop/data
hdfs dfs -mkdir /spark
hdfs dfs -chmod g+w /spark

# in order to keep the container running

tail -f /dev/null
