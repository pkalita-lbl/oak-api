# oak-api

Prototype web API backed by oaklib[https://github.com/INCATools/ontology-access-kit].

## Setup

```shell
poetry install
```

Add a [semantic-sql](https://github.com/INCATools/semantic-sql) SQLite database to the root directory.

```shell
cp settings.yaml.example settings.yaml
```

Update `settings.yaml` with the name of your local database.

## Run

```shell
make dev
```

Development server will be running on http://localhost:8000/. Documentation for endpoints can be found at http://localhost:8000/docs.
