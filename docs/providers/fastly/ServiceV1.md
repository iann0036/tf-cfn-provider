# Terraform::Fastly::ServiceV1

Provides a Fastly Service, representing the configuration for a website, app,
API, or anything else to be served through Fastly. A Service encompasses Domains
and Backends.

The Service resource requires a domain name that is correctly set up to direct
traffic to the Fastly service. See Fastly's guide on [Adding CNAME Records][fastly-cname]
on their documentation site for guidance.

## Properties

`Backend` - (Optional) A set of Backends to service requests from your Domains. Defined below. Backends must be defined in this argument, or defined in the `Vcl` argument below.

`Condition` - (Optional) A set of conditions to add logic to any basic configuration object in this service. Defined below.

`CacheSetting` - (Optional) A set of Cache Settings, allowing you to override.

`Director` - (Optional) A director to allow more control over balancing traffic over backends. when an item is not to be cached based on an above `Condition`. Defined below.

`Gzip` - (Required) A set of gzip rules to control automatic gzipping of content. Defined below.

`Header` - (Optional) A set of Headers to manipulate for each request. Defined below.

`DefaultTtl` - (Optional) The default Time-to-live (TTL) for requests.

`ForceDestroy` - (Optional) Services that are active cannot be destroyed. In order to destroy the Service, set `ForceDestroy` to `true`. Default `false`.

`RequestSetting` - (Optional) A set of Request modifiers. Defined below.

`S3logging` - (Optional) A set of S3 Buckets to send streaming logs too. Defined below.

`Papertrail` - (Optional) A Papertrail endpoint to send streaming logs too. Defined below.

`Sumologic` - (Optional) A Sumologic endpoint to send streaming logs too. Defined below.

`Gcslogging` - (Optional) A gcs endpoint to send streaming logs too. Defined below.

`Bigquerylogging` - (Optional) A BigQuery endpoint to send streaming logs too. Defined below.

`Syslog` - (Optional) A syslog endpoint to send streaming logs too. Defined below.

`Logentries` - (Optional) A logentries endpoint to send streaming logs too. Defined below.

`ResponseObject` - (Optional) Allows you to create synthetic responses that exist entirely on the varnish machine. Useful for creating error or maintenance pages that exists outside the scope of your datacenter. Best when used with Condition objects.

`Snippet` - (Optional) A set of custom, "regular" (non-dynamic) VCL Snippet configuration blocks.  Defined below.

`Vcl` - (Optional) A set of custom VCL configuration blocks. The ability to upload custom VCL code is not enabled by default for new Fastly accounts (see the [Fastly documentation](https://docs.fastly.com/guides/vcl/uploading-custom-vcl) for details).

### CacheSetting Properties

`StaleTtl` - (Optional) Max "Time To Live" for stale (unreachable) objects.

`Ttl` - (Optional) The Time-To-Live (TTL) for the object.

### Bigquerylogging Properties

`Email` - (Optional) The email for the service account with write access to your BigQuery dataset. If not provided, this will be pulled from a `FASTLY_BQ_EMAIL` environment variable.

`SecretKey` - (Optional) The secret key associated with the sservice account that has write access to your BigQuery table. If not provided, this will be pulled from the `FASTLY_BQ_SECRET_KEY` environment variable. Typical format for this is a private key in a string with newlines.

`ProjectId` - (Required) The ID of your GCP project.

`Dataset` - (Required) The ID of your BigQuery dataset.

`Table` - (Required) The ID of your BigQuery table.

`Template` - (Optional) Big query table name suffix template. If set will be interpreted as a strftime compatible string and used as the [Template Suffix for your table](https://cloud.google.com/bigquery/streaming-data-into-bigquery#template-tables).

### Snippet Properties

`Type` - (Required) The location in generated VCL where the snippet should be placed (can be one of `init`, `recv`, `hit`, `miss`, `pass`, `fetch`, `error`, `deliver`, `log` or `none`).

`Priority` - (Optional) Priority determines the ordering for multiple snippets. Lower numbers execute first.  Defaults to `100`.

### Vcl Properties

`Name` - (Required) A unique name for this configuration block.

`Content` - (Required) The custom VCL code to upload.

`Main` - (Optional) If `true`, use this block as the main configuration. If `false`, use this block as an includable library. Only a single VCL block can be marked as the main block. Default is `false`.

### Gzip Properties

`ContentTypes` - (Optional) The content-type for each type of content you wish to have dynamically gzip'ed. Example: `["text/html", "text/css"]`.

`Extensions` - (Optional) File extensions for each file type to dynamically gzip. Example: `["css", "js"]`.

`Destination` - (Required) The name of the header that is going to be affected by the Action.

`IgnoreIfSet` - (Optional) Do not add the header if it is already present. (Only applies to the `set` action.). Default `false`.

`Source` - (Optional) Variable to be used as a source for the header content. (Does not apply to the `delete` action.).

`Regex` - (Optional) Regular expression to use (Only applies to the `Regex` and `regex_repeat` actions.).

`Substitution` - (Optional) Value to substitute in place of regular expression. (Only applies to the `Regex` and `regex_repeat` actions.).

### Syslog Properties

`Address` - (Required) A hostname or IPv4 address of the Syslog endpoint.

`MessageType` - (Optional) How the message should be formatted; one of: `classic`, `loggly`, `logplex` or `blank`.  Default `classic`.

`TlsHostname` - (Optional) Used during the TLS handshake to validate the certificate.

`TlsCaCert` - (Optional) A secure certificate to authenticate the server with.

### Sumologic Properties

`Url` - (Required) The URL to Sumologic collector endpoint.

### Backend Properties

`Healthcheck` - (Optional) Name of a defined `Healthcheck` to assign to this backend.

`AutoLoadbalance` - (Optional, boolean) Denotes if this Backend should be included in the pool of backends that requests are load balanced against. Default `true`.

`BetweenBytesTimeout` - (Optional) How long to wait between bytes in milliseconds. Default `10000`.

`ConnectTimeout` - (Optional) How long to wait for a timeout in milliseconds. Default `1000`.

`ErrorThreshold` - (Optional) Number of errors to allow before the Backend is marked as down. Default `0`.

`FirstByteTimeout` - (Optional) How long to wait for the first bytes in milliseconds. Default `15000`.

`MaxConn` - (Optional) Maximum number of connections for this Backend. Default `200`.

`UseSsl` - (Optional) Whether or not to use SSL to reach the backend. Default `false`.

`MaxTlsVersion` - (Optional) Maximum allowed TLS version on SSL connections to this backend.

`MinTlsVersion` - (Optional) Minimum allowed TLS version on SSL connections to this backend.

`SslCiphers` - (Optional) Comma separated list of OpenSSL Ciphers to try when negotiating to the backend.

`SslCaCert` - (Optional) CA certificate attached to origin.

`SslClientCert` - (Optional) Client certificate attached to origin. Used when connecting to the backend.

`SslClientKey` - (Optional) Client key attached to origin. Used when connecting to the backend.

`SslCheckCert` - (Optional) Be strict about checking SSL certs. Default `true`.

`SslHostname` - (Optional, deprecated by Fastly) Used for both SNI during the TLS handshake and to validate the cert.

`SslCertHostname` - (Optional) Overrides ssl_hostname, but only for cert verification. Does not affect SNI at all.

`SslSniHostname` - (Optional) Overrides ssl_hostname, but only for SNI in the handshake. Does not affect cert validation at all.

`Weight` - (Optional) The [portion of traffic](https://docs.fastly.com/guides/performance-tuning/load-balancing-configuration.html#how-weight-affects-load-balancing) to send to this Backend. Each Backend receives `weight / total` of the traffic. Default `100`.

`Statement` - (Required) The statement used to determine if the condition is met.

### Condition Properties

`DefaultHost` - (Optional) Sets the host header.

`Action` - (Optional) Allows you to terminate request handling and immediately perform an action. When set it can be `lookup` or `pass` (Ignore the cache completely).

`MaxStaleAge` - (Optional) How old an object is allowed to be to serve `stale-if-error` or `stale-while-revalidate`, in seconds.

`ForceMiss` - (Optional) Force a cache miss for the request. If specified, can be `true` or `false`.

`ForceSsl` - (Optional) Forces the request to use SSL (Redirects a non-SSL request to SSL).

`BypassBusyWait` - (Optional) Disable collapsed forwarding, so you don't wait for other objects to origin.

`HashKeys` - (Optional) Comma separated list of varnish request object fields that should be in the hash key.

`Xff` - (Optional) X-Forwarded-For, should be `clear`, `leave`, `append`, `append_all`, or `overwrite`. Default `append`.

`TimerSupport` - (Optional) Injects the X-Timer info into the request for viewing origin fetch durations.

`GeoHeaders` - (Optional) Injects Fastly-Geo-Country, Fastly-Geo-City, and Fastly-Geo-Region into the request headers.

### ResponseObject Properties

`RequestCondition` - (Optional) Name of already defined `Condition` to be checked during the request phase. If the condition passes then this object will be delivered. This `Condition` must be of type `REQUEST`.

`CacheCondition` - (Optional) Name of already defined `Condition` to check after we have retrieved an object. If the condition passes then deliver this Request Object instead. This `Condition` must be of type `CACHE`. For detailed information about Conditionals, see [Fastly's Documentation on Conditionals][fastly-conditionals].

`Status` - (Optional) The HTTP Status Code. Default `200`.

`Response` - (Optional) The HTTP Response. Default `Ok`.

`ContentType` - (Optional) The MIME type of the content.

### Healthcheck Properties

`Host` - (Required) The Host header to send for this Healthcheck.

`CheckInterval` - (Optional) How often to run the Healthcheck in milliseconds. Default `5000`.

`ExpectedResponse` - (Optional) The status code expected from the host. Default `200`.

`HttpVersion` - (Optional) Whether to use version 1.0 or 1.1 HTTP. Default `1.1`.

`Initial` - (Optional) When loading a config, the initial number of probes to be seen as OK. Default `2`.

`Method` - (Optional) Which HTTP method to use. Default `HEAD`.

`Threshold` - (Optional) How many Healthchecks must succeed to be considered healthy. Default `3`.

`Timeout` - (Optional) Timeout in milliseconds. Default `500`.

`Window` - (Optional) The number of most recent Healthcheck queries to keep for this Healthcheck. Default `5`.

### Director Properties

`Comment` - (Optional) An optional comment about the Director.

`Shield` - (Optional) Selected POP to serve as a "shield" for origin servers.

`Backends` - (Required) Names of defined backends to map the director to. Example: `[ "origin1", "origin2" ]`.

`Capacity` - (Optional) Load balancing weight for the backends. Default `100`.

`Quorum` - (Optional) Percentage of capacity that needs to be up for the director itself to be considered up. Default `75`.

`Retries` - (Optional) How many backends to search if it fails. Default `5`.

### Gcslogging Properties

`Path` - (Optional) Path to store the files. Must end with a trailing slash. If this field is left empty, the files will be saved in the bucket's root path.

`BucketName` - (Required) The name of the bucket in which to store the logs.

`Period` - (Optional) How frequently the logs should be transferred, in seconds. Default `3600`.

`GzipLevel` - (Optional) Level of GZIP compression, from `0-9`. `0` is no compression. `1` is fastest and least compressed, `9` is slowest and most compressed. Default `0`.

### Logentries Properties

`Port` - (Optional) The port number configured in Logentries to send logs to. Defaults to `20000`.

`ResponseCondition` - (Optional) Name of already defined `Condition` to apply. This `Condition` must be of type `RESPONSE`. For detailed information about Conditionals, see [Fastly's Documentation on Conditionals][fastly-conditionals].

`Format` - (Optional) Apache-style string or VCL variables to use for log formatting. Defaults to Apache Common Log format (`%h %l %u %t %r %>s`).

`FormatVersion` - (Optional) The version of the custom logging format used for the configured endpoint. Can be either 1 (the default, version 1 log format) or 2 (the version 2 log format).

`Placement` - (Optional) Where in the generated VCL the logging call should be placed; one of: `none` or `waf_debug`.

`Token` - (Required) Logentries Token to be used for authentication (https://logentries.com/doc/input-token/).

`UseTls` - (Optional) Whether to use TLS for secure logging. Defaults to `true`.

### S3logging Properties

`Domain` - (Optional) If you created the S3 bucket outside of `us-east-1`, then specify the corresponding bucket endpoint. Example: `s3-us-west-2.amazonaws.com`.

`S3AccessKey` - (Required) AWS Access Key of an account with the required permissions to post logs. It is **strongly** recommended you create a separate IAM user with permissions to only operate on this Bucket. This key will be not be encrypted. You can provide this key via an environment variable, `FASTLY_S3_ACCESS_KEY`.

`S3SecretKey` - (Required) AWS Secret Key of an account with the required permissions to post logs. It is **strongly** recommended you create a separate IAM user with permissions to only operate on this Bucket. This secret will be not be encrypted. You can provide this secret via an environment variable, `FASTLY_S3_SECRET_KEY`.

`TimestampFormat` - (Optional) `strftime` specified timestamp formatting (default `%Y-%m-%dT%H:%M:%S.000`).

`Redundancy` - (Optional) The S3 redundancy level. Should be formatted; one of: `standard`, `reduced_redundancy` or null. Default `null`.


## Return Values

### Fn::GetAtt

`Id` - The ID of the Service.

`ActiveVersion` - The currently active version of your Fastly.

`Director` - Set of Directors. See above for details.

`ResponseObject` - Set of Response Object configurations. See above for details.

`DefaultTtl` - Default TTL.

`ForceDestroy` - Force the destruction of the Service on delete.

## See Also

* [fastly_service_v1](https://www.terraform.io/docs/providers/fastly/r/service_v1.html) in the _Terraform Provider Documentation_