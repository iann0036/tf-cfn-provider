# Terraform::OCI::CoreInstanceConsoleConnection

This resource provides the Instance Console Connection resource in Oracle Cloud Infrastructure Core service.

Creates a new console connection to the specified instance.
Once the console connection has been created and is available,
you connect to the console using SSH.

For more information about console access, see [Accessing the Console](https://docs.cloud.oracle.com/iaas/Content/Compute/References/serialconsole.htm).

## Properties

`DefinedTags` - (Optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see [Resource Tags](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).  Example: `{"Operations.CostCenter": "42"}`.

`FreeformTags` - (Optional) Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see [Resource Tags](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).  Example: `{"Department": "Finance"}`.

`InstanceId` - (Required) The OCID of the instance to create the console connection to.

`PublicKey` - (Required) The SSH public key used to authenticate the console connection.


## Return Values

### Fn::GetAtt

`CompartmentId` - The OCID of the compartment to contain the console connection.

`ConnectionString` - The SSH connection string for the console connection.

`DefinedTags` - Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see [Resource Tags](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).  Example: `{"Operations.CostCenter": "42"}`.

`Fingerprint` - The SSH public key fingerprint for the console connection.

`FreeformTags` - Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see [Resource Tags](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).  Example: `{"Department": "Finance"}`.

`Id` - The OCID of the console connection.

`InstanceId` - The OCID of the instance the console connection connects to.

`State` - The current state of the console connection.

`VncConnectionString` - The SSH connection string for the SSH tunnel used to connect to the console connection over VNC.

## See Also

* [oci_core_instance_console_connection](https://www.terraform.io/docs/providers/oci/r/core_instance_console_connection.html) in the _Terraform Provider Documentation_