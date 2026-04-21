variable "resource_group_name" {
  description = "Name of the resource group"
  type        = string
  default     = "crc-resource-group"
}

variable "location" {
  description = "Azure region for resources"
  type        = string
  default     = "westeurope"
}
