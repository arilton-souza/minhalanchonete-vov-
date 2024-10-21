import os
from pathlib import Path
from dotenv import load_dotenv

# Carregar variáveis de ambiente de um arquivo .env
load_dotenv()

BASE_DIR = Path(__file__).resolve().parent.parent

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.getenv('DB_NAME', 'nome_do_banco'),  # Nome do banco de dados
        'USER': os.getenv('DB_USER', 'usuario'),
        'PASSWORD': os.getenv('DB_PASSWORD', 'senha'),
        'HOST': os.getenv('DB_HOST', 'localhost'),  # Endereço do host
        'PORT': os.getenv('DB_PORT', '5432'),  # Porta do banco de dados
    }
}
import os
from pathlib import Path
from dotenv import load_dotenv

# Carregar variáveis de ambiente de um arquivo .env
load_dotenv()

BASE_DIR = Path(__file__).resolve().parent.parent

if os.getenv('DJANGO_ENV') == 'production':
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql',
            'NAME': os.getenv('DB_NAME', 'nome_do_banco'),
            'USER': os.getenv('DB_USER', 'usuario'),
            'PASSWORD': os.getenv('DB_PASSWORD', 'senha'),
            'HOST': os.getenv('DB_HOST', 'localhost'),
            'PORT': os.getenv('DB_PORT', '5432'),
        }
    }
else:
    # Configuração para ambiente de desenvolvimento (SQLite)
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': BASE_DIR / 'db.sqlite3',
        }
    }
