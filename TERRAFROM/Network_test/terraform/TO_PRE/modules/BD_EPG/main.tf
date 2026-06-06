/// ACI TENANTS - BD - EPG 
/// CONFIGURATION PROCESS

# terraform {
#   required_providers {
#     aci = {
#       source = "CiscoDevNet/aci"
#     }
#   }
# }

# provider "aci" {
#   # Configuration options
# }
terraform {
  required_providers {
    aci = {
      source = "ciscodevnet/aci"
      version = "0.7.0"
    }
  }
  required_version = ">= 0.13"
}

resource "aci_tenant" "tenant" {
  name = var.tenant_name
}


resource "aci_vrf" "vrf" {
  for_each   = var.vrf_id

  name       = each.key
  tenant_dn  = aci_tenant.tenant.id
  depends_on = [aci_tenant.tenant]
}


resource "aci_bridge_domain" "bridge_domain" {
  for_each           = local.bridge_domains

  name               = each.key
  tenant_dn          = aci_tenant.tenant.id
  unicast_route      = each.value.unicast_route
  arp_flood          = each.value.arp_flood
  bridge_domain_type = each.value.bridge_domain_type
  unk_mcast_act      = each.value.unk_mcast_act
  unk_mac_ucast_act  = each.value.unk_mac_ucast_act
  relation_fv_rs_ctx = aci_vrf.vrf[each.value.vrf].id
}



resource "aci_application_profile" "app_prof" {
  for_each = local.application_profiles

  name       = each.key
  tenant_dn  = aci_tenant.tenant.id
  depends_on = [aci_tenant.tenant]
}



resource "aci_application_epg" "epgs" {
  for_each = local.epgs

  name                   = each.value.name
  application_profile_dn = aci_application_profile.app_prof[each.value.application_profile].id
  relation_fv_rs_bd      = aci_bridge_domain.bridge_domain[each.value.bridge_domain].id
  depends_on             = [aci_bridge_domain.bridge_domain, aci_application_profile.app_prof]
} 

resource "aci_epg_to_domain" "domain" {
  for_each = local.domains

  application_epg_dn = aci_application_epg.epgs[each.value.epg].id
  tdn                = each.value.domain
  depends_on         = [aci_application_epg.epgs]
}


resource "aci_epg_to_static_path" "static_path" {
  for_each = local.static_paths

  application_epg_dn = aci_application_epg.epgs[each.value.epg].id
  tdn                = each.value.path
  encap              = each.value.encap
  mode               = "regular"
  depends_on         = [aci_application_epg.epgs, aci_epg_to_domain.domain]
}


