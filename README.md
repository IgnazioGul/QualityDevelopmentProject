
## Development
Gitflow must be used during development process.
We will use following branches:
- **master** PRODUCTION-READY code
- **develop** for TEST-READY code
- **feature branches** for active feature development (https://devdev.it/guida-gitflow/feature-branch-nuove-funzionalita/).

When a new feature is completed and ready for testing, a pull request to develop must be open.

## Install
python -m venv ./venv

venv\Scripts\activate

pip install -r requirements.txt

## Run 
flask --app qd_project run

