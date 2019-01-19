# Terraform::AzureRM::ServiceFabricCluster

Manage a Service Fabric Cluster.

## Properties

`ResourceGroupName` - (Required) The name of the Resource Group in which the Service Fabric Cluster exists. Changing this forces a new resource to be created.

`Location` - (Required) Specifies the Azure Region where the Service Fabric Cluster should exist. Changing this forces a new resource to be created.

`ReliabilityLevel` - (Required) Specifies the Reliability Level of the Cluster. Possible values include `None`, `Bronze`, `Silver`, `Gold` and `Platinum`.

`ManagementEndpoint` - (Required) Specifies the Management Endpoint of the cluster such as `http://example.com`. Changing this forces a new resource to be created.

`NodeType` - (Required) One or more `NodeType` blocks as defined below.

`UpgradeMode` - (Required) Specifies the Upgrade Mode of the cluster. Possible values are `Automatic` or `Manual`.

`VmImage` - (Required) Specifies the Image expected for the Service Fabric Cluster, such as `Windows`. Changing this forces a new resource to be created.

`ClusterCodeVersion` - (Optional) Required if Upgrade Mode set to `Manual`, Specifies the Version of the Cluster Code of the cluster.

`AddOnFeatures` - (Optional) A List of one or more features which should be enabled, such as `DnsService`.

`AzureActiveDirectory` - (Optional) An `AzureActiveDirectory` block as defined below. Changing this forces a new resource to be created.

`Certificate` - (Optional) A `Certificate` block as defined below.

`ReverseProxyCertificate` - (Optional) A `ReverseProxyCertificate` block as defined below.

`ClientCertificateThumbprint` - (Optional) One or two `ClientCertificateThumbprint` blocks as defined below.

`DiagnosticsConfig` - (Optional) A `DiagnosticsConfig` block as defined below. Changing this forces a new resource to be created.

`FabricSettings` - (Optional) One or more `FabricSettings` blocks as defined below.

`Tags` - (Optional) A mapping of tags to assign to the resource.

### DiagnosticsConfig Properties

`StorageAccountName` - (Required) The name of the Storage Account where the Diagnostics should be sent to.

`ProtectedAccountKeyName` - (Required) The protected diagnostics storage key name, such as `StorageAccountKey1`.

`BlobEndpoint` - (Required) The Blob Endpoint of the Storage Account.

`QueueEndpoint` - (Required) The Queue Endpoint of the Storage Account.

`TableEndpoint` - (Required) The Table Endpoint of the Storage Account.

### FabricSettings Properties

`Parameters` - (Optional) A map containing settings for the specified Fabric Setting.

### EphemeralPorts Properties

`StartPort` - (Required) The start of the Ephemeral Port Range on this Node Type.

`EndPort` - (Required) The end of the Ephemeral Port Range on this Node Type.

### ReverseProxyCertificate Properties

`ThumbprintSecondary` - (Required) The Secondary Thumbprint of the Certificate.

`X509StoreName` - (Required) The X509 Store where the Certificate Exists, such as `My`.

### AzureActiveDirectory Properties

`TenantId` - (Required) The Azure Active Directory Tenant ID. Changing this forces a new resource to be created.

`ClusterApplicationId` - (Required) The Azure Active Directory Client ID which should be used for the Client Application. Changing this forces a new resource to be created.

### NodeType Properties

`Name` - (Required) The name of the Node Type. Changing this forces a new resource to be created.

`InstanceCount` - (Required) The number of nodes for this Node Type.

`IsPrimary` - (Required) Is this the Primary Node Type? Changing this forces a new resource to be created.

`ClientEndpointPort` - (Required) The Port used for the Client Endpoint for this Node Type. Changing this forces a new resource to be created.

`HttpEndpointPort` - (Required) The Port used for the HTTP Endpoint for this Node Type. Changing this forces a new resource to be created.

`DurabilityLevel` - (Optional) The Durability Level for this Node Type. Possible values include `Bronze`, `Gold` and `Silver`. Defaults to `Bronze`. Changing this forces a new resource to be created.

`ApplicationPorts` - (Optional) A `ApplicationPorts` block as defined below.

`EphemeralPorts` - (Optional) A `EphemeralPorts` block as defined below.

`ReverseProxyEndpointPort` - (Optional) The Port used for the Reverse Proxy Endpoint  for this Node Type. Changing this will upgrade the cluster.

### ClientCertificateThumbprint Properties

`Thumbprint` - (Required) The Thumbprint associated with the Client Certificate.

`IsAdmin` - (Required) Does the Client Certificate have Admin Access to the cluster? Non-admin clients can only perform read only operations on the cluster.


## Return Values

### Fn::GetAtt

`Id` - The ID of the Service Fabric Cluster.

`ClusterEndpoint` - The Cluster Endpoint for this Service Fabric Cluster.

## See Also

* [azurerm_service_fabric_cluster](https://www.terraform.io/docs/providers/azurerm/r/service_fabric_cluster.html) in the _Terraform Provider Documentation_