provider "azurerm" {
  features {}
}
terraform {
  backend "azurerm" {
    resource_group_name      = "nida"
    storage_account_name     = "practise1"
    container_name           = "mycontainer1"
    key                      = "terraform.tfstate"
  }
}

resource "azurerm_resource_group" "nida1" {
  name     = "example-resources2"
  location = "West Europe"
}


module "windowsservers" {
  source              = "Azure/compute/azurerm"
  resource_group_name = azurerm_resource_group.nida1.name
  is_windows_image    = true
  vm_hostname         = "mywinvm1" // line can be removed if only one VM module per resource group
  admin_password      = "ComplxP@ssw0rd!1"
  vm_os_simple        = "WindowsServer"
  public_ip_dns       = ["winsimplevmips2"] // change to a unique name per datacenter region
  vnet_subnet_id      = module.network.vnet_subnets[0]

  depends_on = [azurerm_resource_group.nida1]
}

module "network" {
  source              = "Azure/network/azurerm"
  resource_group_name = azurerm_resource_group.nida1.name
  subnet_prefixes     = ["10.0.1.0/24"]
  subnet_names        = ["subnet1"]

  depends_on = [azurerm_resource_group.nida1]
}


output "windows_vm_public_name" {
  value = module.windowsservers.public_ip_dns_name
}