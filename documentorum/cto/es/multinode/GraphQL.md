# GraphQL

> GraphQL is a query language for APIs developed by Meta. It provides a complete description of the data in the API and gives clients the power to ask for exactly what they need.
> 

## Index

## Features

GraphQL is a query language and runtime that offers several key features, providing flexibility and efficiency in data fetching and manipulation. Here are some notable features of GraphQL:

- **Strong Typing**: A well-defined schema allows precise data modeling and ensures consistent communication between clients and servers.
- **Declarative Queries**: Clients specify exactly what data they need, avoiding over-fetching or under-fetching.
- **Single Request for Multiple Resources**: Fetch related data in one request, reducing round trips and addressing issues like the N+1 problem.
- **Introspection**: Query the schema itself, enabling automatic documentation, tooling, and API exploration.
- **Nested Queries**: Request deeply related data in a single query, improving efficiency and readability.
- **Type Validation**: Queries are validated against the schema at execution time, catching errors early.
- **Real-time Updates**: Subscriptions allow clients to receive real-time data via persistent connections.
- **Efficient Resolving & Caching**: Batch and cache data requests to optimize performance.
- **Versioning Support**: APIs can evolve without breaking existing clients.
- **Rich Ecosystem**: A growing community and diverse tooling make adoption easier across languages and platforms.

## Anatomy

> GraphQL is a query language for APIs and a runtime for executing those queries with your existing data. It provides a more efficient and flexible alternative to REST.
> 

The core components of GraphQL include:

### 🔧 **Schema**

Defines the structure of the API — what queries and mutations are available and the types they return or accept.

- **Types**: Define object shapes (e.g., `type User`, `type Post`).
- **Scalars**: Basic data types (`Int`, `Float`, `String`, `Boolean`, `ID`).
- **Enums**: Fixed sets of values.
- **Interfaces & Unions**: Polymorphic types.
- **Input Types**: Used for arguments, especially for mutations.

### 📥 **Query**

Specifies **what data the client wants**. The server responds **only with the data requested**, nothing more.

```graphql
query {
  user(id: "1") {
    name
    email
  }
}

```

### ✏️ **Mutation**

Used to **modify data** (create, update, delete). Mutations can also return values.

```graphql
mutation {
  addUser(name: "Alice", email: "alice@example.com") {
    id
  }
}

```

### 🔄 **Subscription**

Keeps clients updated in **real time** via a WebSocket connection (e.g., chat messages, notifications).

```graphql
subscription {
  messageSent {
    content
    sender
  }
}

```

### 💡 **Resolver Functions**

Functions that connect queries, mutations, or fields in the schema to the underlying data sources (e.g., databases, APIs).

```
const resolvers = {
  Query: {
    user: (_, { id }) => getUserById(id)
  }
}

```

### 🌐 **Execution Engine**

Takes a query and executes it based on:

- The GraphQL schema
- Resolver functions
- Inputs provided by the client

### 🔒 **Context**

A shared object accessible to all resolvers during a request, typically used for:

- Authentication
- Data loaders
- Shared services or DB connections

## ⚙️ Execution Engine

The **Execution Engine** is the internal logic of a GraphQL server that **interprets and resolves** a query using the schema and resolvers.

🔁 Lifecycle of Execution

Here’s how the execution typically works:

1. **Parsing**
    - The raw query string is parsed into an **Abstract Syntax Tree (AST)**.
2. **Validation**
    - The AST is checked against the **schema** to ensure that the query is syntactically and semantically correct.
    - Example: is `user(id: "1")` a valid query? Does `user` exist in the schema?
3. **Execution**
    - Walk the AST and **invoke resolvers** for each field, recursively.
    - Execution is **depth-first** and **field-by-field**.
    - Results are assembled into the final response.

🤖 How It Executes Fields

Each field in a GraphQL query is resolved by a **resolver function**, either:

- Custom (user-defined)
- Default (auto-resolves fields by matching object properties)

For a query like:

```graphql
{
  user(id: "1") {
    name
    posts {
      title
    }
  }
}

```

The engine:

- Calls `user(id: "1")` resolver → gets a `User` object.
- Then `name` resolver on that `User`.
- Then `posts` resolver (might be async).
- Then `title` for each post.

Execution is **parallelized at each field level** unless resolvers block (e.g., if one resolver depends on the result of another).

🛑 Error Handling

Errors can occur in resolvers. Execution continues for sibling fields unless explicitly aborted.

## 🧰 Context

The **context** is a special object **created per request** and **passed to every resolver**. It's like a shared workspace or "backpack" for the request.

🔍 Purpose

The context is used for:

- **Authentication / Authorization**
    - Attach user info to context so resolvers can check permissions.
- **Database connections / ORM sessions**
- **DataLoaders** (for batching and caching)
- **External service clients (REST, gRPC, etc.)**
- **Custom logic or request-scoped metadata**

🛠️ Example (Node.js with Apollo Server)

```
const server = new ApolloServer({
  typeDefs,
  resolvers,
  context: async ({ req }) => {
    const token = req.headers.authorization || "";
    const user = await getUserFromToken(token);
    return {
      user,
      db,
      loaders: createLoaders()
    };
  }
});

```

Then in a resolver:

```
const resolvers = {
  Query: {
    me: (_, __, context) => {
      if (!context.user) throw new AuthenticationError("Not logged in");
      return context.user;
    }
  }
};

```

🧵 Context Is Scoped Per Request

This means:

- It’s **safe to store request-level state**.
- It’s **isolated** — no data leaking between requests.
- You can add logging IDs, trace data, or even request timestamps.

## 🛠️ **Tools and Libraries**

Common tools in a GraphQL stack:

- **Apollo Server/Client**
- **GraphQL.js**
- **Relay**
- **GraphQL Yoga**
- **Hasura, PostGraphile** (auto-generated GraphQL APIs)

## References

- [GraphQL kinda sucks](https://news.ycombinator.com/item?id=32366759)
- [Why not use GraphQL? (wundergraph.com)](https://news.ycombinator.com/item?id=25014582)
- [Pg_GraphQL: A GraphQL Extension for PostgreSQL (supabase.com)](https://news.ycombinator.com/item?id=29430720)
- [Principled GraphQL (principledgraphql.com)](https://news.ycombinator.com/item?id=19147742)
- [GraphQL: A data query language](https://engineering.fb.com/2015/09/14/core-data/graphql-a-data-query-language/)
- [GraphQL](https://www.wikiwand.com/en/GraphQL)