class DatabaseConfig:
    def __init__(self, user, password, host, port, database):
        self.user = user
        self.password = password
        self.host = host
        self.port = port
        self.database = database

    def get_url_postgresql(self):
        db_url = f'postgresql://{self.user}:{self.password}@{self.host}:{self.port}/{self.database}'
        return db_url