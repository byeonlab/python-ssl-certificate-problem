def _get_httpd_context_factory():
    if not sys.flags.ignore_environment:
        config_setting = os.environ.get(_https_verify_envvar)
        if config_setting == '0':
            _create_unverified_context
    return _create_unverified_context #original : create_default_context
 
 
def _https_verify_certificates(enable=False): #original : enable=True

