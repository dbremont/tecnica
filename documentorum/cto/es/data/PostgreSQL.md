# PostgreSQL

> Storage Model: Investigate the storage model for indexes; relations; etc.
> 

![](https://i.ytimg.com/vi/Hm_Q4_mz3UA/maxresdefault.jpg)

QA:

- Which is the storage format used to store b-tree? https://www.postgresql.org/docs/current/btree.html https://github.com/postgres/postgres/blob/master/src/backend/access/nbtree/README https://dba.stackexchange.com/questions/111603/how-does-postgres-make-its-b-tree-index
- How many **storage models** does **PostgreSQL** use? [How many **storage models** does **PostgreSQL** use?](PostgreSQL%20c3742c0a3fb54745906235947e3aa5b7.md)

## Index

```bash
# General
docker run --name some-postgres -e POSTGRES_DB=appdb -e POSTGRES_USER=user -e POSTGRES_PASSWORD=pass -p 5432:5432 -d postgres

# For Instance
docker run --name some-postgres -e POSTGRES_DB=appdb -e POSTGRES_USER=user -e POSTGRES_PASSWORD=pass -p 5432:5432 -d postgrest:13-alpine

```

**PostgreSQL** has a unique architecture that allows it to use multiple processes and threads to perform different tasks. This architecture is based on the **PostgreSQL** master process, which coordinates communication between the various **PostgreSQL** worker processes.

The master process manages connections from client System Callsapplications and routes SQL queries to the appropriate worker process. The worker processes are responsible for executing the SQL queries and returning the results to the master process, which sends the results back to the client application.

Communication between the master and worker processes uses interprocess communication (IPC) mechanisms such as shared memory, semaphores, and message queues. **PostgreSQL** uses a technique called shared memory to provide fast and efficient communication between the master process and the worker processes.

Shared memory is a memory segment that can be accessed by multiple processes simultaneously. In **PostgreSQL**, the shared memory segment stores data structures such as the shared buffer pool, the locking information, and the communication channels between the master and worker processes. The master and worker processes can access this shared memory segment to communicate with each other.

In addition to shared memory, **PostgreSQL** uses other IPC mechanisms, such as semaphores and message queues, to synchronize and communicate between processes. For example, semaphores coordinate access to shared resources, such as the shared buffer pool, while message queues send messages between processes.

In summary, **PostgreSQL** uses a combination of shared memory, semaphores, and message queues to enable communication between the master process and the worker processes. This architecture allows **PostgreSQL** to handle multiple client connections and perform various tasks simultaneously, making it a scalable and efficient database management system.

## On Contributing to Postgresql

In my personal experience, reviewing other people’s code is a good starting point. Firstly, IMO this is one of the most valuable contributions, since the community is always short on reviewers. Secondly, in the process, you will learn what the rest of the community is working on, which patches have a good chance of being accepted, and the implementation details of the system.

Additionally, I would like to recommend the following materials for self-study:

- https://www.amazon.com/Database-System-Concepts-Abraham-Silberschatz/dp/1260084507/ ** Especially the chapter available online about PostgreSQL
- https://www.youtube.com/playlist?list=PLSE8ODhjZXjZaHA6QcxDfJ0SIWBzQFKEG
- https://www.timescale.com/blog/how-and-why-to-become-a-postgresql-contributor/

I would second the recommendation to help with patch reviewing because it is one of the most valuable contributions you can make to the project as well as a good way to start to build relationships with other contributors, which will be helpful the next time they are tearing apart one of your patches ;-)

In addition, two other resources to be aware of: * Paul Ramsey has a really nice write up on his thoughts on getting started hacking Postgres: http://blog.cleverelephant.ca/2022/10/postgresql-links.html

- I suspect you may have seen these, but in case not, the wiki has several key pages to be aware of, which are linked to from https://wiki.postgresql.org/wiki/Development_information

References: - http://blog.cleverelephant.ca/2022/10/postgresql-links.html, - https://wiki.postgresql.org/wiki/Development_information

Goal:

- What happens when a connection is not closed?
- Connection Pool
- Compile  Postgrest
- Debug Postgres
- Benchmark  Postgres
- PostgrestRest
- How transaction works?
- How loggins works? / [https://dbdb.io/db/leveldb](https://dbdb.io/db/leveldb)
- ...

## Install

```bash
sudo apt-get install build-essential libreadline-dev zlib1g-dev flex bison
./configure --prefix=/home/dbremont/Code/postgres/out/ --enable-debug CFLAGS="-O0 -g" #  --prefix instalation path
make
make install
```

```jsx
    6902 text files.
    6686 unique files.                                          
    2274 files ignored.

github.com/AlDanial/cloc v 1.90  T=6.00 s (775.4 files/s, 483589.5 lines/s)
---------------------------------------------------------------------------------------
Language                             files          blank        comment           code
---------------------------------------------------------------------------------------
C                                     1504         181173         373316         903105
PO File                                453         171387         211050         511238
SQL                                    748          28669          21841         116119
C/C++ Header                           941          18197          61502         100457
Perl                                   295          11442          10316          51121
XML                                      3              4             15          30922
Bourne Shell                            34           3127           2816          20908
yacc                                    10           2876           3100          20817
Meson                                  275           1945           1171          10794
make                                   312           2191           2281           7641
lex                                     13           1119           2231           5447
m4                                      13            614            154           4534
XSLT                                    10            276            224           1876
C++                                      3            161            268            662
YAML                                     2            141            166            551
Python                                   8            157            137            416
SVG                                      3              0             76            416
JSON                                     1              0              0            144
CSS                                      1             37             14            131
D                                        1             14             14             66
Assembly                                 2             14             38             44
Windows Resource File                    2              3              1             33
Bourne Again Shell                       1             21              6             32
Lisp                                     1              1              1             17
CSV                                      5              0              0             16
Markdown                                 1              5              0             16
IDL                                      8              0              0              8
Windows Message File                     1              0              0              5
Windows Module Definition                1              0              1              4
sed                                      1              2             10              3
---------------------------------------------------------------------------------------
SUM:                                  4653         423576         690749        1787543
---------------------------------------------------------------------------------------
```

## Run

```bash
./bin/initdb data # init
./bin/postgres -D data # run
```

## Debug

```bash
# Remember pg create a new 'process'  to serve every connection.
# So you need to find the 'right process' that is serving your connectión.
sudo gdb -p <pid> # PG pid
```

## Architecture

> A PostgreSQL instance runs as a dedicated server process.
> 

> **PostgreSQL** has a unique architecture that allows it to use multiple processes and threads to perform different tasks. This architecture is based on the **PostgreSQL** master process, which coordinates communication between the various **PostgreSQL** worker processes.
> 

> The **master process manages connections** from client applications and routes SQL queries to the appropriate worker process. The worker processes are responsible for executing the SQL queries and returning the results to the master process, which sends the results back to the client application.
> 

> **Communication** between the master and worker processes uses interprocess communication (IPC) mechanisms such as shared memory, semaphores, and message queues. **PostgreSQL** uses a technique called shared memory to provide fast and efficient communication between the master process and the worker processes.
> 

> **Shared memory** is a memory segment that can be accessed by multiple processes simultaneously. In **PostgreSQL**, the shared memory segment stores data structures such as the shared buffer pool, the locking information, and the communication channels between the master and worker processes. The master and worker processes can access this shared memory segment to communicate with each other.
> 

```bash
 › ps -aux | grep post
dbremont 1174161  0.0  0.0 207300 21760 pts/0    t+   20:48   0:00 ./bin/postgres -D data
dbremont 1174162  0.0  0.0 207592 18792 ?        Ss   20:48   0:00 postgres: checkpointer 
dbremont 1174163  0.0  0.0 207432  4840 ?        Ss   20:48   0:00 postgres: background writer 
dbremont 1174165  0.0  0.0 207432  7528 ?        Ss   20:48   0:00 postgres: walwriter 
dbremont 1174166  0.0  0.0 208884  6888 ?        Ss   20:48   0:00 postgres: autovacuum launcher 
dbremont 1174167  0.0  0.0 208892  5992 ?        Ss   20:48   0:00 postgres: logical replication launcher 
dbremont 1175768  0.0  0.0 209800 15764 ?        Ss   21:04   0:00 postgres: dbremont postgres 127.0.0.1(54242) idle
dbremont 1175770  0.0  0.0 211344 17812 ?        Ss   21:04   0:00 postgres: dbremont postgres 127.0.0.1(54258) idle
dbremont 1176121  0.0  0.0 210316 18964 ?        Ss   21:08   0:00 postgres: dbremont prueba 127.0.0.1(44892) idle
dbremont 1176123  0.0  0.0 211408 23580 ?        Ss   21:08   0:00 postgres: dbremont prueba 127.0.0.1(44894) idle
dbremont 1176125  0.0  0.0 209800 18068 ?        Ss   21:08   0:00 postgres: dbremont prueba 127.0.0.1(44902) idle
dbremont 1176127  0.0  0.0 209800 18196 ?        Ss   21:08   0:00 postgres: dbremont prueba 127.0.0.1(44910) idle
dbremont 1176129  0.0  0.0 209800 18196 ?        Ss   21:08   0:00 postgres: dbremont prueba 127.0.0.1(44916) idle
dbremont 1176132  0.0  0.0 210988 22348 ?        Ss   21:08   0:00 postgres: dbremont prueba 127.0.0.1(44920) idle
dbremont 1177741  0.0  0.0  11752  2688 pts/4    S+   21:22   0:00 grep --color=auto --exclude-dir=.bzr --exclude-dir=CVS --exclude-dir=.git --exclude-dir=.hg --exclude-dir=.svn --exclude-dir=.idea --exclude-dir=.tox post

pstree -p 1174161
postgres(1174161)─┬─postgres(1174162)
                  ├─postgres(1174163)
                  ├─postgres(1174165)
                  ├─postgres(1174166)
                  ├─postgres(1174167)
                  ├─postgres(1175768)
                  ├─postgres(1175770)
                  ├─postgres(1176121)
                  ├─postgres(1176123)
                  ├─postgres(1176125)
                  ├─postgres(1176127)
                  ├─postgres(1176129)
                  └─postgres(1176132)
```

## Internals

PostgreSQL is a powerful open-source relational database management system with many features and capabilities. Here are some of the main parts of PostgreSQL:

- **Query Processor**: The PostgreSQL query processor is responsible for parsing, analyzing, and optimizing SQL queries submitted by clients. It creates an execution plan that specifies how the query will be executed.
- **Storage Manager**: The storage manager is responsible for managing the storage and retrieval of data from disk. It manages the physical data files and provides data caching, indexing, and transaction management features.
- **Relational Engine**: The relational engine manages the logical data representation in the database. It provides features such as data modeling, schema management, and integrity constraints.
- **Concurrency Control Manager**: The concurrency control manager manages concurrent access to data by multiple clients. It ensures that transactions are executed serializable and provides features such as locking, transaction isolation levels, and deadlock detection.
- **Recovery Manager**: The recovery manager ensures that the database remains consistent during system failures. It provides features such as logging and rollback, which allow the database to recover from losses and maintain data integrity.
- **Security Manager**: The security manager manages users' and applications' access to the database. It provides features such as authentication, authorization, and data encryption to ensure data privacy and security.
- **Backup and Restore Manager**: The backup and restore manager creates and restores database backups. It provides features such as incremental and differential backups, allowing for point-in-time data recovery.
- **Replication Manager**: The replication manager replicates data across multiple nodes in a distributed database environment. It provides replication topologies, conflict resolution, and data synchronization features.
- **PL/pgSQL**: PL/pgSQL is a procedural language used to write stored procedures, functions, and triggers in PostgreSQL. It provides features such as looping, branching, and exception handling and allows for complex business logic to be implemented in the database.
- **Extensions**: PostgreSQL provides a wide range of extensions that can be used to add additional functionality to the database. These extensions can be developed by the community or by third-party developers and can add features such as GIS, full-text search, and JSON support.
- **Monitoring and Management**: PostgreSQL provides a range of monitoring and management features to allow administrators to monitor the health and performance of the database. These features may include tools for monitoring system resources, identifying performance bottlenecks, and tuning database parameters.

## Indexing

```csharp
CREATE INDEX idx_hash ON table_name USING HASH (column_name);
CREATE INDEX idx_hash ON table_name USING <Index Tiype> (column_name);
```

| **Index Type** | **Description** | **Use Case** |
| --- | --- | --- |
| **B-tree Index (Default)** | Balanced tree structure for ordered data. | Equality and range queries (`=`, `<`, `>`, `BETWEEN`). |
| **Hash Index** | Uses a hash table for indexing. | Fast equality comparisons (`=`). |
| **GIN (Generalized Inverted Index)** | Inverted index for multi-valued data types. | Full-text search, JSONB, arrays, hstore. |
| **GiST (Generalized Search Tree)** | Flexible index for complex data types like geometric and full-text search. | Nearest-neighbor searches, geometric data, and specialized range queries. |
| **SP-GiST (Space-Partitioned GiST)** | Optimized for partitioned space indexing (e.g., quadtrees, k-d trees). | Spatial data and partitioned data queries. |
| **BRIN (Block Range INdexes)** | Indexes ranges of table blocks, used for large, sequential datasets. | Large time-series, log data, or sequential data. |
| **Partial Index** | Index on a subset of table rows based on a condition. | Index a specific subset of rows (e.g., where `column_name IS NOT NULL`). |
| **Expression Index** | Index based on the result of an expression or function applied to columns. | Queries involving expressions or functions (e.g., `LOWER(column_name)`). |
| **Unique Index** | Ensures the uniqueness of the indexed columns. | Automatically created for `UNIQUE` or `PRIMARY KEY` constraints. |
| **Covering Index (Index-Only Scan)** | Index that includes all required columns to answer the query directly from the index. | When queries require a specific set of columns, reducing I/O by using the index instead of the table. |

## How many **storage models** does **PostgreSQL** use?

| **Storage Model** | **Description** | **Use Case** | **Implementation** |
| --- | --- | --- | --- |
| **Heap Storage** | Default storage for table data. Rows are stored without a specific order. | Suitable for tables where no specific order is required. | Data stored in blocks/pages, each containing multiple rows. |
| **Index Storage** | Various index types like B-tree, Hash, GiST, GIN, SP-GiST, BRIN. | Speeds up searches, joins, and range queries. | Indexes are stored separately from the heap in specific index structures. |
| **TOAST (The Oversized-Attribute Storage Technique)** | Handles large data types (e.g., large text or binary fields) that don't fit in a single page. | Used for large text, bytea, or other variable-length types. | Large values are compressed and stored in separate system tables. |
| **Foreign Data Wrappers (FDW)** | Allows connection to external data sources like other databases or file systems. | Integrates PostgreSQL with external systems/data stores. | External data is treated as a regular table, abstracted for querying. |
| **Temporary Storage** | Storage used for temporary tables and indexes during query execution. | Useful for intermediate query results, e.g., in sorting, joins, or aggregations. | Temporary storage is cleared at the end of a session or transaction. |
| **Table Partitioning** | Divides large tables into smaller, manageable partitions. | Optimizes queries by accessing relevant partitions (e.g., for time-series or log data). | Data distributed across multiple partitions based on a key (range or list). |
| **WAL (Write-Ahead Logging)** | Ensures data integrity by recording changes in a log before applying them to the database. | Provides durability and crash recovery. | Changes are first recorded in the WAL log and then applied to the database. |
| **Logical Replication Storage** | Stores changes in a format for logical replication between databases. | High availability and data distribution across systems. | Changes are stored in a logical replication format for propagation to subscribers. |

## References

- [The part of Postgres we hate the most: Multi-version concurrency control (ottertune.com)](https://news.ycombinator.com/item?id=35716963)
- [PostgreSQL DBA](https://roadmap.sh/postgresql-dba)
- [Debugging the Postgres query planner (2018) (gocardless.com)](https://news.ycombinator.com/item?id=32834182)
- [Devious SQL: Message Queuing Using Native PostgreSQL (crunchydata.com)](https://news.ycombinator.com/item?id=30119285)
- [Postgres Insider Terminology](https://www.crunchydata.com/blog/challenging-postgres-terminology)
- [Manage Mailing List](https://lists.postgresql.org/) - [Altenative View](https://postgrespro.com/list)
- [Community](https://www.postgresql.org/community/)
- [awesome-postgres](https://github.com/dhamaniasad/awesome-postgres)
- [Understanding database indexes in PostgreSQL (mastermind.dev)](https://news.ycombinator.com/item?id=35978757)
- [Show HN: Postgres query lock explainer (github.com/admtal)](https://news.ycombinator.com/item?id=35981238)
- [Tuning Postgres and the new insert benchmark, round 3](http://smalldatum.blogspot.com/2023/06/tuning-postgres-and-new-insert.html)
- [Pgvector: Open-source vector similarity search for Postgres](https://news.ycombinator.com/item?id=34966045)
- [PostgreSQL Lock Conflicts](https://postgres-locks.husseinnasser.com/)
- [How to Listen to Database Changes Using Postgres Triggers in Elixir (peterullrich.com)](https://news.ycombinator.com/item?id=36323058)
- [Postgres Locks — A Deep Dive](https://medium.com/@hnasr/postgres-locks-a-deep-dive-9fc158a5641c) - [Comments](https://twitter.com/hnasr/status/1672287201600872448)
- [PostgreSQL reconsiders its process-based model (lwn.net)](https://news.ycombinator.com/item?id=36393030)
- [PostgreSQL Process Architecture](https://medium.com/@hnasr/postgresql-process-architecture-f21e16459907)
- [Implementing System-Versioned Tables in Postgres](https://hypirion.com/musings/implementing-system-versioned-tables-in-postgres)
- https://people.cs.rutgers.edu/~pxk/417/notes/cassandra.html
- Parsing the Postgres protocol – logging executed statements (kviklet.dev)
[https://news.ycombinator.com/item?id=39706582](https://news.ycombinator.com/item?id=39706582)
- PostgreSQL is Enough
[https://gist.github.com/cpursley/c8fb81fe8a7e5df038158bdfe0f06dbb](https://gist.github.com/cpursley/c8fb81fe8a7e5df038158bdfe0f06dbb)
- Ten years of improvements in PostgreSQL's optimizer ([rmarcus.info](http://rmarcus.info/)) / [https://news.ycombinator.com/item?id=40060123](https://news.ycombinator.com/item?id=40060123)
- Handling Data Larger Memory
    - How to get large array from postgres ~70GB of data with minimal RAM usage? / [https://stackoverflow.com/questions/71909885/how-to-get-large-array-from-postgres-70gb-of-data-with-minimal-ram-usage](https://stackoverflow.com/questions/71909885/how-to-get-large-array-from-postgres-70gb-of-data-with-minimal-ram-usage)
    - How spark read a large file (petabyte) when file can not be fit in spark's main memory / [https://stackoverflow.com/questions/46638901/how-spark-read-a-large-file-petabyte-when-file-can-not-be-fit-in-sparks-main](https://stackoverflow.com/questions/46638901/how-spark-read-a-large-file-petabyte-when-file-can-not-be-fit-in-sparks-main)
    - Can Postgres process data larger than installed memory because it leverages File-I/O? / [https://www.reddit.com/r/PostgreSQL/comments/1b4azb0/can_postgres_process_data_larger_than_installed/](https://www.reddit.com/r/PostgreSQL/comments/1b4azb0/can_postgres_process_data_larger_than_installed/)
- https://news.ycombinator.com/item?id=26211895
- [The **LLVM** Compiler Infrastructure](https://www.notion.so/The-LLVM-Compiler-Infrastructure-63fef44f698d4912b814c9bc5436da28?pvs=21)
- https://www.orioledb.com/blog/orioledb-neon-differences
- https://dlt.github.io/blog/posts/introduction-to-postgresql-indexes/
