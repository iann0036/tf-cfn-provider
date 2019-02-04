# Terraform::Google::ComputeInstance

Manages a VM instance resource within GCE. For more information see
[the official documentation](https://cloud.google.com/compute/docs/instances)
and
[API](https://cloud.google.com/compute/docs/reference/latest/instances).

## Properties

`BootDisk` - (Required) The boot disk for the instance.
Structure is documented below.

`MachineType` - (Required) The machine type to create.

`Name` - (Required) A unique name for the resource, required by GCE.
Changing this forces a new resource to be created.

`Zone` - (Required) The zone that the machine should be created in.

`NetworkInterface` - (Required) Networks to attach to the instance. This can
be specified multiple times. Structure is documented below.

`AllowStoppingForUpdate` - (Optional) If true, allows Terraform to stop the instance to update its properties.
If you try to update a property that requires stopping the instance without setting this field, the update will fail.

`AttachedDisk` - (Optional) Additional disks to attach to the instance. Can be repeated multiple times for multiple disks. Structure is documented below.

`CanIpForward` - (Optional) Whether to allow sending and receiving of
packets with non-matching source or destination IPs.
This defaults to false.

`CreateTimeout` - (Optional) Configurable timeout in minutes for creating instances. Default is 4 minutes.
Changing this forces a new resource to be created.

`Description` - (Optional) A brief description of this resource.

`DeletionProtection` - (Optional) Enable deletion protection on this instance. Defaults to false.
**Note:** you must disable deletion protection before removing the resource (e.g., via `terraform destroy`), or the instance cannot be deleted and the Terraform run will not complete successfully.

`Hostname` - (Optional) A custom hostname for the instance. Must be a fully qualified DNS name and RFC-1035-valid.
Valid format is a series of labels 1-63 characters long matching the regular expression `[a-z]([-a-z0-9]*[a-z0-9])`, concatenated with periods.
The entire hostname must not exceed 253 characters. Changing this forces a new resource to be created.

`GuestAccelerator` - (Optional) List of the type and count of accelerator cards attached to the instance. Structure documented below.
**Note:** GPU accelerators can only be used with [`OnHostMaintenance`](#on_host_maintenance) option set to TERMINATE.

`Labels` - (Optional) A set of key/value label pairs to assign to the instance.

`Metadata` - (Optional) Metadata key/value pairs to make available from
within the instance. Ssh keys attached in the Cloud Console will be removed.
Add them to your config in order to keep them attached to your instance.

`MetadataStartupScript` - (Optional) An alternative to using the
startup-script metadata key, except this one forces the instance to be
recreated (thus re-running the script) if it is changed. This replaces the
startup-script metadata key on the created instance and thus the two
mechanisms are not allowed to be used simultaneously.

`MinCpuPlatform` - (Optional) Specifies a minimum CPU platform for the VM instance. Applicable values are the friendly names of CPU platforms, such as
`Intel Haswell` or `Intel Skylake`. See the complete list [here](https://cloud.google.com/compute/docs/instances/specify-min-cpu-platform).
**Note**: [`AllowStoppingForUpdate`](#allow_stopping_for_update) must be set to true in order to update this field.

`Project` - (Optional) The ID of the project in which the resource belongs. If it
is not provided, the provider project is used.

`Scheduling` - (Optional) The scheduling strategy to use. More details about
this configuration option are detailed below.

`ScratchDisk` - (Optional) Scratch disks to attach to the instance. This can be
specified multiple times for multiple scratch disks. Structure is documented below.

`ServiceAccount` - (Optional) Service account to attach to the instance.
Structure is documented below.
**Note**: [`AllowStoppingForUpdate`](#allow_stopping_for_update) must be set to true in order to update this field.

`Tags` - (Optional) A list of tags to attach to the instance.

### BootDisk Properties

`AutoDelete` - (Optional) Whether the disk will be auto-deleted when the instance
is deleted. Defaults to true.

`DeviceName` - (Optional) Name with which attached disk will be accessible.
On the instance, this device will be `/dev/disk/by-id/google-{{device_name}}`.

`DiskEncryptionKeyRaw` - (Optional) A 256-bit [customer-supplied encryption key]
(https://cloud.google.com/compute/docs/disks/customer-supplied-encryption),
encoded in [RFC 4648 base64](https://tools.ietf.org/html/rfc4648#section-4)
to encrypt this disk.

`InitializeParams` - (Optional) Parameters for a new disk that will be created
alongside the new instance. Either `InitializeParams` or `Source` must be set.
Structure is documented below.

`Source` - (Optional) The name or self_link of the existing disk (such as those managed by
`Terraform::Google::ComputeDisk`) to attach.

### InitializeParams Properties

`Size` - (Optional) The size of the image in gigabytes. If not specified, it
will inherit the size of its base image.

`Type` - (Optional) The GCE disk type. May be set to pd-standard or pd-ssd.

`Image` - (Optional) The image from which to initialize this disk. This can be
one of: the image's `self_link`, `projects/{project}/global/images/{image}`,
`projects/{project}/global/images/family/{family}`, `global/images/{image}`,
`global/images/family/{family}`, `family/{family}`, `{project}/{family}`,
`{project}/{image}`, `{family}`, or `{image}`. If referred by family, the
images names must include the family name. If they don't, use the
[google_compute_image data source](/docs/providers/google/d/datasource_compute_image.html).
For instance, the image `centos-6-v20180104` includes its family name `centos-6`.
These images can be referred by family name here.

### ScratchDisk Properties

`Interface` - (Optional) The disk interface to use for attaching this disk; either SCSI or NVME.
Defaults to SCSI.

### AttachedDisk Properties

`Source` - (Required) The name or self_link of the disk to attach to this instance.

`DeviceName` - (Optional) Name with which the attached disk will be accessible
under `/dev/disk/by-id/`.

`Mode` - (Optional) Either "READ_ONLY" or "READ_WRITE", defaults to "READ_WRITE"
If you have a persistent disk with data that you want to share
between multiple instances, detach it from any read-write instances and
attach it to one or more instances in read-only mode.

`DiskEncryptionKeyRaw` - (Optional) A 256-bit [customer-supplied encryption key]
(https://cloud.google.com/compute/docs/disks/customer-supplied-encryption),
encoded in [RFC 4648 base64](https://tools.ietf.org/html/rfc4648#section-4)
to encrypt this disk.

### NetworkInterface Properties

`Network` - (Optional) The name or self_link of the network to attach this interface to.
Either `Network` or `Subnetwork` must be provided.

`Subnetwork` - (Optional) The name or self_link of the subnetwork to attach this
interface to. The subnetwork must exist in the same region this instance will be
created in. Either `Network` or `Subnetwork` must be provided.

`SubnetworkProject` - (Optional) The project in which the subnetwork belongs.
If the `Subnetwork` is a self_link, this field is ignored in favor of the project
defined in the subnetwork self_link. If the `Subnetwork` is a name and this
field is not provided, the provider project is used.

`NetworkIp` - (Optional) The private IP address to assign to the instance. If
empty, the address will be automatically assigned.

`AccessConfig` - (Optional) Access configurations, i.e. IPs via which this
instance can be accessed via the Internet. Omit to ensure that the instance
is not accessible from the Internet (this means that ssh provisioners will
not work unless you are running Terraform can send traffic to the instance's
network (e.g. via tunnel or because it is running on another cloud instance
on that network). This block can be repeated multiple times. Structure
documented below.

`AliasIpRange` - (Optional) An
array of alias IP ranges for this network interface. Can only be specified for network
interfaces on subnet-mode networks. Structure documented below.

### AccessConfig Properties

`NatIp` - (Optional) The IP address that will be 1:1 mapped to the instance's
network ip. If not given, one will be generated.

`PublicPtrDomainName` - (Optional) The DNS domain name for the public PTR record.
To set this field on an instance, you must be verified as the owner of the domain.
See [the docs](https://cloud.google.com/compute/docs/instances/create-ptr-record) for how
to become verified as a domain owner.

`NetworkTier` - (Optional) The [networking tier][network-tier] used for configuring this instance.
This field can take the following values: PREMIUM or STANDARD. If this field is
not specified, it is assumed to be PREMIUM.

### AliasIpRange Properties

`IpCidrRange` - The IP CIDR range represented by this alias IP range. This IP CIDR range
must belong to the specified subnetwork and cannot contain IP addresses reserved by
system or used by other network interfaces. This range may be a single IP address
(e.g. 10.2.3.4), a netmask (e.g. /24) or a CIDR format string (e.g. 10.1.2.0/24).

`SubnetworkRangeName` - (Optional) The subnetwork secondary range name specifying
the secondary range from which to allocate the IP CIDR range for this alias IP
range. If left unspecified, the primary range of the subnetwork will be used.

### ServiceAccount Properties

`Email` - (Optional) The service account e-mail address. If not given, the
default Google Compute Engine service account is used.
**Note**: [`AllowStoppingForUpdate`](#allow_stopping_for_update) must be set to true in order to update this field.

`Scopes` - (Required) A list of service scopes. Both OAuth2 URLs and gcloud
short names are supported. To allow full access to all Cloud APIs, use the
`cloud-platform` scope. See a complete list of scopes [here](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/instances/set-scopes#--scopes).
**Note**: [`AllowStoppingForUpdate`](#allow_stopping_for_update) must be set to true in order to update this field.

### Scheduling Properties

`Preemptible` - (Optional) Is the instance preemptible.

`OnHostMaintenance` - (Optional) Describes maintenance behavior for the
instance. Can be MIGRATE or TERMINATE, for more info, read
[here](https://cloud.google.com/compute/docs/instances/setting-instance-scheduling-options).

`AutomaticRestart` - (Optional) Specifies if the instance should be
restarted if it was terminated by Compute Engine (not a user).


## Return Values

### Fn::GetAtt

`InstanceId` - The server-assigned unique identifier of this instance.

`MetadataFingerprint` - The unique fingerprint of the metadata.

`SelfLink` - The URI of the created resource.

`TagsFingerprint` - The unique fingerprint of the tags.

`LabelFingerprint` - The unique fingerprint of the labels.

`CpuPlatform` - The CPU platform used by this instance.

`NetworkInterface.0.networkIp` - The internal ip address of the instance, either manually or dynamically assigned.

`NetworkInterface.0.accessConfig.0.natIp` - If the instance has an access config, either the given external ip (in the `NatIp` field) or the ephemeral (generated) ip (if you didn't provide one).

`AttachedDisk.0.diskEncryptionKeySha256` - The [RFC 4648 base64](https://tools.ietf.org/html/rfc4648#section-4).

`BootDisk.diskEncryptionKeySha256` - The [RFC 4648 base64](https://tools.ietf.org/html/rfc4648#section-4).

`Disk.0.diskEncryptionKeySha256` - The [RFC 4648 base64](https://tools.ietf.org/html/rfc4648#section-4).

## See Also

* [google_compute_instance](https://www.terraform.io/docs/providers/google/r/compute_instance.html) in the _Terraform Provider Documentation_