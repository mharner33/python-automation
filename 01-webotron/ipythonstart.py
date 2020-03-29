# coding: utf-8
# To reload run: pipenv run ipython -i ipythonstart.py
import boto3
session = boto3.Session(profile_name = 'pythonautomation')
s3 = session.resource('s3')

