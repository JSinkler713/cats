1. Drop the database
2. Recreate the database
    `$ psql postgres`
    `postgres=# DROP DATABASE database_name_here;`
    `postgres=# CREATE DATABASE database_name_here;`
    OR 
    `$ deletedb name_of_database`
    `$ createdb name_of_database`

3. Run migrations (to build tables, columns, etc.)
4. Add in some more dummy data
