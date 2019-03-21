### we prepend t_ to tablenames and f_ to fieldnames for disambiguity

########################################
db.define_table('t_mgmt_server',
                Field('name', type='string',
                      label=T('Management server Name')),
                Field('last_ip', type='string',
                      label=T('Last IP')),
                Field('ver', type='string',
                      label=T('MGMT Server version')),
                Field('is_enabled', type='boolean',
                      label=T('Is enabled ?')),
                auth.signature, format='%(name)s',
                migrate=settings.migrate)
########################################
########################################
db.define_table('t_CHKP_ver',
                Field('name', type='string',
                      label=T('Version Name')),
                Field('mgmt_api_ver', type='string',
                      label=T('MGMT Api version')),
                auth.signature, format='%(name)s',
                migrate=settings.migrate)
########################################