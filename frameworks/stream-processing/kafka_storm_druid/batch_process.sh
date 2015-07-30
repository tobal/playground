#! /bin/bash

ZOOKEEPER='/home/tobal/local/bin/zookeeper-3.4.6'
KAFKA='/home/tobal/local/bin/kafka_2.10-0.8.2.1'
DRUID='/home/tobal/local/bin/druid-0.8.0'

# Start Zookeeper
$ZOOKEEPER/bin/zkServer.sh start

# Start Kafka
$KAFKA/bin/kafka-server-start.sh $KAFKA/config/server.properties

# Create new Kafka topic
$KAFKA/bin/kafka-topics.sh --create --zookeeper localhost:2181 --replication-factor 1 --partitions 1 --topic historic_data

# Feed topic with batched data
./batch_generator.py | $KAFKA/bin/kafka-console-producer.sh --broker-list localhost:9092 --topic historic_data

