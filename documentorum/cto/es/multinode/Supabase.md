# Supabase

> …
> 

QA:

- How to reason deeply about **connection pooling**?
- …

## Run

> …
> 

```bash
docker run -d -p 8000:8000 -p 9443:9443 --name portainer --restart=always -v /var/run/docker.sock:/var/run/docker.sock -v portainer_data:/data portainer/portainer-ce:latest
```

## How to run docker Postgre sql’s files in init?

```bash
# General
docker run --name some-postgres -e POSTGRES_DB=appdb -e POSTGRES_USER=user -e POSTGRES_PASSWORD=pass -p 5432:5432 -d postgres

# For Instance
docker run --name some-postgres -e POSTGRES_DB=appdb -e POSTGRES_USER=user -e POSTGRES_PASSWORD=pass -p 5432:5432 -d postgrest:13-alpine
```

## Security

> Row Level Security (RLS)
> 

## References

- https://github.com/supabase/supabase
- [PostgreSQL](https://www.notion.so/PostgreSQL-c3742c0a3fb54745906235947e3aa5b7?pvs=21)