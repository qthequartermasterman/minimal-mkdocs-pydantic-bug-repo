import pydantic_settings

class MyModel(pydantic.BaseModel):
    id: int
    name: str

class AnotherModel(MyModel):
    asdf: str

class MySettingsModel(pydantic_settings.BaseSettings):
    asdf: str