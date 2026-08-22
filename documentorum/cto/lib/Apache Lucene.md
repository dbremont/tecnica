> Apache Lucene is a high-performance, open-source full-text search library written in Java that provides powerful search and indexing capabilities for a wide range of applications.
> 

- ¿How to serialize an index?
- ¿How to load an index?

## Query Startegies

Here’s a table summarizing Apache Lucene search query strategies:

| **Query Type** | **Description** | **Example Code** |
| --- | --- | --- |
| **Term Query** | Searches for documents containing a specific term in a field. | `Query query = new TermQuery(new Term("field", "value"));` |
| **Boolean Query** | Combines multiple queries using Boolean logic (AND, OR, NOT) for complex search conditions. | `java<br>BooleanQuery.Builder booleanQuery = new BooleanQuery.Builder();<br>booleanQuery.add(new TermQuery(new Term("field", "value1")), BooleanClause.Occur.MUST);<br>booleanQuery.add(new TermQuery(new Term("field", "value2")), BooleanClause.Occur.SHOULD);<br>Query query = booleanQuery.build();<br>` |
| **Phrase Query** | Searches for documents containing a specific sequence of words (phrase) in a field. | `java<br>Query query = new PhraseQuery.Builder()<br> .add(new Term("field", "first"))<br> .add(new Term("field", "second"))<br> .build();<br>` |
| **Wildcard Query** | Searches for documents containing terms that match a wildcard pattern (e.g., `*`, `?`). | `Query query = new WildcardQuery(new Term("field", "term*"));` |
| **Fuzzy Query** | Searches for documents containing terms similar to a given term, useful for handling misspellings. | `Query query = new FuzzyQuery(new Term("field", "term"), 2);` |
| **Range Query** | Searches for documents containing terms within a specified range. | `Query query = IntPoint.newRangeQuery("field", 10, 20);` |
| **Prefix Query** | Searches for documents containing terms that start with a specified prefix. | `Query query = new PrefixQuery(new Term("field", "prefix"));` |
| **Regexp Query** | Searches for documents containing terms that match a regular expression pattern. | `Query query = new RegexpQuery(new Term("field", "pattern.*"));` |
| **Numeric Range Query** | Searches for documents containing numeric values within a specified range. | `Query query = NumericRangeQuery.newIntRange("field", 10, 20, true, true);` |
| **Boosting Query** | Adjusts the relevance score of a query by multiplying its weight. | `Query query = new BoostQuery(new TermQuery(new Term("field", "value")), 2.0f);` |
| **Custom Score Query** | Allows for custom scoring of documents based on a query. | `Query query = new CustomScoreQuery(new TermQuery(new Term("field", "value")));` |
| **Function Query** | Modifies the score of documents based on a function, such as a mathematical function. | `Query query = new FunctionScoreQuery(new MatchAllDocsQuery(), ScoreFunctionFunction);` |
| **Multi-field Query** | Searches across multiple fields with a single query. | `String[] fields = {"field1", "field2"}; Query query = MultiFieldQueryParser.parse(queryString, fields, analyzer);` |
| **DisMax Query** | Finds the maximum score of a set of queries, useful for handling optional queries. | `java<br>Query query = new DisjunctionMaxQuery(Arrays.asList(<br> new TermQuery(new Term("field", "value1")),<br> new TermQuery(new Term("field", "value2"))<br> ), 0.5f);<br>` |
| **BM25 Query** | Uses the BM25 ranking function for scoring documents, effective for many real-world search scenarios. | `// BM25 is implemented in Lucene by default for relevance scoring` |
| **Autocomplete & Suggesters** | Provides autocomplete suggestions based on term frequencies. | `// Use a suggester with a special Index for auto-completion` |

## Binary Representation

> …
> 

## In Memory Representation

> …
> 

Apache Lucene uses various in-memory data structures to efficiently handle indexing and searching. Here is a table summarizing key in-memory data structures used in Lucene:

| **Data Structure** | **Purpose** | **Description** |
| --- | --- | --- |
| **`FieldInfo`** | Field Metadata | Stores metadata about fields in the index, such as field name, type, and whether it's indexed or stored. |
| **`Term`** | Term Representation | Represents a term in the index, consisting of a field name and term text. This is fundamental for searching and indexing. |
| **`Terms`** | Term Collection | Collection of terms for a particular field. It is used to access term data, including term frequency and postings. |
| **`PostingsList`** | Term Occurrences | Holds a list of postings (document IDs) for a specific term, showing which documents contain the term and where. |
| **`PostingsEnum`** | Postings Enumeration | Provides a way to iterate through postings for a term. It helps in retrieving document IDs and term frequencies. |
| **`DocValues`** | Field Values | Holds per-document values for fields. This is used for sorting and faceting operations, and is stored separately from the main index. |
| **`StoredFields`** | Stored Document Fields | Contains the actual stored values of fields for documents. These are retrieved during searches to provide complete document information. |
| **`Norms`** | Normalization Factors | Stores normalization factors for fields. These factors are used to adjust the relevance scores of documents based on field length and other parameters. |
| **`TermVectors`** | Term Frequency and Position | Contains term frequency, position, and offsets for each term in a document. This is useful for features like highlighting and advanced query parsing. |
| **`IndexWriter`** | Indexing Engine | Manages the process of adding, updating, and deleting documents in the index. It handles merging of segments and index optimization. |
| **`IndexReader`** | Index Reading Engine | Provides access to the indexed data for searching. It can be used to create `IndexSearcher` instances for query execution. |
| **`IndexSearcher`** | Search Engine | Performs searches over the index. It uses in-memory data structures to execute queries efficiently and return results. |
| **`Directory`** | Index Storage Abstraction | Represents an abstract storage mechanism for the index. `FSDirectory` and `RAMDirectory` are common implementations for file and in-memory storage. |
| **`SegmentInfo`** | Segment Metadata | Contains information about index segments, including their name, number of documents, and whether they are deleted or not. |
| **`SegmentReader`** | Segment Reader | Reads a specific segment of the index. It interacts with data structures like `Terms`, `PostingsList`, and `DocValues`. |
| **`FieldType`** | Field Definition | Describes the properties of a field, such as whether it is stored, indexed, or tokenized. |

## References

- [Apache Lucene](https://en.wikipedia.org/wiki/Apache_Lucene)
- https://lucene.apache.org/
- https://github.com/apache/lucene

https://lucene.apache.org/core/9_9_1/

- https://lucene.apache.org/core/9_9_1/core/org/apache/lucene/codecs/lucene99/package-summary.html#package.description

https://blog.mikemccandless.com/2011/02/visualizing-lucenes-segment-merges.html

- https://engineeringblog.yelp.com/2021/09/nrtsearch-yelps-fast-scalable-and-cost-effective-search-engine.html
- https://j.blaszyk.me/tech-blog/exploring-apache-lucene-index/
- https://j.blaszyk.me/tech-blog/exploring-apache-lucene-search-and-ranking/

https://j.blaszyk.me/tech-blog/exploring-apache-lucene-scale/