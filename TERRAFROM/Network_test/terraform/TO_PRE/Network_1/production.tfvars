
#### TENANT

tenant_name = "demon_tn"


#### VRF

vrf_id      = ["vrf-total"]


##### BD

bd = {
  BD1 = {
    unicast_route      = "no",
    vrf                = "vrf-total",
    arp_flood          = "yes",
    bridge_domain_type = "regular",
    unk_mcast_act      = "flood",
    unk_mac_ucast_act  = "flood"
  },
  BD2 = {
    unicast_route      = "no",
    vrf                = "vrf-total",
    arp_flood          = "yes",
    bridge_domain_type = "regular",
    unk_mcast_act      = "flood",
    unk_mac_ucast_act  = "flood"
  }
}

### APPLICATION PROFILES

application_profiles = ["PIW"]


#### EPGS

epgs = {
  EPG1 = {
    name                = "EPG1"
    application_profile = "PIW"
    bridge_domain       = "BD1"
    domains             = ["uni/phys-Mick_Jackson_Static_PhysDom"]
    static_paths        = []
  },

  TWO-EPG2 = {
    name                = "EPG2"
    application_profile = "PIW"
    bridge_domain       = "BD2"
    domains             = ["uni/phys-Mick_Jackson_Static_PhysDom"]
    static_paths = [
      {
        vlan_id = 349
        path    = "topology/pod-1/paths-101/pathep-[eth1/28]"
      },
      {
        vlan_id = 349
        path    = "topology/pod-1/paths-101/pathep-[eth1/29]"
      }
    ]
  }
}
