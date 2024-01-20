from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    DB_HOST: str
    DB_PORT: int
    DB_USER: str
    DB_PASS: str
    DB_NAME: str

    # @root_validator(skip_on_failure=True)
    # def get_database_url(cls, values):
    #     values['DATABASE_URL'] = (
    #         f"postgresql+asyncpg://{values['DB_USER']}:{values['DB_PASS']}@"
    #         f"{values['DB_HOST']}:{values['DB_PORT']}/{values['DB_NAME']}"
    #     )
    #     return values

    @property
    def DATABASE_URL(self):
        return (
            f'postgresql+asyncpg://{self.DB_USER}:{self.DB_PASS}@'
            f'{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}'
        )

    SECRET_KEY: str
    ALGORITHM: str

    class Config:
        env_file = '.env'


settings = Settings()
