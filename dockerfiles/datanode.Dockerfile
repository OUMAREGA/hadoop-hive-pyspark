FROM bde2020/hadoop-datanode:2.0.0-hadoop2.7.4-java8

# Configuration du terminal dans le traitement
# des caractères au format UTF-8
ENV LC_CTYPE C.UTF-8
ENV HADOOP_HOME=/opt/hadoop-2.7.4

RUN sed -i 's/-backports//g' /etc/apt/sources.list
RUN apt-get update && apt-get install -y python3 vim nano wget

RUN wget -O /opt/mongo-hadoop-streaming.jar https://repo1.maven.org/maven2/org/mongodb/mongo-hadoop-streaming/1.3.0/mongo-hadoop-streaming-1.3.0.jar

RUN wget -O /opt/mongo-hadoop-core.jar https://repo1.maven.org/maven2/org/mongodb/mongo-hadoop-core/1.3.0/mongo-hadoop-core-1.3.0.jar


