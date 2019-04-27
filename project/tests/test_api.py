#!/usr/bin/env python

import requests
import json
from app.app import app
from app.models import database_init


# reset DB
with app.app_context():
    database_init()

# test static pages
def test_index():
    resp = requests.get('http://localhost:5000/')
    assert resp.status_code == 200
    assert resp.text.find('demo.js') > -1

def test_lorem():
    resp = requests.get('http://localhost:5000/lorem')
    assert resp.status_code == 200
    assert resp.text.find('Lorem ipsum') > -1

# test route API
def test_route_create():
    resp = requests.post('http://localhost:5000/route')
    data = json.loads(resp.text)

    assert resp.status_code == 200
    assert data.get('id') == 1

def test_route_get():
    resp = requests.get('http://localhost:5000/route/1')
    data = json.loads(resp.text)
    assert resp.status_code == 200
    assert data.get('id') == 1
    assert data.get('event') is None


def test_event_create():
    resp = requests.post('http://localhost:5000/event', json={
        'start_id': 1,
        'end_id': 1,
        'time': '1990-01-01',
        'route_id': 1
    })
    data = json.loads(resp.text)

    assert resp.status_code == 200
    assert data.get('id') == 1


def test_event_get():
    resp = requests.get('http://localhost:5000/event/1')
    data = json.loads(resp.text)
    assert resp.status_code == 200
    assert data.get('id') == 1
    assert data.get('start_id') == 1
    assert data.get('end_id') == 1
    assert data.get('time') == '1990-01-01'
    assert data.get('route_id') == 1

def test_event_put():
    resp = requests.put('http://localhost:5000/event/1', json={
        'start_id': 2,
        'end_id': 2,
        'time': '2990-01-01',
        'route_id': 0,
    })
    data = json.loads(resp.text)

    assert resp.status_code == 200
    assert data.get('id') == 1

    resp = requests.get('http://localhost:5000/event/1')
    data = json.loads(resp.text)
    assert resp.status_code == 200
    assert data.get('id') == 1
    assert data.get('start_id') == 2
    assert data.get('end_id') == 2
    assert data.get('time') == '2990-01-01'
    assert data.get('route_id') == 1


def test_route_list_get():
    resp = requests.get('http://localhost:5000/route')
    data = json.loads(resp.text)

    expected_data = json.loads('{"1":{"events":[1],"id":1}}')
    assert resp.status_code == 200
    assert data == expected_data

    resp = requests.post('http://localhost:5000/route')
    assert resp.status_code == 200

    resp = requests.get('http://localhost:5000/route')
    data = json.loads(resp.text)

    expected_data = json.loads('{"1":{"events":[1],"id":1},"2":{"events":[],"id":2}}')
    assert resp.status_code == 200
    assert data == expected_data


def test_event_list_get():
    resp = requests.get('http://localhost:5000/event')
    data = json.loads(resp.text)

    expected_data = json.loads('{"1":{"end_id":2,"id":1,"route_id":1,"time":"2990-01-01","start_id":2,"route":1}}')
    assert resp.status_code == 200
    assert data == expected_data


    resp = requests.post('http://localhost:5000/event', json={
        'start_id': 3,
        'end_id': 3,
        'time': '1999-01-01',
        'route_id': 2
    })
    data = json.loads(resp.text)

    assert resp.status_code == 200
    assert data.get('id') == 2

    resp = requests.get('http://localhost:5000/event')
    data = json.loads(resp.text)

    expected_data = json.loads('{"1":{"end_id":2,"id":1,"route_id":1,"time":"2990-01-01","start_id":2,"route":1},"2":{"end_id":3,"id":2,"route_id":2,"time":"1999-01-01","start_id":3,"route":2}}')
    assert resp.status_code == 200
    assert data == expected_data


def test_route_delete():
    resp = requests.delete('http://localhost:5000/route/1')
    data = json.loads(resp.text)
    assert resp.status_code == 200
    assert data.get('row') == 1



def test_event_delete():
    resp = requests.delete('http://localhost:5000/event/2')
    data = json.loads(resp.text)
    assert resp.status_code == 200
    assert data.get('row') == 1



# test city API

def test_city_list_get():
    resp = requests.get('http://localhost:5000/city')
    data = json.loads(resp.text)

    assert resp.status_code == 200
    assert len(data) > 3

# reset DB
with app.app_context():
    database_init()
    print('reset db')
