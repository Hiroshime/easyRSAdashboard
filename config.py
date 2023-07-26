SECRET_KEY = ''

SQLALCHEMY_DATABASE_URI = \
    '{SGBD}://{usuario}:{senha}@{servidor}/{database}'.format(
        SGBD = 'mariadb+mariadbconnector',
        usuario = '',
        senha = '',
        servidor = '172.20.1.2',
        database = 'dashboard'
    )
