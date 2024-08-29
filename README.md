## CRUD - FASTAPI

1. create virtual environment 

```bash
python3.11 -m venv venv
```

2. activate virtual environment 

```bash
source venv/bin/activate
```
3. Installing dependencies from lock file
```bash
poetry install
```
4. Migrating the code with the postgresql 
```bash
cd liquibase/changelog
liquibase update
```
5. To run the code :-
```bash
uvicorn index:app --reload
```

##### If we are getting the error of port are in use :-
```bash
lsof -i:port
kill -9 id
```


