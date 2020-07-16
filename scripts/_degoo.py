#coding: utf-8

from degoo import degoo_login
import os
username=os.environ["USERNAME"]
password=os.environ["PASSWORD"]
mess_age = degoo_login.Degoo(username, password)
mess_age.login_degoo()
print("Successful logined to Degoo")