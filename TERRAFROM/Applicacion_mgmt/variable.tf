variable "user" {
  description = "Login information"
  type        = map
  default     = {
  username = "paco"
  password = "!v3G@!4@Y"
  url      = "https://10.129.123.4/"
  }
}


variable "tenant" {
    type    = string
    default = "terraform-tenant"
}
variable "vrf" {
    type    = string
    default = "alfredolanda"
}
variable "bd" {
    type    = string
    default = "pacomartinezsoria"
  #  type = map
  #  default = {
  #    porridge1 = {
  #       description  = "locaza 1",
  #       arp_flood     = "yes"
  #       },
  #    porridge2 = {
  #       description   = "locaza2",
  #       arp_flood     = "no",

  #    }
  #  }
 }


variable "ap" {
    description = "Create application profile"
    type        = string
    default     = "intranet"
}




#   type = map(object({
#     name = string
#     arp_flood = string
#     type = string
#     gateway = string
#     scope = list(string)
#   }))
#   default = {
#     default_bd = {
#       name = "default"
#       arp_flood = "yes"
#       type = "L3"
#       gateway = "192.168.1.1/24"
#       scope = ["private"]
#     }
#  }
# }



# }
# variable "subnet" {
#     type    = string
#     default = "10.10.101.1/24"
# }



# variable "ap" {
#     description = "Create application profile"
#     type        = string
#     default     = "intranet"
# }



# variable "epgs" {
#     description = "Create epg"
#     type        = map
#     default     = {
#         web_epg = {
#             epg   = "web",
#             bd    = "prod_bd",
#             encap = "21"
#         },
#         db_epg = {
#             epg   = "db",
#             bd    = "prod_bd",
#             encap = "22"
#         }
#     }
# }



# variable "epg_contracts" {
#     description = "epg contracts"
#     type        = map
#     default     = {
#         terraform_one = {
#             epg           = "web_epg",
#             contract      = "contract_web",
#             contract_type = "provider" 
#         },
#         terraform_two = {
#             epg           = "web_epg",
#             contract      = "contract_sql",
#             contract_type = "consumer" 
#         },
#         terraform_three = {
#             epg           = "db_epg",
#             contract      = "contract_sql",
#             contract_type = "provider" 
#         }
#     }
# }





# variable "filters" {
#   description = "Create filters with these names and ports"
#   type        = map
#   default     = {
#     filter_https = {
#       filter   = "https",
#       entry    = "https",
#       protocol = "tcp",
#       port     = "443"
#     },
#     filter_sql = {
#       filter   = "sql",
#       entry    = "sql",
#       protocol = "tcp",
#       port     = "1433"
#     }
#   }
# }
# variable "contracts" {
#   description = "Create contracts with these filters"
#   type        = map
#   default     = {
#     contract_web = {
#       contract = "web",
#       subject  = "https",
#       filter   = "filter_https"
#     },
#     contract_sql = {
#       contract = "sql",
#       subject  = "sql",
#       filter   = "filter_sql"
#     }
#   }
# }

