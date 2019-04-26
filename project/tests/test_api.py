from flask import request, jsonify
from app.models import app



with app.test_client() as c:
    rv = c.post('/event', json={
        'username': 'flask', 'password': 'secret'
    })
    json_data = rv.get_json()
    assert 1
