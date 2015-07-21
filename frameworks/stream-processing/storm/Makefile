.PHONY: build
build:
	mvn clean install -DskipTests=true

.PHONY: run
run:
	mvn compile exec:java -Dstorm.topology=storm.playground.TestTopology

