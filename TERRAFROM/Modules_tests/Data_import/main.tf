terraform {
  required_providers {
    aci = {
      source = "ciscodevnet/aci"
      version = "0.7.0"
    }
  }
  required_version = ">= 0.13"
}


provider "aci" {
  username = "paco"
  password = "!v3G@!4@Y"
  url      = "https://10.129.123.4/"
  insecure = true
}


data "aci_tenant" "tenant_import" {
  name = "demon_tn"
}

data "aci_vrf" "vrf_import" {
  tenant_dn   = "${data.aci_tenant.tenant_import.id}"
  name        = "vrf-total"
}

# data "aci_bridge_domain" "my_shared_bd" {
#   tenant_dn   = "${data.aci_tenant. my_shared_tenant.id}"
#   name        = "my_shared_bd"
# }


resource "aci_application_profile" "terraform_app" {
  tenant_dn = "${data.aci_tenant.tenant_import.id}"
  name       = "demo_app_profile"
}








