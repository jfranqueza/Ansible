
#### TENANT

# tenant_name = "pu"


#### VRF

# vrf_id      = ["vrf_parcial1", "vrf_parcial2"]




# vrf_id      = {
#   VRFS = ["vrf_parcial1", "vrf_parcial2"]
# }

##### BD

bd = {
  BD3 = {
    unicast_route      = "no",
    vrf                = "vrf_parcial1",
    arp_flood          = "yes",
    bridge_domain_type = "regular",
    unk_mcast_act      = "flood",
    unk_mac_ucast_act  = "flood"
  },
  BD4 = {
    unicast_route      = "no",
    vrf                = "vrf_parcial2",
    arp_flood          = "yes",
    bridge_domain_type = "regular",
    unk_mcast_act      = "flood",
    unk_mac_ucast_act  = "flood"
  }
}

### APPLICATION PROFILES

application_profiles = ["FERRO"]


#### EPGS

epgs = {
  EPG3 = {
    name                = "EPG3"
    application_profile = "FERRO"
    bridge_domain       = "BD3"
    domains             = ["uni/phys-Mick_Jackson_Static_PhysDom"]
    static_paths        = []
  },

  EPG4 = {
    name                = "EPG4"
    application_profile = "FERRO"
    bridge_domain       = "BD4"
    domains             = ["uni/phys-Mick_Jackson_Static_PhysDom"]
    static_paths = [
      {
        vlan_id = 348
        path    = "topology/pod-1/paths-101/pathep-[eth1/28]"
      },
      {
        vlan_id = 348
        path    = "topology/pod-1/paths-101/pathep-[eth1/29]"
      }
    ]
  }
}
