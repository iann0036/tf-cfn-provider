# Terraform::Google::ComputeVpnTunnel

VPN tunnel resource.


To get more information about VpnTunnel, see:

* [API documentation](https://cloud.google.com/compute/docs/reference/rest/v1/vpnTunnels)
* How-to Guides
    * [Cloud VPN Overview](https://cloud.google.com/vpn/docs/concepts/overview)
    * [Networks and Tunnel Routing](https://cloud.google.com/vpn/docs/concepts/choosing-networks-routing)

~> **Warning:** All arguments including the shared secret will be stored in the raw
state as plain-text.
[Read more about sensitive data in state](/docs/state/sensitive-data.html).

<div class = "oics-button" style="float: right; margin: 0 0 -15px">
  <a href="https://console.cloud.google.com/cloudshell/open?cloudshell_git_repo=https%3A%2F%2Fgithub.com%2Fterraform-google-modules%2Fdocs-examples.git&cloudshell_working_dir=vpn_tunnel_basic&cloudshell_image=gcr.io%2Fgraphite-cloud-shell-images%2Fterraform%3Alatest&open_in_editor=main.tf&cloudshell_print=.%2Fmotd&cloudshell_tutorial=.%2Ftutorial.md" target="_blank">
    <img alt="Open in Cloud Shell" src="//gstatic.com/cloudssh/images/open-btn.svg" style="max-height: 44px; margin: 32px auto; max-width: 100%;">
  </a>
</div>

## Return Values

### Fn::GetAtt

Fn::GetAtt returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

`SelfLink` - The URI of the created resource.

## See Also

* [google_compute_vpn_tunnel](https://www.terraform.io/docs/providers/google/r/compute_vpn_tunnel.html) in the _Terraform Provider Documentation_