# Real-Time Data Analysis Project
## Overview
This project aims to analyze real-time data using various technologies such as Druid, Kafka, Spark, Python, Docker and Superset. The project will ingest, process, aggregate and visualize streaming data from different sources and provide insights for business intelligence and decision making.
## Technologies
The project will use the following technologies:
- Druid: A high-performance, real-time analytics database that supports sub-second queries on streaming and batch data at scale1.
- Kafka: A distributed streaming platform that enables reliable and scalable data ingestion and processing.
- Spark: A unified analytics engine that supports large-scale data processing and machine learning.
- Python: A popular programming language that offers a rich set of libraries and frameworks for data analysis and manipulation4.
- Docker: A platform that enables building, running and sharing applications using containers.
- Superset: An open-source business intelligence platform that allows users to create and explore interactive dashboards and visualizations on their data.

## Some Choices
- Druid database management was abandoned because it was too complex for my current needs. Additionally, the Clickhouse Kafka connector was abandoned due to various requirement deficiencies in localhost. We will continue our journey with Cassandra.

## Roadmap 

- [x] Create Kafka docker-compose 
- [x] Create Druid docker-compose for OLAP
- [x] Create Spark docker-compose
- [x] Create topic for Druid
- [x] Produce Kafka with Dummy Variable
- [x] Consume dummy data from Kafka
- [ ] Show dummy data on Superset
- [ ] Create Scraping script from live-api
- [ ] Set Kafka config to Druid
- [ ] Mount Druid and Kafka
- [ ] Create Airflow for schedule and monitor DAG
- [ ] Design architecture of live-stream data
- [ ] So on, The list will be adjusted for requirements on going

## Architecture

## Install

#### Useful Scripts 

##### Kafka

Some basic Kafka commands are:
```
Create Topic - after connect kafka bash in docker
./bin/kafka-topics.sh --bootstrap-server <topic_name>:9092 --create --topic <topic_name>

List Topics 
./bin/kafka-topics.sh --bootstrap-server=localhost:9092 --list
```

##### Docker
Some basic Docker commands are:
```
Run docker-compose file
docker-compose <docker-compose-filename>
```

```
Connect docker bash 
docker exec -it <container_name> bash
```

##### Producer
Some basic Python commands are:
```
python <producer_script_name.py>
```

