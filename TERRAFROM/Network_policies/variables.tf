variable "user" {
  default = ""
}

variable "tenant" {
  default = ""
}

variable "vrf" {
  type = set(string)
  default = [""]
}

variable "network_centric" {
  type = set(object({
    bd        = string
    epg       = string
  }))
  default =[
    {
      bd        = ""
      epg       = ""
    }
  ]
} 

variable "bd_arp_flood" {
  description = "Specify whether ARP flooding is enabled"
  default     = "yes"
  validation {
    condition = (var.bd_arp_flood == "yes") || (var.bd_arp_flood == "no")
    error_message = "Allowed values are \"yes\" and \"no\"."
  }
}


variable "ap" {
  default = ""
}


# variable "bd_ap_epg" {
#     type  = map
#     description = "describing the world"
#     default = { []
#       ap_prod   = "DC_PRO_v30_10_130_220_0_24_BD"

  #   },
  #     DC_PRO_v24_10_130_214_0_24_BD = {
  #     name      = "DC_PRO_v24_10_130_214_0_24_BD"
  #   },
  #     C_PRO_v10_10_130_200_0_24_BD = {
  #     name      = "DC_PRO_v10_10_130_200_0_24_BD"
  #   },
  #     DC_PRO_v9_10_130_201_0_24_BD = {
  #     name      = "DC_PRO_v9_10_130_201_0_24_BD"
  #   },
  #     DC_PRO_v7_10_130_197_0_24_BD = {
  #     name      = "DC_PRO_v7_10_130_197_0_24_BD"    
  #   },
  #     DC_PRO_v148_10_129_80_192_27_BD = {
  #     name      = "DC_PRO_v148_10_129_80_192_27_BD"      
  #   },
  #     DC_PRO_v189_10_129_124_0_23_BD = {
  #     name      = "DC_PRO_v189_10_129_124_0_23_BD"      
  #   }
#   ]
#    }
# }


# variable "bd_ap_epg" {
#     type    = map
#     default = {
#       DC_PRO_v30_10_130_220_0_24_BD = {
#       name      = "DC_PRO_v30_10_130_220_0_24_BD"
#     },
#       DC_PRO_v24_10_130_214_0_24_BD = {
#       name      = "DC_PRO_v24_10_130_214_0_24_BD"
#     },
#       C_PRO_v10_10_130_200_0_24_BD = {
#       name      = "DC_PRO_v10_10_130_200_0_24_BD"
#     },
#       DC_PRO_v9_10_130_201_0_24_BD = {
#       name      = "DC_PRO_v9_10_130_201_0_24_BD"
#     },
#       DC_PRO_v7_10_130_197_0_24_BD = {
#       name      = "DC_PRO_v7_10_130_197_0_24_BD"    
#     },
#       DC_PRO_v148_10_129_80_192_27_BD = {
#       name      = "DC_PRO_v148_10_129_80_192_27_BD"      
#     },
#       DC_PRO_v189_10_129_124_0_23_BD = {
#       name      = "DC_PRO_v189_10_129_124_0_23_BD"      
#     },
#       DC_PRO_v3466_10_130_221_200_29_BD = {
#       name      = "DC_PRO_v3466_10_130_221_200_29_BD"      
#     },
#       DC_PRO_v3133_10_129_77_0_24_BD = {
#       name      = "DC_PRO_v3133_10_129_77_0_24_BD"      
#     },
#       DC_PRO_v3131_10_129_75_0_24_BD = {
#       name      = "DC_PRO_v3131_10_129_75_0_24_BD"      
#     },
#       DC_PRO_v6_10_130_196_0_24_BD = {
#       name      = "DC_PRO_v6_10_130_196_0_24_BD"      
#     },
#       DC_PRO_v1422_10_130_142_160_27_BD = {
#       name      = "DC_PRO_v1422_10_130_142_160_27_BD"      
#     },
#       DC_PRO_v166_10_130_143_224_28_BD = {
#       name      = "DC_PRO_v166_10_130_143_224_28_BD"      
#     },
#       DC_PRO_v50_10_130_226_64_27_BD = {
#       name      = "DC_PRO_v50_10_130_226_64_27_BD"      
#     },
#       DC_PRO_v142_10_130_142_0_24_BD = {
#       name      = "DC_PRO_v142_10_130_142_0_24_BD"      
#     },
#       DC_PRO_v20_10_130_210_0_24_BD = {
#       name      = "DC_PRO_v20_10_130_210_0_24_BD"      
#     },
#       DC_PRO_v132_10_130_132_0_24_BD = {
#       name      = "DC_PRO_v132_10_130_132_0_24_BD"      
#     },
#        DC_PRO_v12_10_130_202_0_24_BD = {
#       name      = "DC_PRO_v12_10_130_202_0_24_BD"      
#     },   
#       DC_PRO_v131_10_130_131_0_24_BD = {
#       name      = "DC_PRO_v131_10_130_131_0_24_BD"      
#     },       
#       DC_PRO_v116_10_130_235_128_27_BD = {
#       name      = "DC_PRO_v116_10_130_235_128_27_BD"      
#     },       
#       DC_PRO_v94_10_129_68_32_27_BD = {
#       name      = "DC_PRO_v94_10_129_68_32_27_BD"      
#     },       
#       DC_PRO_v69_10_130_247_0_24_BD = {
#       name      = "DC_PRO_v69_10_130_247_0_24_BD"      
#     },   
#       DC_PRO_v68_10_130_244_0_24_BD = {
#       name      = "DC_PRO_v68_10_130_244_0_24_BD"      
#     },  
#       DC_PRO_v1421_10_130_142_128_27_BD = {
#       name      = "DC_PRO_v1421_10_130_142_128_27_BD"      
#     },
#       DC_PRO_v64_10_130_254_0_24_BD = {
#       name      = "DC_PRO_v64_10_130_254_0_24_BD"      
#     },              
#       DC_PRO_v480_10_130_238_0_24_BD = {
#       name      = "DC_PRO_v480_10_130_238_0_24_BD"      
#     },                   
#       DC_PRO_v63_10_129_73_128_26_BD = {
#       name      = "DC_PRO_v63_10_129_73_128_26_BD"      
#     },
#       DC_PRO_v61_10_129_81_0_24_BD = {
#       name      = "DC_PRO_v61_10_129_81_0_24_BD"      
#     },  
#       DC_PRO_v42_10_130_208_128_26_BD = {
#       name      = "DC_PRO_v42_10_130_208_128_26_BD"      
#     },
#       DC_PRO_v36_10_130_226_0_27_BD = {
#       name      = "DC_PRO_v36_10_130_226_0_27_BD"      
#     },
#       DC_PRO_v460_10_130_236_0_27_BD = {
#       name      = "DC_PRO_v460_10_130_236_0_27_BD"      
#     },
#       DC_PRO_v175_10_130_221_224_27_BD = {
#       name      = "DC_PRO_v175_10_130_221_224_27_BD"      
#     },
#       DC_PRO_v27_10_130_217_0_24_BD = {
#       name      = "DC_PRO_v27_10_130_217_0_24_BD"      
#     },
#       DC_PRO_v440_10_130_234_0_27_BD = {
#       name      = "DC_PRO_v440_10_130_234_0_27_BD"      
#     },                                                                 
#       DC_PRO_v22_10_130_212_0_24_BD = {
#       name      = "DC_PRO_v22_10_130_212_0_24_BD"      
#     },
#       DC_PRO_v121_10_130_204_128_25_BD = {
#       name      = "DC_PRO_v121_10_130_204_128_25_BD"      
#     },
#       DC_PRO_v17_10_130_207_0_24_BD = {
#       name      = "DC_PRO_v17_10_130_207_0_24_BD"      
#     },
#       DC_PRO_v133_10_130_133_0_24_BD = {
#       name      = "DC_PRO_v133_10_130_133_0_24_BD"      
#     },
#       DC_PRO_v826_10_129_80_16_28_BD = {
#       name      = "DC_PRO_v826_10_129_80_16_28_BD"      
#     },
#       DC_PRO_v971_nonrouted_BD = {
#       name      = "DC_PRO_v971_nonrouted_BD"      
#     },
#       DC_PRO_v16_10_130_206_0_24_BD = {
#       name      = "DC_PRO_v16_10_130_206_0_24_BD"      
#     },
#       DC_PRO_v117_10_130_235_192_27_BD = {
#       name      = "DC_PRO_v117_10_130_235_192_27_BD"      
#     },
#       DC_PRO_v667_nonrouted_BD = {
#       name      = "DC_PRO_v667_nonrouted_BD"      
#     },
#       DC_PRO_v15_10_130_205_0_24_BD = {
#       name      = "DC_PRO_v15_10_130_205_0_24_BD"      
#     },
#       DC_PRO_v51_10_130_230_64_27_BD = {
#       name      = "DC_PRO_v51_10_130_230_64_27_BD"      
#     },
#       DC_PRO_v90_10_130_209_0_25_BD = {
#       name      = "DC_PRO_v90_10_130_209_0_25_BD"      
#     },
#       DC_PRO_v464_10_130_236_128_27_BD = {
#       name      = "DC_PRO_v464_10_130_236_128_27_BD"      
#     },                                                                    
#       DC_PRO_v464_10_130_236_128_27_BD = {
#       name      = "DC_PRO_v23_10_130_213_0_24_BD"      
#     },
#       DC_PRO_v52_10_130_228_64_27_BD = {
#       name      = "DC_PRO_v52_10_130_228_64_27_BD"      
#     },
#       DC_PRO_v49_10_130_221_192_29_BD = {
#       name      = "DC_PRO_v49_10_130_221_192_29_BD"      
#     },
#       DC_PRO_v825_10_129_80_16_28_BD = {
#       name      = "DC_PRO_v825_10_129_80_16_28_BD"      
#     },
#       DC_PRO_v89_10_130_248_0_24_BD = {
#       name      = "DC_PRO_v89_10_130_248_0_24_BD"      
#     },
#       DC_PRO_v490_10_130_239_0_24_BD = {
#       name      = "DC_PRO_v490_10_130_239_0_24_BD"      
#     },
#       DC_PRO_v14_10_130_204_0_25_BD = {
#       name      = "DC_PRO_v14_10_130_204_0_25_BD"      
#     },
#       DC_PRO_v462_10_130_236_64_27_BD = {
#       name      = "DC_PRO_v462_10_130_236_64_27_BD"      
#     },
#       DC_PRO_v110_10_130_211_0_25_BD = {
#       name      = "DC_PRO_v110_10_130_211_0_25_BD"      
#     },
#       DC_PRO_v386_10_130_228_192_27_BD = {
#       name      = "DC_PRO_v386_10_130_228_192_27_BD"      
#     },
#       DC_PRO_v76_10_130_209_128_25_BD = {
#       name      = "DC_PRO_v76_10_130_209_128_25_BD"      
#     },
#       DC_PRO_v149_10_129_80_224_27_BD = {
#       name      = "DC_PRO_v149_10_129_80_224_27_BD"      
#     },
#       DC_PRO_v115_10_130_235_0_27_BD = {
#       name      = "DC_PRO_v115_10_130_235_0_27_BD"      
#     },
#       DC_PRO_v180_10_130_208_0_27_BD = {
#       name      = "DC_PRO_v180_10_130_208_0_27_BD"      
#     },
#       DC_PRO_v137_10_130_137_0_24_BD = {
#       name      = "DC_PRO_v137_10_130_137_0_24_BD"      
#     },
#       DC_PRO_v122_10_130_235_64_26_BD = {
#       name      = "DC_PRO_v122_10_130_235_64_26_BD"      
#     },
#       DC_PRO_v40_10_130_230_0_26_BD = {
#       name      = "DC_PRO_v40_10_130_230_0_26_BD"      
#     },
#       DC_PRO_v3132_10_129_76_0_24_BD = {
#       name      = "DC_PRO_v3132_10_129_76_0_24_BD"      
#     },
#       DC_PRO_v29_10_130_219_0_24_BD = {
#       name      = "DC_PRO_v29_10_130_219_0_24_BD"      
#     },
#       DC_PRO_v13_10_130_203_0_24_BD = {
#       name      = "DC_PRO_v13_10_130_203_0_24_BD"      
#     },
#       DC_PRO_v8_10_130_198_0_24_BD = {
#       name      = "DC_PRO_v8_10_130_198_0_24_BD"      
#     },
#       DC_PRO_v406_10_130_230_192_27_BD = {
#       name      = "DC_PRO_v406_10_130_230_192_27_BD"      
#     },
#       DC_PRO_v139_10_130_139_0_24_BD = {
#       name      = "DC_PRO_v139_10_130_139_0_24_BD"      
#       }                                                                                               

#     }
  
# }


