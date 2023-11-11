from dataclasses import dataclass

from envparse import Env

env = Env()


@dataclass(frozen=True, slots=True)
class Settings:
    DB_HOST: str = env.str("DB_HOST")
    DB_PORT: int = env.int("DB_PORT")
    DB_USER: str = env.str("DB_USER")
    DB_PASS: str = env.str("DB_PASS")
    DB_NAME: str = env.str("DB_NAME")

    DATABASE_URL = f"postgresql+asyncpg://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

    def __post_init__(self):
        if not all(map(
                lambda attr: isinstance(attr, str),
                (self.DB_HOST, self.DB_USER, self.DB_PASS, self.DB_NAME)
        )):
            raise TypeError('DB_HOST, DB_USER, DB_PASS, DB_NAME should be of type str')

        if not isinstance(self.DB_PORT, int):
            raise TypeError('DB_PORT should be of type int')


settings = Settings()
