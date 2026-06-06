variable "tenant_name" {
  type = string
  default = "pu"
}

# variable "vrf_id" {
#    type = list(string)
#    default = []
#    ]
# }





variable "bd" {
  type = map(object({
    unicast_route      = string,
    vrf                = string,
    arp_flood          = string,
    bridge_domain_type = string,
    unk_mcast_act      = string,
    unk_mac_ucast_act  = string,
  }))
  default = {}
}



variable "application_profiles" {
  default = []
}

variable "epgs" {
  type = map(object({

    name                = string,
    application_profile = string,
    bridge_domain       = string,
    domains             = list(string),
    static_paths        = list(object({
      path = string,
      vlan_id = number,
    }))
  }))
  default = {}
}