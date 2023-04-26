import os
import secrets

class Config:
    SECRET_KEY = secrets.token_hex(16)
    SQLALCHEMY_DATABASE_URI = "sqlite:///site.db"
    GOOGLE_OAUTH_CLIENT_ID = ""
    GOOGLE_OAUTH_CLIENT_SECRET = ""
    OPENWEATHER_API_KEY = "2349390fe3abd134ee5114e9d964061f"
    YELP_API_KEY = "I3FMxowJBZq0DQkS6V0dgXJicBFVJwONQrzRrOcmXUaHs2TDPbyq3swM5FHNOVuby83Nan0X5u2loqg-MoCmntdZjzHQJYSDap0FeHi0WxN6F3JrHLP-Z-e8ZWVAZHYx"
