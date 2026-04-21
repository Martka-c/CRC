resource "azurerm_resource_group" "rg_crc" {
  name     = "resource-group-crc"
  location = "westeurope"
}

resource "azurerm_resource_group" "rg_crc_var" {
  name     = var.resource_group_name
  location = var.location
}