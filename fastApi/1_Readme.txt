We will be creating a fully featured API which will contain:
1. authentication
2. crud operations
3. schema validations
4. documentation - its very important in APIs to have a proper documentation.

We'll also cover tools which will be needed to build Robust and Complete API, such as:
->   SQL
        -> generating DB schemas
        -> primary keys
        -> foreign keys
        -> table constraints
        -> creating SQL queries to grab exactly what i need.
        -> integrating SQL DBs in APIs via 2 way:
                        -> raw SQL queries
                        -> ORMs
-> DB migration tools:
        -> alembic = allows us to do 'incremental changes' to DB schema to track changes.
-> Postman = to construct HTTP packets (testing)
-> Testing
        -> automation integration tests
-> Deployment
        -> Cloud Hosting
                -> setting up nginx to act as Reverse Proxy.
                -> setting up firewall to block all non-http requests.
                -> setting up SSL for handling HTTPS requests.
        -> Heroku
-> Docker
        -> dockerizing API
-> CI/CD pipelines via GitHub Actions


Tech Stack
1. Python
2. FastAPI
    -> its really about building APIs.
    -> how fast u can build APIs.
    -> well auto-documentation for API + 'Interactive' docs (send http requests).
3. SQL - PostGres [it does not matter what kind of DB u use.]
4. ORM - SQL Alchemy