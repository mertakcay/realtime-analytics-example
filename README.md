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

### Notes
- I couldn't add airflow to project because my memory isn't sufficent for that. I have planned different project for usage of airflow.
## Roadmap 

- [x] Create Kafka docker-compose 
- [x] Create Druid docker-compose for OLAP
- [x] Create Spark docker-compose
- [x] Create topic for Druid
- [x] Produce Kafka with Dummy Variable
- [x] Consume dummy data from Kafka
- [x] Show dummy data on Superset
- [ ] Create Scraping script from live-api
- [x] Set Kafka config to Druid
- [x] Mount Druid and Kafka
- [ ] Create Airflow for schedule and monitor DAG
- [x] Design architecture of live-stream data
- [x] So on, The list will be adjusted for requirements on going

## Architecture

## Install

* If you are using macOS platform, you have to set env platform specific setting
```
 export DOCKER_DEFAULT_PLATFORM=linux/amd64  
```


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

##### Superset
*Important*: You must add private network for all nodes in composes in order to connect superset from druid.

Firstly, you can pull files from the original repository and then run below code

```
Run docker-compose file
cd superset && docker-compose up -d 
```
Hint: If you are using the other docker-compose simultaneously, you have to block port forward in superset docker-compose.

To connect druid, you should add pydruid to requirements.txt file 
```
#pydruid connector
pydruid
```

##### Producer
Some basic Python commands are:
```
python <producer_script_name.py>
```

