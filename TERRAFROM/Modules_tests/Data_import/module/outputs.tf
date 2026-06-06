
output "tenant_dn" {
  value = aci_tenant.tenant.id
}

output "vrfs" {
  value = aci_vrf.vrf
}


output "bridge_dms" {
  description = "List of BDs"
  value = [
    for bd in aci_bridge_domain.bridge_domain : bd.id
  ]
}