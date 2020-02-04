# Ilo Amplifier Integration Pack
This pack allows you to integrate with iLO Amplifier

## Configuration
Copy the example configuration in [iloamplifier].yaml.example](./iloamplifier.yaml.example) to
`/opt/stackstorm/configs/iloamplifier.yaml` and edit as required.

It must contain:

```
ipaddress - Your iloAmp appliance IP address
username - iloAmp User name
password - iloAmp Password
```

You can also use dynamic values from the datastore. See the
[docs](https://docs.stackstorm.com/reference/pack_configs.html) for more info.

Example configuration:

```yaml
---
  login_host: "10.10.10.10"
  login_account: "Administrator"
  login_password: "password"
```
You can also run `st2 pack config iloamplifier` and answer the promts

**Note** : When modifying the configuration in `/opt/stackstorm/configs/` please
           remember to tell StackStorm to load these new values by running
           `st2ctl reload --register-configs`


## Actions

Actions are defined in two groups:

### Individual actions: GET, POST, PUT with under bar will precede each individual action
* ``get_systems``
* ``get_chassis``
* ``get_ethernetinterfaces``


### Orquestra Workflows: will not
