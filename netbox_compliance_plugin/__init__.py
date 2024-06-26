"""Top-level package for NetBox Compliance Plugin."""

__author__ = """Adam Angell"""
__email__ = ""
__version__ = "0.1.0"


from netbox.plugins import PluginConfig


class ComplianceConfig(PluginConfig):
    name = "netbox_compliance_plugin"
    verbose_name = "NetBox Compliance Plugin"
    description = "NetBox plugin for Compliance."
    version = "version"
    base_url = "netbox_compliance_plugin"


config = ComplianceConfig
