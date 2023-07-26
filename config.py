SECRET_KEY = 'klwi@HAJ27As2123eja&'

SQLALCHEMY_DATABASE_URI = \
    '{SGBD}://{usuario}:{senha}@{servidor}/{database}'.format(
        SGBD = 'mariadb+mariadbconnector',
        usuario = 'dash',
        senha = 'L0ngP4ssw0rd',
        servidor = '172.20.1.2',
        database = 'dashboard'
    )