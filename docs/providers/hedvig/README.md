# Hedvig Provider

## Configuration

To configure this resource, you may optionally create an AWS Secrets Manager secret with the name **terraform/hedvig**. The below arguments may be included as the key/value or JSON properties in the secret:

* `username` - The username used to log into a node of the cluster for resource
   creation.

* `password` - The password that corresponds to the username used for logging
   into the cluster.

* `node` - The node that will be used to connect to in the cluster that resources
   will be created on.


## Supported Resources

* [Terraform::Hedvig::Access](Access.md)
* [Terraform::Hedvig::Lun](Lun.md)
* [Terraform::Hedvig::Mount](Mount.md)
* [Terraform::Hedvig::Vdisk](Vdisk.md)