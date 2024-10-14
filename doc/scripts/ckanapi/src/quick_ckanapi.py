import os
from ckanapi import RemoteCKAN
from .config import load_config, parse_args
from .logic import execute_action, list_actions

def connect_to_ckan(ckan_site_url, api_token):
    """
    Connect to the CKAN instance.

    Args:
        ckan_site_url (str): The URL of the CKAN instance.
        api_token (str): The API token for accessing the CKAN instance.

    Returns:
        RemoteCKAN: The CKAN instance connection.
    """
    return RemoteCKAN(ckan_site_url, apikey=api_token)

def is_modifying_action(action_name):
    """
    Determine if an action modifies data based on its name.

    Args:
        action_name (str): The name of the action.

    Returns:
        bool: True if the action modifies data, False otherwise.
    """
    modifying_prefixes = ('update_', 'create_', 'delete_')
    return action_name.startswith(modifying_prefixes)

def main(config):
    """
    Main function to update all packages and export groups and organizations.

    Args:
        config (SampleConfig): The configuration object.
    """
    # Connect to the CKAN instance
    rc = connect_to_ckan(config.ckan_site_url, config.api_token)

    # Create output directories if they don't exist
    output_dir = os.path.join('output', config.site)
    os.makedirs(output_dir, exist_ok=True)

    # Check if there are any actions that modify data
    if any(is_modifying_action(action) for action in config.actions):
        if not config.api_token:
            print("Error: API token is required for modifying actions.")
            return

    # Execute actions based on the configuration
    for action in config.actions:
        execute_action(action, rc, config, output_dir)

    print("Actions completed.")

if __name__ == "__main__":
    args = parse_args()
    config = load_config(args.config, site=args.site)
    config.site = args.site  # Add the site name to the config object
    main(config)