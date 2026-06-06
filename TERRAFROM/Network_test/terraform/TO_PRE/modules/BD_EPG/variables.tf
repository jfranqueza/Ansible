variable "tenant_name" {
  type = string
  default = ""
}

variable "vrf_id" {
  type    = map
  default = {}
}

# variable "bridge_domains" {
#   type = map(object({
#     routing = bool,
#     vrf     = string,
#   }))
#   description = "Map of bridge domains to create and their associated VRFs"
#   default     = {}
# }


variable "bridge_domains" {
  type = map(object({
    unicast_route      = string,
    tenant_name        = string,
    vrf                = string,
    arp_flood          = string,
    bridge_domain_type = string,
    unk_mcast_act      = string,
    unk_mac_ucast_act  = string,
  }))

  # default     = {
  #   name                = "",
  #   unicast_route       = "no",
  #   vrf                 = "",
  #   arp_flood           = "yes",
  #   bridge_domain_type  = "regular",
  # }
}


locals {
   bds = tomap({
    for bd_key, bd in var.bridge_domains : bd_key => {
      vrf                = bd.vrf
      unicast_route      = bd.unicast_route
      arp_flood          = bd.arp_flood
      bridge_domain_type = bd.bridge_domain_type
      unk_mcast_act      = bd.unk_mcast_act 
      unk_mac_ucast_act  = bd.unk_mac_ucast_act
    }
  })

}




variable "application_profiles" {
  type        = set(string)
  description = "List of application profiles belonging to the Tenant"
  default     = []
}





variable "epgs" {
  type = map(object({
    name                = string,
    application_profile = string,
    bridge_domain       = string,
    domains             = list(string),
    static_paths = list(object({
      path    = string,
      vlan_id = number,
    })),
  }))
  description = "Map of EPGs to create and their associated bridge-domains"
  default     = {}
}



# locals {
#   bds = tomap({
#     for bd_key, bd in var.bridge_domains : bd_key => {
#       vrf              = bd.vrf
#       arp_flood        = bd.routing ? "no" : "yes"
#       l2_unicast_flood = bd.routing ? "proxy" : "flood"
#       route            = bd.routing ? "yes" : "no"
#     }
#   })
# }

locals {
  name                 = var.tenant_name
  vrfs                 = var.vrf_id
  bridge_domains       = local.bds 
  application_profiles = var.application_profiles
  epgs                 = var.epgs
}

locals {
  domain_list = flatten([
    for epg_key, epg in var.epgs : [
      for domain_key, domain in epg.domains : {
        domain = domain
        epg    = epg_key
      }
    ]
  ])
}

locals {
  domains = {
    for domain in local.domain_list : join(".", [domain.epg, domain.domain]) => domain
  }
}


locals {
  static_path_list = flatten([
    for epg_key, epg in var.epgs : [
      for path in epg.static_paths : {
        path  = path.path
        encap = "vlan-${path.vlan_id}"
        epg   = epg_key
      }
    ]
  ])
}


locals {
  static_paths = {
    for path in local.static_path_list : join("/", [path.path, path.encap]) => path
  }
}