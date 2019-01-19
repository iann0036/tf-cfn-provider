# Terraform::AWS::CloudhsmV2Cluster

Creates an Amazon CloudHSM v2 cluster.

For information about CloudHSM v2, see the
[AWS CloudHSM User Guide][1] and the [Amazon
CloudHSM API Reference][2].

~> **NOTE:** CloudHSM can take up to several minutes to be set up.
Practically no single attribute can be updated except TAGS.
If you need to delete a cluster, you have to remove its HSM modules first.
To initialize cluster you have to sign CSR and upload it.

## Properties

TBC

## Return Values

### Fn::GetAtt

`ClusterId` - The id of the CloudHSM cluster.

`ClusterState` - The state of the cluster.

`VpcId` - The id of the VPC that the CloudHSM cluster resides in.

`SecurityGroupId` - The ID of the security group associated with the CloudHSM cluster.

`ClusterCertificates` - The list of cluster certificates.

`ClusterCertificates.0.clusterCertificate` - The cluster certificate issued (signed) by the issuing certificate authority (CA) of the cluster's owner.

`ClusterCertificates.0.clusterCsr` - The certificate signing request (CSR). Available only in UNINITIALIZED state.

`ClusterCertificates.0.awsHardwareCertificate` - The HSM hardware certificate issued (signed) by AWS CloudHSM.

`ClusterCertificates.0.hsmCertificate` - The HSM certificate issued (signed) by the HSM hardware.

`ClusterCertificates.0.manufacturerHardwareCertificate` - The HSM hardware certificate issued (signed) by the hardware manufacturer.

## See Also

* [aws_cloudhsm_v2_cluster](https://www.terraform.io/docs/providers/aws/r/cloudhsm_v2_cluster.html) in the _Terraform Provider Documentation_