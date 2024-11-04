import json
import os

def export_to_json(rc, output_dir, file_name, action_list, action_show):
    """
    Export data to a JSON file.

    Args:
        rc (RemoteCKAN): The CKAN instance connection.
        output_dir (str): The directory where the JSON file will be saved.
        file_name (str): The name of the JSON file.
        action_list (str): The CKAN action to list items.
        action_show (str): The CKAN action to show item details.
    """
    item_list = getattr(rc.action, action_list)()
    items = []
    for item_id in item_list:
        item = getattr(rc.action, action_show)(id=item_id)
        items.append(item)
    file_path = os.path.join(output_dir, f"{file_name}.json")
    with open(file_path, 'w') as f:
        json.dump(items, f, indent=4)
    print(f"Data exported to {file_path}")

def export_groups_to_json(rc, output_dir):
    """
    Export all groups to a JSON file.

    Args:
        rc (RemoteCKAN): The CKAN instance connection.
        output_dir (str): The directory where the JSON file will be saved.
    """
    export_to_json(rc, output_dir, 'groups', 'group_list', 'group_show')

def export_organizations_to_json(rc, output_dir):
    """
    Export all organizations to a JSON file.

    Args:
        rc (RemoteCKAN): The CKAN instance connection.
        output_dir (str): The directory where the JSON file will be saved.
    """
    export_to_json(rc, output_dir, 'organizations', 'organization_list', 'organization_show')