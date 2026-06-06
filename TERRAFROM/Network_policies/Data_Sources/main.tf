terraform {
  required_providers {
    aci = {
      source = "CiscoDevNet/aci"
    }
  }
}

# Configure the provider with your Cisco APIC credentials.
provider "aci" {
  username = "${var.user.username}"
  password = "${var.user.password}"
  url      = "${var.user.url}"
  insecure = true
}

# # Define an ACI Tenant Resource.
resource "aci_tenant" "UNGSC_BDS_DC" {
}

# # Define an ACI Tenant VRF Resource.
resource "aci_vrf" "BDS_DC_VRF" {
}

resource "aci_bridge_domain" "BD-DC_PRO_v51_10_130_230_64_27_BD" {
}


