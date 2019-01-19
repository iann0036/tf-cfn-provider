# Terraform::Alicloud::SlbServerCertificate

A Load Balancer Server Certificate is an ssl Certificate used by the listener of the protocol https.

For information about slb and how to use it, see [What is Server Load Balancer](https://www.alibabacloud.com/help/doc-detail/27539.htm).

For information about Server Certificate and how to use it, see [Configure Server Certificate](https://www.alibabacloud.com/help/doc-detail/85968.htm).

## Properties

`Name` - (Optional) Name of the Server Certificate.

`ServerCertificate` - (Optional, ForceNew) the content of the ssl certificate. where `AlicloudCertificateId` is null, it is required, otherwise it is ignored.

`PrivateKey` - (Optional, ForceNew) the content of privat key of the ssl certificate specified by `ServerCertificate`. where `AlicloudCertificateId` is null, it is required, otherwise it is ignored.

`AlicloudCertificateId` - (Optional) an id of server certificate ssued/proxied by alibaba cloud. but it is not supported on the international site of alibaba cloud now.

`AlicloudCertificateName` - (Optional) the name of the certificate specified by `AlicloudCertificateId`.but it is not supported on the international site of alibaba cloud now.


## Return Values

### Fn::GetAtt

`Id` - The Id of Server Certificate (SSL Certificate).

## See Also

* [alicloud_slb_server_certificate](https://www.terraform.io/docs/providers/alicloud/r/slb_server_certificate.html) in the _Terraform Provider Documentation_