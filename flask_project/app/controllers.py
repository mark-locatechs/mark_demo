from flask import abort, jsonify, request, make_response
from app.models import Route, Event, City
from flask_restful import  Api, Resource


from marshmallow import Schema, fields, post_load
from marshmallow_sqlalchemy import ModelSchema

from app.shared import db



class RouteSchema(ModelSchema):
    class Meta:
        model = Route

route_schema = RouteSchema()
routes_schema = RouteSchema(many=True)


class EventSchema(ModelSchema):
    time = fields.Date(
        required=True,
    )
    start_id = fields.Integer(
        required=True,
    )
    end_id = fields.Integer(
        required=True,
    )
    route_id = fields.Integer(
        required=True,
    )
    class Meta:
        model = Event

event_schema = EventSchema()
events_schema = EventSchema(many=True)


class CitySchema(ModelSchema):
    class Meta:
        model = City

cities_schema = CitySchema(many=True)


class RouteController(Resource):

    def get(self, id):

        result = Route.query.get(id)

        if result is None:
            abort(404)

        return route_schema.dump(result)


    def delete(self, id):

        rowcount = Route.query.filter_by(id=id).delete()

        db.session.commit()

        if rowcount == 0:
            abort(404)

        return jsonify(row=rowcount)


class RoutesController(Resource):


    def get(self):
        result = Route.query.all()
        dict_result = { route.get('id'): route for route in routes_schema.dump(result).data}
        return dict_result

    def post(self):
        new_route = Route()
        db.session.add(new_route)
        db.session.commit()

        return jsonify(id=new_route.id)


class EventController(Resource):

    def get(self, id):

        result = Event.query.get(id)

        if result is None:
            abort(404)

        return event_schema.dump(result)


    def delete(self, id):

        rowcount = Event.query.filter_by(id=id).delete()

        db.session.commit()

        if rowcount == 0:
            abort(404)

        return jsonify(row=rowcount)

    def put(self, id):

        data = request.get_json()

        (new_event, error) = event_schema.load(data, session=db.session)


        if error:
            return make_response(jsonify(error=error), 400)

        # remove route_id for security
        data.pop('route_id')

        row_count = Event.query.filter_by(id=id).update(data)

        print(row_count)


        try:
            db.session.commit()

            return jsonify(id=id)

        except Exception as e:
            db.session.rollback()
            abort(400)


class EventsController(Resource):

    def get(self):
        result = Event.query.all()

        dict_result = { event.get('id'): event for event in events_schema.dump(result).data}
        return dict_result

    def post(self):

        (new_event, error) = event_schema.load(request.get_json(), session=db.session)

        if error:
            return make_response(jsonify(error=error), 400)

        db.session.add(new_event)

        try:
            db.session.commit()
            return jsonify(id=new_event.id)
        except Exception as e:
            db.session.rollback()
            abort(400)



class CitiesController(Resource):

    def get(self):
        result = City.query.all()
        dict_result = { city.get('id'): city for city in cities_schema.dump(result).data}
        return dict_result
