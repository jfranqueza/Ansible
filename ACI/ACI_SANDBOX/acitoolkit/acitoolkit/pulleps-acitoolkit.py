import acitoolkit.acitoolkit as aci
from credentials import *
import sys

session = aci.Session(URL, LOGIN, PASSWORD)
resp = session.login()

if not resp.ok:
    print(f"ERROR: Could not login into APIC {URL}")
    print.sys(0)
else:
    print(f"SUCCESS: Logged into APIC {URL}")    

          
endpoints = aci.Endpoint.get(session)
