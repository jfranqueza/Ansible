from acitoolkit.acitoolkit import *
from credentials import *
import json

session = Session(URL, LOGIN, PASSWORD)
session.login()

tenant_name = "piudeferro_Tenant"
vrf_name = "piudeferro_VRF"
tenant = Tenant(tenant_name)
vrf = Context(vrf_name, tenant)

bridge_domain = BridgeDomain("Example_BD", tenant)
bridge_domain.add_context(vrf)
subnet = Subnet('Example_sub', bridge_domain)
subnet.set_scope("public")
subnet.set_addr('192.168.10.1/24')

filter_http = Filter("http", tenant)
filter_entry_tcp80 = FilterEntry ("tcp-80", filter_http, etherT = "ip", prot = "tcp", dFromPort="80", dToPort="80")
filter_sql = Filter("sql", tenant)
filter_entry_tcp1433 = FilterEntry("tcp-1433", filter_sql, etherT = "ip", prot = "tcp", dFromPort="1433", dToPort="1433")

contract_web = Contract("web", tenant)
contract_subject_http = ContractSubject("http", contract_web)
contract_subject_http.add_filter(filter_http)
contract_db = Contract("db", tenant)
contract_subject_db = ContractSubject("sql", contract_db)
contract_subject_db.add_filter(filter_sql)


app_profile = AppProfile("Example_AP", tenant)
epg_web = EPG("Web_EPG", app_profile)
epg_web.add_bd(bridge_domain)
epg_web.provide(contract_web)
epg_web.consume(contract_db)
epg_db = EPG("DB_EPG", app_profile)
epg_db.add_bd(bridge_domain)
epg_db.provide(contract_db)

print(json.dumps(tenant.get_json(), sort_keys=True, indent=2, separators=(',',':')))

resp = session.push_to_apic(tenant.get_url(), data=tenant.get_json())
if resp.ok:
    print("\n{}: {}\n\n{} is ready for use".format(resp.status_code, resp.reason, tenant.name))
else:
    print("\n{}: {}\n\n{} was not created!\n\n Error: {}".format(resp.status_code, resp.reason, subnet.name, resp.content))
    
    
new_tenant_list = Tenant.get(session)
for tn in new_tenant_list:
    print(tn.name)
app_list = AppProfile.get(session, tenant)
for app in app_list:
    print(app.name)
epg_list = EPG.get(session, app_profile, tenant)
for epg in epg_list:
    print(epg.name)

