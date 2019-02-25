# Terraform::Linode::NodebalancerConfig

Provides a Linode NodeBalancer Config resource.  This can be used to create, modify, and delete Linodes NodeBalancer Configs.
For more information, see [Getting Started with NodeBalancers](https://www.linode.com/docs/platform/nodebalancer/getting-started-with-nodebalancers/) and the [Linode APIv4 docs](https://developers.linode.com/api/v4#operation/createNodeBalancerConfig).

The Linode Guide, [Create a NodeBalancer with Terraform](https://www.linode.com/docs/applications/configuration-management/create-a-nodebalancer-with-terraform/), provides step-by-step guidance and additional examples.

## Properties

`NodebalancerId` - (Required) The ID of the NodeBalancer to access.

`Region` - (Required) The region where this nodebalancer_config will be deployed.  Examples are `"us-east"`, `"us-west"`, `"ap-south"`, etc.  *Changing `Region` forces the creation of a new Linode NodeBalancer Config.*.

`Protocol` - (Optional) The protocol this port is configured to serve. If this is set to https you must include an ssl_cert and an ssl_key. (Defaults to "http").

`Port` - (Optional) The TCP port this Config is for. These values must be unique across configs on a single NodeBalancer (you can't have two configs for port 80, for example). While some ports imply some protocols, no enforcement is done and you may configure your NodeBalancer however is useful to you. For example, while port 443 is generally used for HTTPS, you do not need SSL configured to have a NodeBalancer listening on port 443. (Defaults to 80).

`Algorithm` - (Optional) What algorithm this NodeBalancer should use for routing traffic to backends: roundrobin, leastconn, source.

`Stickiness` - (Optional) Controls how session stickiness is handled on this port: 'none', 'table', 'http_cookie'.

`Check` - (Optional) The type of check to perform against backends to ensure they are serving requests. This is used to determine if backends are up or down. If none no check is performed. connection requires only a connection to the backend to succeed. http and http_body rely on the backend serving HTTP, and that the response returned matches what is expected.

`CheckInterval` - (Optional) How often, in seconds, to check that backends are up and serving requests.

`CheckTimeout` - (Optional) How long, in seconds, to wait for a check attempt before considering it failed. (1-30).

`CheckAttempts` - (Optional) How many times to attempt a check before considering a backend to be down. (1-30).

`CheckPath` - (Optional) The URL path to check on each backend. If the backend does not respond to this request it is considered to be down.

`CheckPassive` - (Optional) If true, any response from this backend with a 5xx status code will be enough for it to be considered unhealthy and taken out of rotation.

`CipherSuite` - (Optional) What ciphers to use for SSL connections served by this NodeBalancer. `legacy` is considered insecure and should only be used if necessary.

`SslCert` - (Optional) The certificate this port is serving. This is not returned. If set, this field will come back as `<REDACTED>`. Please use the ssl_commonname and ssl_fingerprint to identify the certificate.

`SslKey` - (Optional) The private key corresponding to this port's certificate. This is not returned. If set, this field will come back as `<REDACTED>`. Please use the ssl_commonname and ssl_fingerprint to identify the certificate.


## See Also

* [linode_nodebalancer_config](https://www.terraform.io/docs/providers/linode/r/nodebalancer_config.html) in the _Terraform Provider Documentation_