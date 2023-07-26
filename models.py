from dashboard import db

class User(db.Model):

    def __repr__(self):
        return '<Name %r>' % self.name

class EasyRSA(db.Model):
    id = db.Column(db.Integer , primary_key=True , autoincrement=True)
    name = db.Column()
    address = db.Column()
    user = db.Column()
    password = db.Column()
    certificate = db.Column()
    def __repr__(self):
        return '<Name %r>' % self.name

class Pki(db.Model):
    id = db.Column(db.Integer , primary_key=True , autoincrement=True)
    name = db.Column()
    path = db.Column()
    password = db.Column()
    def __repr__(self):
        return '<Name %r>' % self.name

class Certificate(db.Model):
    id = db.Column(db.Integer , primary_key=True , autoincrement=True)
    commonName = db.Column()
    path = db.Column()
    create_date = db.Column()
    validDays = db.Column()
    def __repr__(self):
        return '<Name %r>' % self.name

class Concessionaire(db.Model):
    id = db.Column(db.Integer , primary_key=True , autoincrement=True)
    name = db.Column()
    ec_code = db.Column()
    def __repr__(self):
        return '<Name %r>' % self.name

class Regulator(db.Model):
    id = db.Column(db.Integer , primary_key=True , autoincrement=True)
    name = db.Column()
    def __repr__(self):
        return '<Name %r>' % self.name

class Integrator(db.Model):
    id = db.Column(db.Integer , primary_key=True , autoincrement=True)
    name = db.Column()
    def __repr__(self):
        return '<Name %r>' % self.name

class OVPNServer(db.Model):
    id = db.Column(db.Integer , primary_key=True , autoincrement=True)
    name = db.Column()
    address = db.Column()
    port = db.Column()
    def __repr__(self):
        return '<Name %r>' % self.name

class Environment(db.Model):
    id = db.Column(db.Integer , primary_key=True , autoincrement=True)
    name = db.Column()
    def __repr__(self):
        return '<Name %r>' % self.name

class AdministrativeLogs(db.Model):
    id = db.Column(db.Integer , primary_key=True , autoincrement=True)
    date  = db.Column()
    text  = db.Column()
    def __repr__(self):
        return '<Name %r>' % self.name