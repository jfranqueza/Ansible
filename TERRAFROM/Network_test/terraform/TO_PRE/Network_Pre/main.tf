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


data "aci_tenant" "tenant" {
  name  = var.tenant_name
}

# data "aci_vrf" "vrf" {
#   for_each   = toset(var.vrf_id["VRFS"])
#   name       = each.key
#   tenant_dn  = var.tenant_name #data.aci_tenant.tenant.id
# }


module "aci_tenant" {
  source               = "/home/reponeg/nexus/franquezaj/TERRAFROM/Network_test/terraform/TO_PRE/modules/BD_EPG/v1"
  tenant_name          = data.aci_tenant.tenant
  # vrf_id               = data.aci_vrf.vrf
  bridge_domains       = var.bd
  application_profiles = var.application_profiles
  epgs                 = var.epgs
}  

