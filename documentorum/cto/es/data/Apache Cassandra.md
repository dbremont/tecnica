# Apache Cassandra

> **Apache Cassandra** is a highly scalable, distributed **NoSQL** database designed to handle large amounts of data across many commodity servers, providing high availability with no single point of failure.
> 

QA:

- How to set up a Cassandra Cluster in docker?

## Index

## Install, Run , Test & Use

> …
> 

```bash
docker run --name cassandra -d -p 9042:9042 cassandra:latest
pip install cassandra-driver
```

```python
from cassandra.cluster import Cluster

# Connect to the Cassandra cluster
cluster = Cluster(['127.0.0.1'])  # Assuming Cassandra is running on localhost
session = cluster.connect()

# Create a keyspace (database) if not exists
session.execute("""
    CREATE KEYSPACE IF NOT EXISTS my_keyspace
    WITH replication = {'class': 'SimpleStrategy', 'replication_factor': 1}
""")

# Switch to the keyspace
session.set_keyspace('my_keyspace')

# Create a table
session.execute("""
    CREATE TABLE IF NOT EXISTS users (
        id UUID PRIMARY KEY,
        name text,
        age int
    )
""")

# Insert data into the table
from uuid import uuid4
session.execute("""
    INSERT INTO users (id, name, age) VALUES (%s, %s, %s)
""", (uuid4(), 'Alice', 30))

# Query data
rows = session.execute("SELECT * FROM users")
for row in rows:
    print(f"ID: {row.id}, Name: {row.name}, Age: {row.age}")

# Close the session and cluster connection
cluster.shutdown()

```

## **CQL (Cassandra Query Language)**

> SQL, like SQL, is explicitly used to interact with the Apache Cassandra NoSQL database.
> 

## References

- https://en.wikipedia.org/wiki/Apache_Cassandra
- https://cassandra.apache.org/_/index.html
- https://github.com/apache/cassandra
- https://news.ycombinator.com/item?id=9308221
- https://www.datastax.com/blog/lightweight-transactions-cassandra-20
- https://nosql.mypopescu.com/post/17940621304/dealing-with-jvm-limitations-in-apache-cassandra
- https://www.datastax.com/blog/tools-testing-cassandra
- https://www.youtube.com/watch?v=OnG1FCr5WTI
- https://www.pingcap.com/