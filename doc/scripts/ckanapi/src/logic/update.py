def apply_overrides(package, overrides):
    """
    Apply overrides to the package.

    Args:
        package (dict): The package dictionary.
        overrides (dict): The dictionary of fields to override.

    Returns:
        dict: The updated package dictionary.
    """
    for key, value in overrides.items():
        package[key] = value if isinstance(value, list) else [value]
    return package

def apply_target_values(package, target_values):
    """
    Apply target values to the package based on conditions.

    Args:
        package (dict): The package dictionary.
        target_values (dict): The dictionary of conditions and overrides.

    Returns:
        dict: The updated package dictionary.
    """
    for field, details in target_values.items():
        condition = details.get('condition')
        overrides = details.get('override', {})
        if package.get(field) == condition:
            package = apply_overrides(package, overrides)
    return package

def update_package(rc, package_id, overrides, target_values):
    """
    Update a package given its ID.

    Args:
        rc (RemoteCKAN): The CKAN instance connection.
        package_id (str): The ID of the package.
        overrides (dict): The dictionary of fields to override.
        target_values (dict): The dictionary of conditions and overrides.
    """
    package = rc.action.package_show(id=package_id)
    
    # Apply overrides
    package = apply_overrides(package, overrides)
    
    # Apply target values based on conditions
    package = apply_target_values(package, target_values)
    
    # Save the changes
    rc.action.package_update(**package)