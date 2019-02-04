# Terraform::Packet::Project

Provides a Packet Project resource to allow you manage devices
in your projects.

## Properties

`Name` - (Required) The name of the Project on Packet.net.

`PaymentMethodId` - The UUID of payment method for this project. If you keep it empty, Packet API will pick your default Payment Method.

`OrganizationId` - The UUID of Organization under which you want to create the project. If you leave it out, the project will be create under your the default Organization of your account.

`Asn` - Autonomous System Numer for local BGP deployment.

`Md5` - (Optional) Password for BGP session in plaintext (not a checksum).

`DeploymentType` - `private` or `public`, the `private` is likely to be usable immediately, the `public` will need to be review by Packet engineers.


## Return Values

### Fn::GetAtt

`Id` - The unique ID of the project.

`PaymentMethodId` - The UUID of payment method for this project.

`OrganizationId` - The UUID of this project's parent organization.

`Created` - The timestamp for when the Project was created.

`Updated` - The timestamp for the last time the Project was updated.

`Status` - status of BGP configuration in the project.

`MaxPrefix` - The maximum number of route filters allowed per server.

## See Also

* [packet_project](https://www.terraform.io/docs/providers/packet/r/project.html) in the _Terraform Provider Documentation_