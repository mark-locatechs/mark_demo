from shared import db


class Route(db.Model):
    __table_args__ = {'mysql_collate': 'utf8_general_ci'}
    id = db.Column(db.Integer, primary_key=True)

    events = db.relationship('Event',
        backref=db.backref('route', lazy=True))

    def __repr__(self):
        return '<Route %r>' % self.id


class Event(db.Model):
    __table_args__ = {'mysql_collate': 'utf8_general_ci'}
    id = db.Column(db.Integer, primary_key=True)
    time = db.Column(db.Date, unique=False, nullable=False)

    route_id = db.Column(db.Integer, db.ForeignKey('route.id'), nullable=False)
    start_id = db.Column(db.Integer, db.ForeignKey('city.id'), nullable=False)
    end_id = db.Column(db.Integer, db.ForeignKey('city.id'), nullable=False)


    def __repr__(self):
        return '<Event %r>' % self.id


class City(db.Model):
    __table_args__ = {'mysql_collate': 'utf8_general_ci'}
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80, collation='utf8_unicode_ci'), unique=False, nullable=False)

    def __repr__(self):
        return '<City %r>' % self.name


def database_init():

    db.drop_all()
    db.create_all()

    city1 = City(name='Amsterdam')
    city2 = City(name='Berlin')
    city3 = City(name='Paris')
    city4 = City(name='Tokyo')
    db.session.add(city1)
    db.session.add(city2)
    db.session.add(city3)
    db.session.add(city4)
    db.session.commit()

