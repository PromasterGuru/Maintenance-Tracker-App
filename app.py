from flask import Flask, jsonify, request
import types
import pdb

app = Flask(__name__)


users = [
    {
        'user_id': 101,
        'username': 'promaster',
        'email': 'promaster@daisy.com',
        'userpassword': 'promaster'
    },
    {
        'user_id': 102,
        'username': 'github',
        'email': 'github@gmail.com',
        'password': 'githubguru'
    }
]

requests = [
    {
        'user': 102,
        'projectid': 101,
        'request_type': 'Maintenance',
        'request_description': 'Ugrade to the latest version.',
        'request_date': '12/23/2017',
        'Approved/Rejected':'Approved',
        'status':'Resolved'
    },
    {
        'user': 102,
        'projectid': 132,
        'request_type': 'Repair',
        'request_description': 'Cant login client accounts',
        'request_date': '01/20/2018',
        'Approved/Rejected':'Rejected',
        'status': 'Not Ressolved'
    },
    {
        'user': 103,
        'projectid': 121,
        'request_type': 'Maintenance',
        'request_description': "Slowed performance.",
        'request_date': '02/25/2018',
        'Approved/Rejected':'Approved',
        'status': 'Ressolved'
    }
]


@app.route('/')
def index():
    return "We will get back to you soon"


@app.route('/api/v1/signup', methods=['POST'])
def signup():
    pass


@app.route('/api/v1/login', methods=['POST'])
def login():
    pass


@app.route('/api/v1/users/requests/<string:user_id>', methods=['GET'])
def getAllRequests(user_id):
    if not user_id or user_id==None:
        user_id=0
    try:
        if user_id is None or isinstance(int(user_id),int)==False:
            response = jsonify({"requests": "You have entered an invalid user id"})
            response.status_code = 200
            return response
        else:
            user_id = int(user_id)
    except:
        response = jsonify({"requests": "You have entered an invalid user id"})
        response.status_code = 405 #Method not allowed
        return response

    userRequests = [request for request in requests if request["requestorid"] == user_id]

    if not userRequests:
        response = jsonify({"requests": "No requests for this user"})
        response.status_code = 200
        return response
    else:
        response = jsonify({"requests": userRequests})
        response.status_code = 200
        return response

@app.route('/api/v1/users/request/<string:request_id>', methods=['GET'])
def getSingleRequest(request_id):
    if not request_id or request_id==None:
        request_id=0
    try:
        if request_id is None or isinstance(int(request_id),int)==False:
            response = jsonify({"requests": "Invalid request id"})
            response.status_code = 404
            return response
        else:
            request_id = int(request_id)
    except:
        response = jsonify({"requests": "Invalid request id"})
        response.status_code = 405
        return response

    userRequests = [request for request in requests if request["request_id"] == request_id]

    if not userRequests:
        response = jsonify({"requests": "No requests found"})
        response.status_code = 200
        return response
    else:
        response = jsonify({"requests": userRequests})
        response.status_code = 200
        return response


if __name__ == '__main__':
    app.run(debug=True)
