import yaml
import argparse
import os

default_sites_file = './input/sites.yml'
default_site = 'default'

class SampleConfig:
    """
    Configuration class for CKAN instance settings and overrides.

    Attributes:
        ckan_site_url (str): The URL of the CKAN instance.
        api_token (str): The API token for accessing the CKAN instance.
        actions (list): List of actions to perform.
        organizations (str): Path to the JSON file containing organization data.
        groups (str): Path to the JSON file containing group data.
        users (str): Path to the JSON file containing user data.
        override (dict): Dictionary of override values.
        delete (list): List of keys to delete.
        target_values (dict): Dictionary of target values.
    """
    def __init__(self, config):
        self.ckan_site_url = config['ckan_site_url']
        self.api_token = config.get('api_token')
        self.actions = config['actions']
        self.organizations = config.get('organizations')
        self.groups = config.get('groups')
        self.users = config.get('users')
        self.override = config.get('override', {})
        self.delete = config.get('delete', [])
        self.target_values = config.get('target_values', {})
        target_site_config = config.get('target_site', {})
        self.target_ckan_site_url = target_site_config.get('ckan_site_url')
        self.target_api_token = target_site_config.get('api_token')
        self.target_organization_id = target_site_config.get('target_organization_id')
        self.delete_all_before_copy = target_site_config.get('delete_all_before_copy', False)  # Nueva opción


def load_config(config_file, site='default'):
    """
    Load the configuration from a YAML file.

    Args:
        config_file (str): The path to the YAML configuration file.
        site (str): The site configuration to load.

    Returns:
        SampleConfig: The loaded configuration object.
    """
    if not os.path.exists(config_file):
        example_file = config_file.replace('sites.yml', 'sites.example.yml')
        if os.path.exists(example_file):
            print(f"Warning: {config_file} not found. Please use {example_file} as a template to create your own {config_file} before running the script.")
        else:
            print(f"Error: {config_file} not found and no example file {example_file} available.")
        exit(1)

    with open(config_file, 'r') as file:
        config_data = yaml.safe_load(file)
        return SampleConfig(config_data[site])

def parse_args():
    """
    Parse command-line arguments.

    Returns:
        argparse.Namespace: The parsed arguments.
    """
    parser = argparse.ArgumentParser(description='Load CKAN configuration.')
    parser.add_argument('-s', '--site', type=str, default=default_site, help='The site configuration to load')
    parser.add_argument('-c', '--config', type=str, default=default_sites_file, help='The path to the YAML configuration file')
    return parser.parse_args()

if __name__ == "__main__":
    args = parse_args()
    config = load_config(args.config, site=args.site)
    print(f"Loaded configuration for site: {args.site}")
    print(f"CKAN Site URL: {config.ckan_site_url}")
    print(f"Actions: {config.actions}")
    if config.override:
        print(f"Override: {config.override}")
    #FIXME: Not working, duplicate datasets.
    # if config.delete:
    #     print(f"Delete fields: {config.delete}")
    if config.target_values:
        print(f"Target Values: {config.target_values}")
    if config.organizations:
        print(f"Organizations JSON Path: {config.organizations}")
    if config.groups:
        print(f"Groups JSON Path: {config.groups}")
    if config.users:
        print(f"Users JSON Path: {config.users}")