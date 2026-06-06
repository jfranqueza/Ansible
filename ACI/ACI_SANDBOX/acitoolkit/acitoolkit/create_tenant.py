from acitoolkit.acitoolkit import *
from credentials import *

session = acitoolkit.Session(URL, LOGIN, PASSWORD)
session.login()

tenant_list = Tenant.get(session)

for tenant in tenant_list:
    print(tenant)