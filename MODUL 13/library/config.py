import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


class Config:
    SECRET_KEY = os.environ.get("SECRET_KEY") or "remember-to-add-secret-key"
    SQLALCHEMY_DATABASE_URI = (
            os.environ.get('DATABASE_URL') or
            'sqlite:///' + os.path.join(BASE_DIR, 'library/db/biblioteka3.db')
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = False
