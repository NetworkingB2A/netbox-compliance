from netbox.plugins import PluginMenuButton, PluginMenuItem

plugin_buttons = [
    PluginMenuButton(
        link="plugins:netbox_compliance_plugin:compliance_add",
        title="Add",
        icon_class="mdi mdi-plus-thick",
    )
]

menu_items = (
    PluginMenuItem(
        link="plugins:netbox_compliance_plugin:compliance_list",
        link_text="Compliance",
        buttons=plugin_buttons,
    ),
)
