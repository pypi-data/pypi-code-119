
try:
    from importlib.resources import files
except ImportError:
    from importlib_resources import files
    
schema = files('argus_api.schema.componentadmin').joinpath('componentadmin.json')
        