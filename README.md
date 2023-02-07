
  

## Development

Gitflow must be used during development process.

We will use following branches:

-  **master** for PRODUCTION-READY code

-  **develop** for TEST-READY code

-  **feature branches** creted from develop and used for active feature development (https://devdev.it/guida-gitflow/feature-branch-nuove-funzionalita/). 

  

When a new feature is completed and ready for testing, a pull request to develop must be open.

  

## Install

```python -m venv ./venv```

  

```venv\Scripts\activate```

  
```
pip install -r requirements_dev.txt
```
```
pip install -r requirements.txt
```

  

## Run

```py bot.py```

  

## Testing

Add unit-test to ./tests, then run:
```
pytest --cov src tests/ --cov-report=html --cov-fail-under=75
```
Please note that you cannot push a projecy version that has <75% code coverage.
