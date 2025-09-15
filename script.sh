# create files if not exist
touch requirements.txt
touch README.md
touch .gitignore
touch setup.py
touch .env
touch Dockerfile
touch app.py
touch flask-deployment.yaml


# create folders if not exist
mkdir -p data
mkdir -p flipkart
mkdir -p prometheus
mkdir -p static
mkdir -p templates
mkdir -p utils
mkdir -p grafana

# add some basic content to the files if they are empty
touch utils/__init__.py
touch utils/logger.py
touch utils/custom_exceptions.py

touch templates/index.html
touch static/style.css

touch flipkart/__init__.py
touch flipkart/config.py
touch flipkart/data_converter.py
touch flipkart/data_ingestion.py
touch flipkart/rag_chain.py


