from .get import export_groups_to_json, export_organizations_to_json
from .update import update_package
from .create import create_organizations, create_groups, create_users
# Import other actions as needed

def list_actions():
    """
    List all available actions in the logic module.

    Returns:
        dict: A dictionary of action names and their corresponding functions.
    """
    actions = {
        'export_groups': export_groups_to_json,
        'export_organizations': export_organizations_to_json,
        'update_packages': update_package,
        'create_organizations': create_organizations,
        'create_groups': create_groups,
        'create_users': create_users,
        # Add other actions here
    }
    return actions

def execute_action(action_name, rc, config, output_dir):
    """
    Execute a specific action based on the action name.

    Args:
        action_name (str): The name of the action to execute.
        rc (RemoteCKAN): The CKAN instance connection.
        config (SampleConfig): The configuration object.
        output_dir (str): The output directory path.
    """
    actions = list_actions()
    if action_name in actions:
        if action_name == 'update_packages':
            # Get the list of all packages
            package_list = rc.action.package_list()

            # Iterate over each package and update it
            for package_id in package_list:
                actions[action_name](rc, package_id, config.override, config.target_values)
        elif action_name == 'create_organizations':
            actions[action_name](rc, config.organizations)
        elif action_name == 'create_groups':
            actions[action_name](rc, config.groups)
        elif action_name == 'create_users':
            actions[action_name](rc, config.users)
        else:
            actions[action_name](rc, output_dir)