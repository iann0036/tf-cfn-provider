# Terraform::Google::ComputeInstanceTemplate

Manages a VM instance template resource within GCE. For more information see
[the official documentation](https://cloud.google.com/compute/docs/instance-templates)
and
[API](https://cloud.google.com/compute/docs/reference/latest/instanceTemplates).

## Properties

`Disk` - (Required) Disks to attach to instances created from this template. This can be specified multiple times for multiple disks. Structure is documented below.

`MachineType` - (Required) The machine type to create.

`Name` - (Optional) The name of the instance template. If you leave this blank, Terraform will auto-generate a unique name.

`NamePrefix` - (Optional) Creates a unique name beginning with the specified prefix. Conflicts with `Name`.

`CanIpForward` - (Optional) Whether to allow sending and receiving of packets with non-matching source or destination IPs. This defaults to false.

`Description` - (Optional) A brief description of this resource.

`InstanceDescription` - (Optional) A brief description to use for instances created from this template.

`Labels` - (Optional) A set of key/value label pairs to assign to instances created from this template,.

`Metadata` - (Optional) Metadata key/value pairs to make available from within instances created from this template.

`MetadataStartupScript` - (Optional) An alternative to using the startup-script metadata key, mostly to match the compute_instance resource. This replaces the startup-script metadata key on the created instance and thus the two mechanisms are not allowed to be used simultaneously.

`NetworkInterface` - (Required) Networks to attach to instances created from this template. This can be specified multiple times for multiple networks. Structure is documented below.

`Project` - (Optional) The ID of the project in which the resource belongs. If it is not provided, the provider project is used.

`Region` - (Optional) An instance template is a global resource that is not bound to a zone or a region. However, you can still specify some regional resources in an instance template, which restricts the template to the region where that resource resides. For example, a custom `Subnetwork` resource is tied to a specific region. Defaults to the region of the Provider if no value is given.

`Scheduling` - (Optional) The scheduling strategy to use. More details about this configuration option are detailed below.

`ServiceAccount` - (Optional) Service account to attach to the instance. Structure is documented below.

`Tags` - (Optional) Tags to attach to the instance.

`GuestAccelerator` - (Optional) List of the type and count of accelerator cards attached to the instance. Structure documented below.

`MinCpuPlatform` - (Optional) Specifies a minimum CPU platform. Applicable values are the friendly names of CPU platforms, such as `Intel Haswell` or `Intel Skylake`. See the complete list [here](https://cloud.google.com/compute/docs/instances/specify-min-cpu-platform).

`AutoDelete` - (Optional) Whether or not the disk should be auto-deleted. This defaults to true.

`Boot` - (Optional) Indicates that this is a boot disk.

`DeviceName` - (Optional) A unique device name that is reflected into the /dev/  tree of a Linux operating system running within the instance. If not specified, the server chooses a default device name to apply to this disk.

`DiskName` - (Optional) Name of the disk. When not provided, this defaults to the name of the instance.

`SourceImage` - (Required if source not set) The image from which to initialize this disk. This can be one of: the image's `self_link`, `projects/{project}/global/images/{image}`, `projects/{project}/global/images/family/{family}`, `global/images/{image}`, `global/images/family/{family}`, `family/{family}`, `{project}/{family}`, `{project}/{image}`, `{family}`, or `{image}`.

`Interface` - (Optional) Specifies the disk interface to use for attaching this disk.

`Mode` - (Optional) The mode in which to attach this disk, either READ_WRITE or READ_ONLY. If you are attaching or creating a boot disk, this must read-write mode.

`Source` - (Required if source_image not set) The name (**not self_link**) of the disk (such as those managed by `Terraform::Google::ComputeDisk`) to attach.

`DiskType` - (Optional) The GCE disk type. Can be either `"pd-ssd"`, `"local-ssd"`, or `"pd-standard"`.

`DiskSizeGb` - (Optional) The size of the image in gigabytes. If not specified, it will inherit the size of its base image.

`Type` - (Optional) The type of GCE disk, can be either `"SCRATCH"` or `"PERSISTENT"`.

`DiskEncryptionKey` - (Optional) Encrypts or decrypts a disk using a customer-supplied encryption key.

`KmsKeySelfLink` - (Optional) The self link of the encryption key that is stored in Google Cloud KMS.

`Network` - (Optional) The name or self_link of the network to attach this interface to. Use `Network` attribute for Legacy or Auto subnetted networks and `Subnetwork` for custom subnetted networks.

`Subnetwork` - (Optional) the name of the subnetwork to attach this interface to. The subnetwork must exist in the same `Region` this instance will be created in. Either `Network` or `Subnetwork` must be provided.

`SubnetworkProject` - (Optional) The ID of the project in which the subnetwork belongs. If it is not provided, the provider project is used.

`NetworkIp` - (Optional) The private IP address to assign to the instance. If empty, the address will be automatically assigned.

`AccessConfig` - (Optional) Access configurations, i.e. IPs via which this instance can be accessed via the Internet. Omit to ensure that the instance is not accessible from the Internet (this means that ssh provisioners will not work unless you are running Terraform can send traffic to the instance's network (e.g. via tunnel or because it is running on another cloud instance on that network). This block can be repeated multiple times. Structure documented below.

`AliasIpRange` - (Optional) An array of alias IP ranges for this network interface. Can only be specified for network interfaces on subnet-mode networks. Structure documented below.

`NatIp` - (Optional) The IP address that will be 1:1 mapped to the instance's network ip. If not given, one will be generated.

`NetworkTier` - (Optional) The [networking tier][network-tier] used for configuring this instance template. This field can take the following values: PREMIUM or STANDARD. If this field is not specified, it is assumed to be PREMIUM.

`IpCidrRange` - The IP CIDR range represented by this alias IP range. This IP CIDR range must belong to the specified subnetwork and cannot contain IP addresses reserved by system or used by other network interfaces. At the time of writing only a netmask (e.g. /24) may be supplied, with a CIDR format resulting in an API error.

`SubnetworkRangeName` - (Optional) The subnetwork secondary range name specifying the secondary range from which to allocate the IP CIDR range for this alias IP range. If left unspecified, the primary range of the subnetwork will be used.

`Email` - (Optional) The service account e-mail address. If not given, the default Google Compute Engine service account is used.

`Scopes` - (Required) A list of service scopes. Both OAuth2 URLs and gcloud short names are supported. To allow full access to all Cloud APIs, use the `cloud-platform` scope. See a complete list of scopes [here](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/instances/set-scopes#--scopes).

`AutomaticRestart` - (Optional) Specifies whether the instance should be automatically restarted if it is terminated by Compute Engine (not terminated by a user). This defaults to true.

`OnHostMaintenance` - (Optional) Defines the maintenance behavior for this instance.

`Preemptible` - (Optional) Allows instance to be preempted. This defaults to false. Read more on this [here](https://cloud.google.com/compute/docs/instances/preemptible).


## Return Values

### Fn::GetAtt

`MetadataFingerprint` - The unique fingerprint of the metadata.

`SelfLink` - The URI of the created resource.

`TagsFingerprint` - The unique fingerprint of the tags.

## See Also

* [google_compute_instance_template](https://www.terraform.io/docs/providers/google/r/compute_instance_template.html) in the _Terraform Provider Documentation_