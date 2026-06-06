user = {
  username = "paco"
  password = "!v3G@!4@Y"
  url      = "https://10.129.123.4/"
}

tenant   = "TEST_BDS_DC"
vrf = ["TEST_BDS_DC_VRF1", "TEST_BDS_DC_VRF2", "TEST_BDS_DC_VRF3"]
ap = "Testenv_PROD"
 
network_centric = [
    {
        bd  = "DC_PRO_v30_10_130_220_0_24_BD"
        epg = "DC_PRO_v30_10_130_220_0_24_EPG"
    },
    {
        bd  = "DC_PRO_v24_10_130_214_0_24_BD"
        epg = "DC_PRO_v24_10_130_220_0_24_EPG"
    }    
]


