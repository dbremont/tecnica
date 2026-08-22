# Oracle

String Operations

## Instalation

```bash
docker run -d --name oracle19c \
  -p 1521:1521 -p 5500:5500 \
  -e ORACLE_PASSWORD=$PASS \
  gvenzl/oracle-xe
```

url : `jdbc:oracle:thin:@//localhost:1521/XE`

user: system
pass: $PASS

Oracle

- Case Sensitive: Sensitive
- String Quotes: Single Only

Check support for internalization.

Support for colation.

Read the chapter of a databse book.

DBMS Random https://stackoverflow.com/questions/1568630/generating-random-number-in-each-row-in-oracle-query

## QA

### What do we mean by an Schema in Oracle? What is the different with Scheme in other database systems?

> A logical namespace owned by a single **database user** that contains and organizes database objects.

In Oracle’s internal architecture:

- A schema is not a standalone object type.
- A schema is implicitly created when a user is created.
- The schema name is identical to the username.
- It exists as a logical container for objects owned by that user.

> In Oracle Database, objects are uniquely ownership-bound to a single schema (forming disjoint ownership partitions), while cross-schema references introduce directed privilege and dependency edges that require explicit authorization, yielding a layered access/dependency graph rather than a hierarchical tree structure.

There is not create schema.

> In Oracle Database a schema is an ownership-bound logical namespace that is structurally inseparable from a database user (schema ≡ user and exists implicitly as the set of objects whose `OWNER` equals that user), whereas in systems like PostgreSQL and Microsoft SQL Server a schema is an independent, first-class namespace object decoupled from principals, allowing multiple schemas per user and explicit namespace-level authorization and resolution control.

## References

- https://docs.oracle.com/en/database/oracle/oracle-database/19/sqlrf/Format-Models.html#GUID-DFB23985-2943-4C6A-96DF-DF0F664CED96
- https://docs.oracle.com/en/database/oracle/oracle-database/19/refrn/NLS_TIMESTAMP_FORMAT.html#GUID-1070C91E-6C9D-4FAF-BD58-7880DBED9899
- https://www.techonthenet.com/oracle/functions/to_date.php
- Oracle functions to_char, extract, to_date, to_timestamp, …
- https://www.oracletutorial.com/oracle-date-functions/oracle-to_date/
- https://github.com/wnameless/docker-oracle-xe-11g
- https://stackoverflow.com/questions/67805311/oracle-database-installation-on-ubuntu-18-04
