# LevelDB

> **LevelDB** is a fast **key-value** storage library written at Google that provides an ordered mapping from string keys to string values. It is based on concepts from Google's Big Table database system, and its architecture is designed for high performance and efficiency.

## Use Cases

LevelDB is suitable for applications requiring high write throughput and efficient read performance. It is commonly used in scenarios such as:

- Embedded databases
- Caching systems
- Log storage
- Key-value stores

## Build

```bash

# Third Party
- git clone --recurse-submodules https://github.com/google/leveldb.git
- git clone https://github.com/google/googletest.git
- git clone https://github.com/google/benchmark.git 

mkdir build && cd build
cmake -DCMAKE_BUILD_TYPE=Debug ..
cmake --build .
```

```bash
#include <iostream>
#include <cassert>
#include "leveldb/db.h"

// g++ -std=c++11 -g  -o main main.cpp -I/home/dbremont/Code/leveldb/include -L/home/dbremont/Code/leveldb/build -lleveldb -lpthread

int main() {
    leveldb::DB* db;
    leveldb::Options options;
    options.create_if_missing = true;

    // Open the database
    leveldb::Status status = leveldb::DB::Open(options, "testdb", &db);
    assert(status.ok());

    // Write to the database
    std::string key = "key1";
    std::string value = "value1";
    status = db->Put(leveldb::WriteOptions(), key, value);
    assert(status.ok());

    // Read from the database
    status = db->Get(leveldb::ReadOptions(), key, &value);
    assert(status.ok());
    std::cout << "Read value: " << value << std::endl;

    // Close the database
    delete db;

    return 0;
}

```

### Key Components

Here is a table summarizing the key components of LevelDB and their functions:

| **Component** | **Description** | **Function** |
| --- | --- | --- |
| **MemTable** | An in-memory data structure is usually implemented as a skip list. | Temporarily holds writes (put, delete) before they are flushed to disk. |
| **Immutable MemTable** | A MemTable that has been marked as read-only after reaching a specific size. | Converted into an SSTable and written to disk in the background. |
| **SSTables** | Immutable, sorted files stored on disk, organized into levels. | Store key-value pairs in a sorted order for efficient retrieval and compaction. |
| **Write-Ahead Log (WAL)** | A log file where changes are first recorded before being written to the MemTable. | Ensures data durability by logging changes before they are applied to the MemTable. |
| **Compaction** | The process of merging SSTables to maintain the structure and efficiency of levels. | Reclaims storage space, reduces the number of SSTables, and ensures non-overlapping key ranges. |
| **Levels** | Hierarchical organization of SSTables on disk, each with increasing size limits. | Manages data efficiently, optimizes read and write performance, and maintains database health. |
| **Bloom Filters** | Probabilistic data structures are used to test whether an element is a set member. | Speeds up read operations by reducing the number of disk accesses needed to determine key presence. |
| **Comparator** | A function or object is used to define the order of keys. | Ensures that keys are stored and retrieved in a consistent order. |
| **Options** | Configuration parameters for LevelDB. | Allows customization of various aspects of the database, such as cache size, block size, etc. |

## LevelDB Storage Model

> AKA. Files & Format/
> 

### Levels

> In LevelDB, "levels" refer to the hierarchical organization of SSTables (Sorted String Tables) on disk.
> 

Here is a detailed table summarizing the characteristics and functions of each level in LevelDB:

| **Level** | **Characteristics** | **Functions** |
| --- | --- | --- |
| **Level 0** | - Contains newly created SSTables. | - Stores new SSTables from the MemTable. |
|  | - SSTables in this level may have overlapping key ranges. | - No key range overlap restriction, leading to multiple SSTables being checked during reads. |
| **Level 1** | - Contains SSTables with non-overlapping key ranges. | - Ensures that for any given key, only one SSTable needs to be checked, improving read efficiency. |
|  | - Limited in size (e.g., 10 MB). | - Stores compacted SSTables from Level 0, eliminating overlap. |
| **Level 2** | - Larger size limit than Level 1 (e.g., 100 MB). | - Stores compacted SSTables from Level 1, ensuring non-overlapping key ranges. |
|  | - SSTables have non-overlapping key ranges. | - Read efficiency is maintained as key ranges do not overlap within the level. |
| **Level 3** | - Even larger size limit (e.g., 1 GB). | - Continues to store compacted SSTables from the previous level with non-overlapping key ranges. |
|  | - Non-overlapping key ranges. | - Maintains read performance with more data being managed efficiently. |
| **Level 4** | - Further increased size limit. | - Stores more data, maintaining non-overlapping key ranges for efficient read operations. |
|  | - Non-overlapping key ranges. | - Compacting SSTables from Level 3 into larger SSTables. |
| **Level 5** | - Significantly larger size limit, continuing the exponential growth pattern. | - Manages an increasing amount of data with efficient read performance due to non-overlapping key ranges. |
|  | - Non-overlapping key ranges. | - SSTables are compacted and merged into larger, more manageable files. |
| **Level 6** | - Largest level, continuing the exponential growth pattern. | - Manages the largest amount of data, maintaining efficient reads with non-overlapping key ranges. |
|  | - Non-overlapping key ranges. | - Final level for compacted SSTables, ensuring that the database remains performant and space-efficient. |

## Read/Write Path

1. **Write Path**:
    - Writes are first appended to the WAL for durability.
    - Changes are then added to the MemTable.
    - When the MemTable is full, it is converted into an SSTable and written to disk.
2. **Read Path**:
    - Reads first check the MemTable for the key.
    - If not found, the immutable MemTable is checked.
    - Finally, the SSTables are searched, starting from Level 0 and proceeding to higher levels.
    - Bloom filters speed up SSTable searches by reducing unnecessary disk reads.

## LevelDB Performance

Here is a table summarizing the performance considerations in LevelDB:

| **Aspect** | **Consideration** | **Details** |
| --- | --- | --- |
| **Write Performance** | **In-Memory Writes** | Writes are first made to the in-memory MemTable, making write operations fast and efficient. |
|  | **Write-Ahead Log (WAL)** | Changes are logged to the WAL for durability, ensuring data is not lost in case of a crash. |
|  | **Batch Writes** | LevelDB supports batch writes to reduce overhead and improve throughput. |
| **Read Performance** | **MemTable and Immutable MemTable** | Reads first check the MemTable and immutable MemTable, providing fast access to recently written data. |
|  | **SSTables** | Reads then check SSTables on disk, starting from Level 0 and progressing to higher levels. |
|  | **Bloom Filters** | Bloom filters are used to quickly determine if a key is not present in an SSTable, reducing unnecessary disk reads. |
| **Compaction** | **Minor Compaction** | Involves merging the immutable MemTable with existing SSTables in Level 0, keeping data organized. |
|  | **Major Compaction** | Merges SSTables across levels to reclaim space and maintain performance, ensuring non-overlapping key ranges. |
|  | **Compaction Triggers** | Compactions are triggered based on size thresholds and the number of SSTables in a level. |
| **Space Management** | **Efficient Use of Storage** | Compaction processes help in reclaiming space and reducing fragmentation. |
|  | **SSTable Size Management** | SSTables are managed in levels with increasing size limits, optimizing storage usage. |
| **Concurrency** | **Locking Mechanisms** | Fine-grained locking allows for concurrent read and write operations, enhancing performance in multi-threaded environments. |
| **Configuration** | **Options** | Various configuration options (e.g., cache size, block size) allow customization for specific performance needs. |
| **Cache** | **Block Cache** | A configurable in-memory cache for frequently accessed data blocks, reducing disk I/O. |
| **Recovery** | **Fast Recovery** | In case of a crash, recovery is efficient due to the WAL and the organization of SSTables. |

## References

- [https://dbdb.io/db/leveldb](https://dbdb.io/db/leveldb)
- [Skip List](https://www.notion.so/Skip-List-926856edf43a4ab195c455b29fb05592?pvs=21)
- [LSM Tree](https://www.notion.so/LSM-Tree-771df20cad82477582adf82a73d55506?pvs=21)
- [Data Maps (Index)](https://www.notion.so/Data-Maps-Index-a836dc7cad624785ae39d9299df894b1?pvs=21)
- [Augmented Data Structures](https://www.notion.so/Augmented-Data-Structures-b6ba73a0edf1463184bbbf6c1cc0f0f6?pvs=21)
