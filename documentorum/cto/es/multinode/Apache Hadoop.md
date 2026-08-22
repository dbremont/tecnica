# Apache Hadoop

> **Apache Hadoop** is an open-source, distributed computing framework designed to process and store large-scale datasets across clusters of commodity hardware. It provides a reliable, scalable, and fault-tolerant architecture for data-intensive applications and can handle both batch and real-time data processing tasks.
> 

> **Language**: **Hadoop** is primarily written in **Java**, but it also has components written in other languages like **C** (for native libraries) and **Shell scripting** (for certain administrative tasks). Additionally, it supports **APIs** for languages like **Python** and **R** for interacting with the **framework**.
> 

## Index

## **Hadoop Distributed File System (HDFS)**:

- **Definition**: HDFS is a distributed storage layer of Hadoop, designed for storing massive datasets across a cluster of machines. It splits large files into blocks (default 128MB or 256MB) and distributes them across multiple nodes. Data is replicated for fault tolerance, typically three replicas per block.
- **Key Features**:
    - **Master-Slave Architecture**: HDFS operates with a **NameNode** (master) and **DataNodes** (slaves). The NameNode manages metadata (file structure and block locations), while DataNodes store actual data blocks.
    - **Fault Tolerance**: Data is replicated across nodes to ensure resilience to node failures.
    - **Write-Once, Read-Many**: HDFS is optimized for batch read access rather than frequent write access.

## **MapReduce**

- **Definition**: MapReduce is a programming model for processing and generating large datasets in parallel across a distributed cluster of computers. It divides tasks into two phases: **Map** and **Reduce**.
- **Key Features**:
    - **Map Phase**: Involves processing input data (usually stored in HDFS), where the input is split into chunks, and each chunk is processed by a **Mapper**. Mappers output key-value pairs.
    - **Shuffle and Sort**: After the Map phase, the system redistributes and sorts the key-value pairs based on the keys, ensuring that all values for a given key are grouped together.
    - **Reduce Phase**: Involves aggregating or summarizing the grouped data, where the **Reducer** processes the data and outputs a final result.
    - **Fault Tolerance**: If a task fails, Hadoop retries the failed task on another node, ensuring job completion.

## **YARN (Yet Another Resource Negotiator)**

- **Definition**: YARN is the resource management layer for Hadoop, introduced to separate the job execution and resource management in Hadoop 2.x. It dynamically allocates resources to applications running on a cluster and coordinates the scheduling of tasks across the nodes.
- **Key Features**:
    - **ResourceManager**: Manages and allocates resources to applications running in the cluster.
    - **NodeManager**: Monitors the resources on each node and reports to the ResourceManager.
    - **ApplicationMaster**: Manages the lifecycle of a single application, including job scheduling and resource negotiation with the ResourceManager.
    - **Scalability**: YARN allows Hadoop to support a variety of processing frameworks (e.g., MapReduce, Apache Spark) beyond just MapReduce.

## **Hadoop Ecosystem**

- **Definition**: Hadoop is not just a single framework, but a collection of technologies that extend its capabilities for various data processing tasks. Key components include:
    - **Hive**: A data warehouse system that provides SQL-like querying capabilities for large datasets stored in HDFS.
    - **Pig**: A high-level platform for creating MapReduce programs, designed to handle complex transformations and large-scale data processing.
    - **HBase**: A distributed NoSQL database built on top of HDFS, optimized for random, real-time read/write access to large datasets.
    - **ZooKeeper**: A coordination service for distributed systems, providing synchronization, configuration, and naming services across the Hadoop ecosystem.
    - **Oozie**: A workflow scheduler that coordinates the execution of jobs in Hadoop.
    - **Sqoop**: A tool for efficiently transferring bulk data between Hadoop and relational databases.
    - **Flume**: A distributed service for collecting, aggregating, and moving large amounts of log data into HDFS.

## Performance

> …
> 

## Instalation

| **Binary** | **Description** |
| --- | --- |
| `hdfs` | The command-line interface for interacting with the Hadoop Distributed File System (HDFS). Allows for managing files, directories, and permissions in the HDFS. |
| `yarn` | The command-line tool for interacting with YARN (Yet Another Resource Negotiator). It manages resources and schedules tasks for processing data. |
| `mapred` | The command-line interface for running and managing MapReduce jobs in the Hadoop ecosystem. |
| `hadoop` | A general-purpose command-line tool that can be used to run Hadoop commands, including starting the cluster, copying data, and running jobs. |
| `hdfs dfs` | A subcommand of `hdfs`, it is used for performing file system operations on HDFS such as copying files, listing directories, setting permissions, etc. |
| `hdfs fsck` | Checks the health of the HDFS filesystem by performing a file system consistency check. |
| `hdfs namenode` | Starts the HDFS NameNode service, which is the master node responsible for managing metadata and coordinating access to HDFS files. |
| `hdfs datanode` | Starts the HDFS DataNode service, which stores the actual data blocks and serves them to clients. |
| `yarn resourcemanager` | Starts the YARN ResourceManager service, which is responsible for managing computing resources and scheduling jobs across the cluster. |
| `yarn nodemanager` | Starts the YARN NodeManager service, which manages resources and task execution on individual nodes. |
| `hadoop jar` | Runs a Hadoop job, typically a MapReduce job, packaged in a `.jar` file. |
| `hadoop fs` | A general-purpose filesystem command-line interface that can interact with various file systems (not just HDFS). |
| `hdfs balancer` | A tool to balance the distribution of data blocks across DataNodes to improve resource utilization. |
| `hdfs dfsadmin` | Admin tool for managing the HDFS file system, used for checking status, setting quotas, and managing safe modes. |

## Uses

| **Use Case** | **Description** | **Industry** |
| --- | --- | --- |
| **Big Data Processing** | Handles massive volumes of structured, semi-structured, and unstructured data across clusters. | Data Analytics, Finance, Telecom |
| **Data Warehousing** | Used as a data repository to store and manage large-scale datasets for querying and analysis. | Retail, Finance, E-commerce |
| **Batch Processing** | Processes large data sets in batches (MapReduce) to perform analytics, filtering, and aggregation. | Any industry handling big data |
| **Log and Event Analytics** | Analyzes server logs, application logs, and events to gain insights or monitor performance. | IT, E-commerce, Media |
| **Fraud Detection** | Detects anomalies in large data sets, such as financial transactions or user behaviors. | Finance, Banking, E-commerce |
| **Machine Learning** | Runs distributed machine learning algorithms on large datasets using frameworks like Mahout. | Healthcare, Marketing, IT |
| **Data Lake** | Provides a scalable, cost-effective repository for raw data, storing it in any format. | Media, Retail, Finance |
| **Recommendation Engines** | Powers personalized recommendation systems by processing user data and behavior at scale. | E-commerce, Media, Social Media |
| **Sentiment Analysis** | Analyzes large sets of text data from sources like social media, reviews, or surveys to extract opinions and trends. | Marketing, Media, Social Media |
| **Genomic Data Processing** | Handles and processes vast amounts of genomic data for research and healthcare analysis. | Healthcare, Research |
| **Financial Market Analysis** | Processes large volumes of real-time and historical stock data for market analysis and prediction. | Finance, Trading |
| **Clickstream Data Analysis** | Analyzes web user behavior data, such as click paths and interactions, to optimize web experiences. | E-commerce, Media, Marketing |
| **Video and Image Processing** | Handles large-scale processing of video and image data for tasks such as recognition or compression. | Media, Security |
| **Network Traffic Analysis** | Monitors and analyzes network traffic data to detect patterns, optimize performance, or find threats. | IT, Telecom, Security |
| **Retail Analytics** | Analyzes sales, inventory, and customer data to identify trends and optimize operations. | Retail, E-commerce |
| **Customer Churn Prediction** | Uses historical data to predict and reduce customer churn by identifying at-risk customers. | Telecom, Finance, E-commerce |
| **Risk Management** | Processes large amounts of financial data to identify and manage risks such as credit defaults. | Banking, Insurance |
| **Energy Consumption Analytics** | Analyzes data from sensors and smart grids to optimize energy usage and efficiency. | Utilities, Renewable Energy |
| **Supply Chain Optimization** | Improves supply chain operations by analyzing data from inventory, transportation, and logistics. | Manufacturing, Retail, Logistics |

## References

- [Hadoop Internals](http://ercoppa.github.io/HadoopInternals/)
- https://hadoop.apache.org/
- https://en.wikipedia.org/wiki/Apache_Hadoop
- [Hadoop Internals - YongChul Kwon](https://courses.cs.washington.edu/courses/cse344/11sp/lectures/cse344-guest-yckwon.pdf)
- https://vutr.substack.com/p/i-spent-8-hours-reading-the-paper-523
- https://github.com/dbremont/hadoop-docker/tree/main
- Borthakur, D. (2007). The hadoop distributed file system: Architecture and design. Hadoop Project Website.
- Gupta, M. K., Pandey, S. K., & Gupta, A. (2022, April). HADOOP-An Open Source Framework for Big Data. In 2022 3rd International Conference on Intelligent Engineering and Management (ICIEM) (pp. 708-711). IEEE.
- Shvachko, K., Kuang, H., Radia, S., & Chansler, R. (2010, May). The hadoop distributed file system. In 2010 IEEE 26th symposium on mass storage systems and technologies (MSST) (pp. 1-10). Ieee.