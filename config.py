import os
from functools import lru_cache
from pydantic import BaseSettings


APP_ENV = os.environ.get("APP_ENV", "development")
base_dir = os.path.dirname(os.path.abspath(__file__))


class BaseConfig(BaseSettings):
    # Why do we need it?
    ENV: str = "base"
    # Is it correct to assign key in this line?
    SECRET_KEY = os.environ.get("SECRET_KEY")
    WTF_CSRF_ENABLED: bool = False
    LOCAL_DB_PORT = os.environ.get("LOCAL_DB_PORT", 5433)


class DevelopmentConfig(BaseConfig):
    DEBUG: bool = True

    SQLALCHEMY_DATABASE_URI = "postgresql://postgres:postgres@127.0.0.1:5433/postgres"
    # SQLALCHEMY_DATABASE_URI = os.environ.get(
    #     "DATABASE_URL", "sqlite:///" + os.path.join(base_dir, "database.sqlite3")
    # )


class TestingConfig(BaseConfig):
    TESTING: bool = True

    SQLALCHEMY_DATABASE_URI: str = "sqlite:///" + os.path.join(
        base_dir, "database-test.sqlite3"
    )


@lru_cache
def config(name=APP_ENV) -> DevelopmentConfig | TestingConfig:
    CONF_MAP = dict(development=DevelopmentConfig(), testing=TestingConfig())
    configuration = CONF_MAP[name]
    configuration.ENV = name

    return configuration


# app.config["WTF_CSRF_ENABLED"] = False
# app.config[
#     "SQLALCHEMY_DATABASE_URI"
# ] = f"postgresql://postgres:postgres@127.0.0.1:{LOCAL_DB_PORT}/postgres"
#     app.config["SECRET_KEY"] = os.environ.get("SECRET_KEY")
