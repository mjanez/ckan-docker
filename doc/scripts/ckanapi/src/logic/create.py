import json
import os

def load_json(file_path):
    """
    Load JSON data from a file.

    Args:
        file_path (str): The path to the JSON file.

    Returns:
        list: The JSON data loaded from the file.
    """
    with open(file_path, 'r') as f:
        return json.load(f)

def create_organizations(rc, json_path):
    """
    Create new organizations in CKAN.

    Args:
        rc (RemoteCKAN): The CKAN instance connection.
        json_path (str): The path to the JSON file containing organization data.
    """
    organizations = load_json(json_path)
    for org in organizations:
        try:
            rc.action.organization_create(**org)
            print(f"Organization '{org['name']}' created successfully.")
        except Exception as e:
            print(f"Failed to create organization '{org['name']}': {e}")

def create_groups(rc, json_path):
    """
    Create new groups in CKAN.

    Args:
        rc (RemoteCKAN): The CKAN instance connection.
        json_path (str): The path to the JSON file containing group data.
    """
    groups = load_json(json_path)
    for group in groups:
        try:
            rc.action.group_create(**group)
            print(f"Group '{group['name']}' created successfully.")
        except Exception as e:
            print(f"Failed to create group '{group['name']}': {e}")

def create_users(rc, json_path):
    """
    Create new users in CKAN.

    Args:
        rc (RemoteCKAN): The CKAN instance connection.
        json_path (str): The path to the JSON file containing user data.
    """
    users = load_json(json_path)
    for user in users:
        try:
            rc.action.user_create(**user)
            print(f"User '{user['name']}' created successfully.")
        except Exception as e:
            print(f"Failed to create user '{user['name']}': {e}")