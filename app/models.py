class Requests(object):
    """Sample user requests"""
    def __init__(self):
        self.db_requests =\
            [
                {
                    'request_id':200,
                    'user_id': 102,
                    'project_id': 101,
                    'request_type': 'Maintenance',
                    'request_description': 'Ugrade to the latest version.',
                    'request_date': '12/23/2017',
                    'Approved/Rejected':'Approved',
                    'status':'Resolved'
                },
                {
                    'request_id':201,
                    'user_id': 102,
                    'project_id': 132,
                    'request_type': 'Repair',
                    'request_description': 'Cant login user accounts',
                    'request_date': '01/20/2018',
                    'Approved/Rejected':'Rejected',
                    'status': 'Not Ressolved'
                },
                {
                    'request_id':203,
                    'user_id': 103,
                    'project_id': 121,
                    'request_type': 'Maintenance',
                    'request_description': "Slowed performance.",
                    'request_date': '02/25/2018',
                    'Approved/Rejected':'Approved',
                    'status': 'Ressolved'
                }
            ]


class Users(object):
    """list to contain users"""
    def __init__(self):
        self.db_users =\
            [
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
