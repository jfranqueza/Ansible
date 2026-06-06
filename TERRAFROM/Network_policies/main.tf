
terraform {
  required_providers {
    aci = {
      source = "ciscodevnet/aci"
      version = "0.7.0"
    }
  }
  required_version = ">= 0.13"
}

# Configure the provider with your Cisco APIC credentials.
provider "aci" {
  username = "${var.user.username}"
  password = "${var.user.password}"
  url      = "${var.user.url}"
  insecure = true
}

# Define an ACI Tenant Resource.
resource "aci_tenant" "terraform_tenant" {
    name        = "${var.tenant}"
    description = "This tenant is created by terraform"
}

# Define an ACI Tenant VRF Resource.
resource "aci_vrf" "terraform_vrf" {
    tenant_dn   = "${aci_tenant.terraform_tenant.id}"
    description = "VRF Created Using Terraform"
    name        = var.vrf
}



#Define an ACI Tenant BD Resource.

resource "aci_bridge_domain" "PROD_bridges" {
    tenant_dn          = "${aci_tenant.terraform_tenant.id}"
    relation_fv_rs_ctx = "${aci_vrf.terraform_vrf.id}"
    description        = "BD Created Using Terraform"
    name               = "${var.bd}"
}



resource "aci_application_profile" "terraform_ap" {
  tenant_dn  = aci_tenant.terraform_tenant.id
  name       = "${var.ap}"
  description = ""
}


# # Define an ACI Tenant EPG Resource.
# resource "aci_application_epg" "terraform_epg" {
#     application_profile_dn  = aci_application_profile.app_profile_for_epg.id
#     name                              = "demo_epg"
#     description                   = "from terraform"
#     annotation                    = "tag_epg"
#     exception_tag                 = "0"
#     flood_on_encap            = "disabled"
#     fwd_ctrl                      = "none"
#     has_mcast_source             = "no"
#     is_attr_based_epg         = "no"
#     match_t                          = "AtleastOne"
#     name_alias                  = "alias_epg"
#     pc_enf_pref                  = "unenforced"
#     pref_gr_memb                  = "exclude"
#     prio                              = "unspecified"
#     shutdown                      = "no"
# }




# # Define an ACI Tenant BD Resource.
# resource "aci_bridge_domain" "PROD_bridges" {
#     tenant_dn          = "${aci_tenant.terraform_tenant.id}"
#     relation_fv_rs_ctx = "${aci_vrf.terraform_vrf.id}"
#     description        = "BD Created Using Terraform"
#     name               = "${var.bd}"
# }






# resource "aci_bridge_domain" "terraform_bridges" {
#     for_each = {for network in var.network_centric: network.bd => network}
#     #for_each = var.network_centric
#     tenant_dn          = "${aci_tenant.terraform_tenant.id}"
#     #relation_fv_rs_ctx = "${each.value.vrf}"#"${aci_vrf.terraform_vrf.id}"
#     name               = "${each.value.bd}"
#     arp_flood = "yes"
#     bridge_domain_type = "regular"
#     ip_learning = "yes"
#     limit_ip_learn_to_subnets = "yes"
#     multi_dst_pkt_act = "bd-flood"
#     unicast_route = "no"
#     unk_mac_ucast_act = "flood"
#     unk_mcast_act = "flood"
#     v6unk_mcast_act = "flood"
# }