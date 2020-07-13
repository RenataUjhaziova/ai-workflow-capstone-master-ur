# AI Workflow: An end to end AI pipeline

* **data/cs-train**: Contains all the data to train the model
* **models**: Contains all pre-trained saved models for prediction
* **solution_notebooks**: Contains all the notebooks describing solutions and depicting visualizations
* **templates**: Simple templates for rendering flask app
* **unittest**: It has logger test, API test and model test for testing all the functionalities before deploying to production and for maintenance post deployment
* **Dockerfile**: Contains all the commands a user could call on the command line to assemble the docker image.
* **app.py**: Flask app for creating a user interface /train and /predict APIs in order to train and predict respectively
* **data_ingestion_lib.py**: A collection of functions that will transform the data set into features you can use to train a model.
* **model.py**:  A module having functions for training, loading a model and making predictions



## Reviewing pointers:

Unit tests for the API: unittests/ApiTests.py

Unit tests for the model: unittests/ModelTests.py

Unit tests for the logging: unittests/LoggerTests.py

Run all of the unit tests with a single script: run-tests.py

Read/write unit tests are isolated from production models and logs

APIs for training and prediction: /app.py

Data ingestion automation pipeline: /data_ingestion_lib.py

Multiple models comparison: solution_notebooks/

EDA investigation with visualizations: solution_notebooks/Capstone_Part2_v1.ipynb

Containerization within a working Docker image: /Dockerfile

Visualization to compare the model to the baseline model: solution_notebooks/Capstone_Part3_v1.ipynb