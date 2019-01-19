# Terraform::VSphere::CustomAttribute

The `vsphere_custom_attribute` resource can be used to create and manage custom
attributes, which allow users to associate user-specific meta-information with 
vSphere managed objects. Custom attribute values must be strings and are stored 
on the vCenter Server and not the managed object.

For more information about custom attributes, click [here][ext-custom-attributes].

[ext-custom-attributes]: https://docs.vmware.com/en/VMware-vSphere/6.5/com.vmware.vsphere.vcenterhost.doc/GUID-73606C4C-763C-4E27-A1DA-032E4C46219D.html

~> **NOTE:** Custom attributes are unsupported on direct ESXi connections 
and require vCenter.

## Return Values

### Fn::GetAtt

Fn::GetAtt returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

## See Also

* [vsphere_custom_attribute](https://www.terraform.io/docs/providers/vsphere/r/custom_attribute.html) in the _Terraform Provider Documentation_