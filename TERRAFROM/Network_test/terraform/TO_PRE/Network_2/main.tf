terraform {
  required_providers {
    aci = {
      source  = "ciscodevnet/aci"
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


module "aci_tenant" {
  source               = "/home/dpko.un.org/franquezaj-su/TERRAFORM/TO_PRE/modules/Tenant_BD_EPG"
  tenant_name          = var.tenant_name
  vrf_id               = var.vrf_id
  bridge_domains       = var.bd
  application_profiles = var.application_profiles
  epgs                 = var.epgs
}  