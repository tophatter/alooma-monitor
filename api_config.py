import os
import alooma

ALOOMA_USERNAME = os.environ.get('ALOOMA_USERNAME')
ALOOMA_PASSWORD = os.environ.get('ALOOMA_PASSWORD')
ALOOMA_ACCOUNT_NAME = os.environ.get('ALOOMA_ACCOUNT_NAME')

api = alooma.Client(
    username=ALOOMA_USERNAME,
    password=ALOOMA_PASSWORD,
    account_name=ALOOMA_ACCOUNT_NAME
)