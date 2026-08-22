# Discourse Case Study

## Build

```bash
git clone https://github.com/discourse/discourse.git
cd discourse
cp samples/standalone.dev.yml docker-compose.override.yml
docker compose up --build
```

## 🔧 Common Commands

```bash
# Enter the Rails console
docker compose exec web rails c

# Run tests
docker compose exec web bundle exec rspec

# Run Ember JS client in hot-reload mode
docker compose exec web bin/dev
```

## Debug

> ...

## Performance Test

> ...

## Architecture

[] Interface -> "Ember JS"
[] Back-End  ->  Rails, ...

## Next Steps

[] Study Ember.js

## References

- [Discourse](https://en.wikipedia.org/wiki/Discourse_(software))
- [Discourse Docker](https://github.com/discourse/discourse_docker)
- [Discourse Source Code](https://github.com/discourse/discourse)
- [Ruby Language](https://righteous-guardian-68f.notion.site/Ruby-Language-257f2cbe63894ac3bc3257f1c4f8de3b?source=copy_link)
- [Ember.js](https://righteous-guardian-68f.notion.site/Ember-js-204c0f5171ec80d2aed8ead5b52f8fa1?source=copy_link)
- [Docker](https://www.notion.so/Docker-77672b18bb7046f1b5635dcee37cb1af?source=copy_link)
- [Node JS](https://www.notion.so/NodeJS-dbfd4d8f45d440ae909695dfe8c33107?source=copy_link)
- [Install Discourse for development using Docker](https://meta.discourse.org/t/install-discourse-for-development-using-docker/102009)
