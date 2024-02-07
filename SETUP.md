Depois de criar o RDS com PostgreSQL, faça login no banco e execute a seguinte query:
```sql
CREATE DATABASE todo_list;
CREATE TABLE todos (
    id SERIAL PRIMARY KEY,
    task TEXT NOT NULL,
    completed BOOLEAN NOT NULL DEFAULT FALSE
);
```