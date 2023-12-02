
testdata = [
    {
        'test': 'test 0 - me',
        'endpoint_url': '/v2/auth/me',
        'method': 'GET',
        'auth': False,
        'request': {
            'headers': {
                'accept': 'application/json',
                'Content-Type': 'application/x-www-form-urlencoded',
            },
        },
        'response_status_code': 401,
        'response_json': {
            'detail': 'Not authenticated'
        },
        'save_token': False,
    },
    {
        'test': 'test 1 - register',
        'endpoint_url': '/v2/auth/register',
        'method': 'POST',
        'auth': False,
        'request': {
            'params': {
                'name': 'Lena',
                'email': 'Lena%40mail.ru',
                'full_name': 'Lena%20E',
                'disabled': 'false',
                'password': '123',
            },
            'headers': {
                'accept': 'application/json',
            },
        },
        'response_status_code': 201,
        'response_json': {
        },
        'save_token': False,
    },
    {
        'test': 'test 2 - register',
        'endpoint_url': '/v2/auth/register',
        'method': 'POST',
        'auth': False,
        'request': {
            'params': {
                'name': 'Egor',
                'email': 'Egor%40mail.ru',
                'full_name': 'Egor%20Put',
                'disabled': 'false',
                'password': '456',
            },
            'headers': {
                'accept': 'application/json',
            },
        },
        'response_status_code': 201,
        'response_json': {
        },
        'save_token': False,
    },
    {
        'test': 'test 3 - token',
        'endpoint_url': '/v2/auth/token',
        'method': 'POST',
        'auth': False,
        'request': {
            'data': {
                'grant_type': '',
                'username': 'Lena',
                'password': '123',
                'scope': '',
                'client_id': '',
                'client_secret': ''
            },
            'headers': {
                'accept': 'application/json',
                'Content-Type': 'application/x-www-form-urlencoded',
            },
        },
        'response_status_code': 200,
        'response_json': {
        },
        'save_token': True,
    },
    {
        'test': 'test 4 - post-note',
        'endpoint_url': '/v2/notes/post-note',
        'method': 'POST',
        'auth': True,
        'request': {
            'json': {
                "text": "Test note # 1"
            },
            'headers': {
                'accept': 'application/json',
                'Content-Type': 'application/json',
            },
        },
        'response_status_code': 200,
        'response_json': {
        },
        'save_token': False,
    },
    {
        'test': 'test 5 - get notes',
        'endpoint_url': '/v2/notes/get-all',
        'method': 'GET',
        'auth': False,
        'request': {
            'headers': {
                'accept': 'application/json',
            },
        },
        'response_status_code': 401,
        'response_json': {
            "detail": "Not authenticated",
        },
        'save_token': False,
    },
    {
        'test': 'test 6 - token',
        'endpoint_url': '/v2/auth/token',
        'method': 'POST',
        'auth': False,
        'request': {
            'data': {
                'grant_type': '',
                'username': 'Egor',
                'password': '456',
                'scope': '',
                'client_id': '',
                'client_secret': ''
            },
            'headers': {
                'accept': 'application/json',
                'Content-Type': 'application/x-www-form-urlencoded',
            },
        },
        'response_status_code': 200,
        'response_json': {
        },
        'save_token': True,
    },
    {
        'test': 'test 7 - post-note',
        'endpoint_url': '/v2/notes/post-note',
        'method': 'POST',
        'auth': True,
        'request': {
            'json': {
                'create_at': '2023-11-30T11:07:12.102928',
                "text": "Test note # 2"
            },
            'headers': {
                'accept': 'application/json',
                'Content-Type': 'application/json',
            },
        },
        'response_status_code': 200,
        'response_json': {
        },
        'save_token': False,
    },
    {
        'test': 'test 8 - post-note',
        'endpoint_url': '/v2/notes/post-note',
        'method': 'POST',
        'auth': True,
        'request': {
            'json': {
                'create_at': '2023-11-30T11:07:13.102928',
                "text": "Test note # 3"
            },
            'headers': {
                'accept': 'application/json',
                'Content-Type': 'application/json',
            },
        },
        'response_status_code': 200,
        'response_json': {
        },
        'save_token': False,
    },
    {
        'test': 'test 9 - get notes',
        'endpoint_url': '/v2/notes/get-all',
        'method': 'GET',
        'auth': True,
        'request': {
            'headers': {
                'accept': 'application/json',
            },
        },
        'response_status_code': 200,
        'response_json': [
            {
                'create_at': '2023-11-30T11:07:12.102928',
                'text': 'Test note # 2'
            },
            {
                'create_at': '2023-11-30T11:07:13.102928',
                'text': 'Test note # 3'
            }
        ],
        'save_token': False,
    },
    {
        'test': 'test 10 - me',
        'endpoint_url': '/v2/auth/me',
        'method': 'GET',
        'auth': True,
        'request': {
            'headers': {
                'accept': 'application/json',
                'Content-Type': 'application/x-www-form-urlencoded',
            },
        },
        'response_status_code': 200,
        'response_json': {
        },
        'save_token': False,
    },
]
