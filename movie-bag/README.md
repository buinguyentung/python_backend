### PYTHON API SAMPLE USING CONTROLLER - SERVICE - REPOSITORY
A REST API sample using Flask and PyMySQL that I improve from the movie-bag example.
The code is structured into separate layers: REST Controller Layer, Service layer, and Repository Layer.

### HOW TO RUN THIS PROJECT
0. Following the guide in /database/README to setup MySQL database
1. Install venv		
  $ pip install virtualenv
2. Init a virtual environment (venv)
  $ python<version> -m venv <virtual-environment-name>	
  Ex. python -m venv venv
3. Activate the venv
  (Windows) $ .\venv\Scripts\activate
  (Linux) $	source venv/bin/activate
4. Install libraries in a venv
  $ pip install -r requirements.txt
5. Run flask
  $ flask run
