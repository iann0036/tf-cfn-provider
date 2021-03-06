# Terraform::Alicloud::SlbCaCertificate

A Load Balancer CA Certificate is used by the listener of the protocol https.

For information about slb and how to use it, see [What is Server Load Balancer](https://www.alibabacloud.com/help/doc-detail/27539.htm).

For information about CA Certificate and how to use it, see [Configure CA Certificate](https://www.alibabacloud.com/help/doc-detail/85968.htm).

## Properties

`Name` - (Optional) Name of the CA Certificate.

`CaCertificate` - (Required, ForceNew) the content of the CA certificate.


## Return Values

### Fn::GetAtt

`Id` - The Id of CA Certificate .

## See Also

* [alicloud_slb_ca_certificate](https://www.terraform.io/docs/providers/alicloud/r/slb_ca_certificate.html) in the _Terraform Provider Documentation_