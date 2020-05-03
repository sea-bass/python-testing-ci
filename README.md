# Testing and Continuous Integration with Python
Sebastian Castro, 2020

Refer to the following blog posts for more information
* COMING SOON

## Setup
### Local Setup
To get started locally, first clone this repository and go to its root folder.

Create a Python 3 virtual environment using the requirements file included. Take the steps below, replacing `$FOLDER_NAME` with whatever destination you would like.

```
python3 -m -m venv SFOLDER_NAME
source $FOLDER_NAME/bin/activate
pip install -r python_requirements.txt
```

Then, with the virtual environment activated, additionally install the packages included with this repository.

```
pip install .
```

NOTE: This repository uses Python 3.6.

### Docker Setup
This repository contains a Dockerfile, from which you can build a Docker container. To do this, first install Docker, then go to the root folder of the repository and build the container.

```
docker build -t testing-ci .
```

where `testing-ci` is the name of the container, and you can use whatever you prefer instead.

Once you have set this up, you can start an interactive session to the container as follows (assuming you used the same name).

```
docker run -it testing-ci
```

Once you're there, you can run all the tests in this repository as shown in the following section.

## Instructions
### Running Tests
We are using the PyTest module to run our tests. All you need to do is go to the root of this repository and run the following line.

```
pytest
```

PyTest will automatically pick up functions and/or class methods in files that start with `test_`, as well as pick up the command-line options we have specified in the `pytest.ini` file.

One of these options is to generate an HTML test report, which is saved as the `latest_test_results.html` file.

If you are using the Docker workflow, you can copy the generated file to the host using:

```
docker cp <containerId>:/app/latest_test_results.html ./latest_test_results.html
```

where `<containerId>` is the ID of the container you can get by running `docker ps` and copying the ID that shows up.

### Setting up Continuous Integration with Jenkins
A Jenkinsfile is included with this repository. This is set up to run `pytest` and then get the collected JUnit style XML for display on Jenkins.

Most of the setup for this part is done in Jenkins itself, so refer to the blog post (COMING SOON) for more information.