# Maintenance Tracker App

This is a web based application that allows Admin and clients to interact. 
Clients post their maintenance or repair requests while Admin approves or rejects them.

# installation procedure.
  1. Ensure you have **python 3.6.2**,**pip**, and **virtualenv** are installed on your local machine.
  2. Ensure you have Postman since it might bee needed to test the API.
  3. Clone the project to your local machine.
  4. Navigate to the project folder.
  5. Create a virtual environment using `virtualenv venv` on your command line. 

    ```
    export SECRET="random_key"
    export APP_SETTINGS="development"
    ```
  7. Activate your virtual environment i.e. `source venv/bin/activate`.
  8. install the requirements in the environment i.e. `pip install -r requirements.txt`

# Running the app
  1. `python run.py`

# Working endpoints

  | URL                                              | Methods | Description                       |
  |--------------------------------------------------|---------|-----------------------------------|
  | /api/v1/register/                                | POST    | Registering a new user            |
  | /api/v1/login/                                   | GET     | User login                        |
  | /api/v1/requests/                                | POST    | Create a new request              |
  | /api/v1/requests/                                | GET     | Get all user requests             |
  | /api/v1/requests/<user_id>                       | GET     | Get all requests for a given user |
  | /api/v1/requests/<request_id>                    | GET     | Get a request                     |
  | /api/v1/requests/<request_id>                    | PUT     | Edit a request                    |
