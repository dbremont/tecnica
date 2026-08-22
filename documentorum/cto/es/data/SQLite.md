# SQLite

> …
> 

## …

> …
> 

## ETL(Extract Load Transform) con SQLite

1. Fetch the data as CSV,
2. Load data in SQLite,
3. Transfor Data,
4. Export Data to CSV,
5. Use to to generate statements to update the data,
6. Upload the Data.

```bash
-- Normalizarcd ~/Downloads

cat query-create-tables.sql | sqlite3 datos.db 

## .tables.mode csv.import /home/dvictoriano/Downloads/beneficiarios_activos.csv TMP_CLS_CIUDADANO

UPDATE TMP_CLS_CIUDADANO SET COD_ENTIDAD  =  substr('0000000' || COD_ENTIDAD, -11, 11);
```

```sql
SELECT *FROM sqlite_master;
```

## References

- https://www.sqlite.org/datatype3.html
- [SQLite Internals: How The World’s Most Used Database Works](https://www.compileralchemy.com/books/sqlite-internals/)
- [SQLite performance tuning: concurrent reads, multiple GBs and 100k SELECTs/s (phiresky.github.io)](https://news.ycombinator.com/item?id=35547819)
- [SQLite: Past, Present, and Future](https://www.vldb.org/pvldb/vol15/p3535-gaffney.pdf)
- [SQLITE Virtual Machine](https://fly.io/blog/sqlite-virtual-machine/)
- [Overview of FTS5](https://www.sqlite.org/fts5.html)
- [List Of Virtual Tables](https://www.sqlite.org/vtablist.html)
- [ ]  How to copy files over the network? https://news.ycombinator.com/item?id=43856186