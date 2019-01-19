# Terraform::RightScale::Instance

Use this resource to create, update or destroy RightScale [instances](http://reference.rightscale.com/api1.5/resources/ResourceInstances.html).

## Properties

`Name` - (Required) The name of the instance.

`CloudHref` - (Required) The cloud_href the instance belongs to.

`ImageHref` - (Required) The href of the instance image.

`InstanceTypeHref` - (Required) The href of the instance type.

`ServerTemplateHref` - (Optional) The href of the instance server template resource.

`Inputs` - (Optional) Inputs associated with an instance when incarnated from a [server](https://github.com/terraform-providers/terraform-provider-rightscale/blob/master/website/docs/r/cm_server.markdown) or [server_array](https://github.com/terraform-providers/terraform-provider-rightscale/blob/master/website/docs/r/cm_server_array.markdown).

`AssociatePublicIpAddress` - (Optional) Indicates if the instance will get a Public IP address.

`DatacenterHref` - (Optional) The href of the datacenter that holds the instance (e.g. /api/clouds/6/datacenters/6IHONC8ANOUHI).

`DeploymentHref` - (Optional) The href of the deployment that contains the instance (e.g. /api/deployments/594684003).

`IpForwardingEnabled` - (Optional) Allows this Instance to send and receive network traffic when the source and destination IP addresses do not match the IP address of this Instance.

`PrivateIpAddress` - (Optional) The private ip address of this instance.

`KernelImageHref` - (Optional) The href of the instance kernel image.

`RamdiskImageHref` - (Optional) The href of the instance ramdisk image.

`SecurityGroupHrefs` - (Optional) The href of the instance security groups.

`PlacementGroupHref` - (Optional) The href of the [placement_group](http://docs.rightscale.com/cm/dashboard/clouds/aws/ec2_placement_groups.html) that contains the instance (e.g. /api/placement_groups/512SV3FUJA7OO).

`SshKeyHref` - (Optional) The href of the SSH key to use.

`SubnetHrefs` - (Optional) The hrefs of the instance subnet.

`UserData` - (Optional) User data that RightScale automatically passes to your instance at boot time.

`Locked` - (Optional)  Whether instance is locked, a locked instance cannot be terminated or deleted.

`CloudSpecificAttributes` - (Optional) Attributes specific to the cloud the instance belongs to that have no specific rightscale abstraction.  This block supports:.

### CloudSpecificAttributes Properties

`AdminUsername` - The user that will be granted administrative privileges. Supported by AzureRM cloud only.

`AutomaticInstanceStoreMapping` - A flag indicating whether instance store mapping should be enabled.  Only available on clouds supporting automatic instance store mapping.

`AvailabilitySet` - Availability set for raw instance. Supported by Azure v2 cloud only.

`CreateBootVolume` - If enabled, the instance will launch into volume storage. Otherwise, it will boot to local storage.  Only available on clouds supporting this option.

`CreateDefaultPortForwardingRules` - Automatically create default port forwarding rules (enabled by default). Supported by Azure cloud only.

`DeleteBootVolume` - If enabled, the associated volume will be deleted when the instance is terminated.  Only available on clouds supporting this option.

`DiskGb` - The size of root disk. Supported by UCA cloud only.

`EbsOptimized` - Whether the instance is able to connect to IOPS-enabled volumes.  AWS clouds only.

`IamInstanceProfile` - The name or ARN of the IAM Instance Profile (IIP) to associate with the instance. AWS clouds only.

`KeepAliveId` - The id of keep alive. Supported by UCA cloud only.

`LocalSsdCount` - Additional local SSDs. Supported by GCE cloud only.

`LocalSsdInterface` - The type of SSD(s) to be created. Supported by GCE cloud only.

`MaxSpotPrice` - Specify the max spot price you will pay for. Required when 'pricing_type' is 'spot'. Only applies to clouds which support spot-pricing and when 'spot' is chosen as the 'pricing_type'. Should be a Float value >= 0.001, eg: 0.095, 0.123, 1.23, etc... AWS clouds only.

`MemoryMb` - The size of instance memory. Supported by UCA cloud only.

`Metadata"` - Extra data used for configuration, in query string format. AWS clouds only.

`NumCores` - The number of instance cores. Supported by UCA cloud only.

`PlacementTenancy` - The tenancy of the server you want to launch. A server with a tenancy of dedicated runs on single-tenant hardware and can only be launched into a VPC.  AWS clouds only.

`Preemptible` - Launch a preemptible instance. A preemptible instance costs much less, but lasts only 24 hours. It can be terminated sooner due to system demands. Supported by GCE cloud only.

`PricingType` - Specify whether or not you want to utilize 'fixed' (on-demand) or 'spot' pricing. Defaults to 'fixed' and only applies to clouds which support spot instances. Can only be set on when creating a new Instance, Server, or ServerArray, or when updating a Server or ServerArray's next_instance.  AWS clouds only.

`RootVolumePerformance` - The number of IOPS (I/O Operations Per Second) this root volume should support. Only available on clouds supporting performance provisioning.

`RootVolumeSize` - The size for root disk. Only available on clouds supporting dynamic resizing of root volume size.

`RootVolumeTypeUid` - The type of root volume for instance. Only available on clouds supporting root volume type.

`ServiceAccount` - Email of service account for instance. Scope will default to cloud-platform. Supported by GCE cloud only.


## Return Values

### Fn::GetAtt

`Links` - Hrefs of related API resources.

`CreatedAt` - Datestamp of instance creation.

`UpdatedAt` - Datestamp of when instance was updated last.

`State` - The state of the instance (operational, terminating, pending, stranded, etc.).

`Href` - Href of the instance.

`ResourceUid` - Cloud resource_uid as reported by cm platform.

`PublicIpAddresses` - List of public IP addresses associated to the instance.

`PrivateIpAddresses` - List of private IP addresses associated to the instance.

## See Also

* [rightscale_instance](https://www.terraform.io/docs/providers/rightscale/r/instance.html) in the _Terraform Provider Documentation_