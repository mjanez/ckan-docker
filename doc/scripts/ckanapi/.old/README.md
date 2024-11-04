# CKAN API Script

This script allows you to interact with a CKAN instance to perform various actions such as updating packages, exporting groups, and exporting organizations. The configuration for different CKAN instances and actions is specified in a YAML file.

## Prerequisites

- Python 3.x

## Setup

### Creating a Virtual Environment

1. Create a virtual environment:

```sh
python3 -m venv venv
```

2. Activate the virtual environment:

- On Linux and macOS:

```sh
source venv/bin/activate
```

- On Windows:

```sh
.\venv\Scripts\activate
```

### Installing Dependencies

Install the required libraries using pip:

```sh
pip install -r requirements.txt
```

## Configuration

The configuration for the CKAN instances and actions is specified in a YAML file located at `./input/sites.yml`. If this file does not exist, you can use the provided `sites.example.yml` as a template.

### Creating `sites.yml`

1. Copy the `sites.example.yml` file to `sites.yml`:

```sh
cp ./input/sites.example.yml ./input/sites.yml
```

2. Edit the `sites.yml` file to include your CKAN instance details and the actions you want to perform. Below is an example configuration:

```yaml
# ./input/sites.yml

default:
  ckan_site_url: 'https://demo.ckan.dcat-ap-3.es'
  api_token: 'your_api_token'
  actions:
    - update_packages
    - export_groups
    - export_organizations
  override:
    theme_es: "http://datos.gob.es/kos/sector-publico/sector/medio-ambiente"
  target_values:
    publisher_name:
      condition: "Sample Company"
      override:
        publisher_type: "http://purl.org/adms/publishertype/Company"

site_1:
  ckan_site_url: 'https://site1.ckan.instance'
  api_token: 'site1_api_token'
  actions:
    - update_packages
    - export_groups
    - export_organizations
  override:
    theme_es: "http://site1.theme.url"
  target_values:
    publisher_name:
      condition: "Site 1 Company"
      override:
        publisher_type: "http://site1.publisher.type"

site_2:
  ckan_site_url: 'https://site2.ckan.instance'
  api_token: null
  actions:
    - export_groups
    - export_organizations

site_3:
  ckan_site_url: 'https://site2.ckan.instance'
  api_token: 'site2_api_token'
  actions:
    - export_groups
    - export_organizations
    - create_organizations
    - create_groups
    - create_users
  organizations: './input/site_3/organizations.json'
  groups: './input/site_3/groups.json'
  users: './input/site_3/users.json'

```

## Usage

To run the script, use the following command:

```sh
python -m src -s <site>
```

Replace `<site>` with the site configuration you want to use (e.g., `default`, `site_1`, `site_2`).

### Example

To run the script using the `site_2` configuration:

```sh
python -m src -s site_2
```

### Command-line Arguments

- `-s` or `--site`: The site configuration to load (default: `default`).
- `-c` or `--config`: The path to the YAML configuration file (default: `./input/sites.yml`).

### Notes

- Actions that modify data (e.g., `update_packages`, `create`, `delete`) require a non-null `api_token`.
- If only `GET` actions are specified (e.g., `export_groups`, `export_organizations`), the `api_token`, `override`, and `target_values` are not required.

## Script Details

The script performs the following actions based on the configuration:

1. **Update Packages**: Updates the packages in the CKAN instance based on the specified overrides and target values.
2. **Export Groups**: Exports all groups from the CKAN instance to a JSON file (`groups.json`).
3. **Export Organizations**: Exports all organizations from the CKAN instance to a JSON file (`organizations.json`).

### Functions

#### Connect

- `connect_to_ckan(ckan_site_url, api_token)`: Connects to the CKAN instance.

#### Create

- `create_organizations(rc, json_path)`: Creates new organizations in CKAN from a JSON file.
- `create_groups(rc, json_path)`: Creates new groups in CKAN from a JSON file.
- `create_users(rc, json_path)`: Creates new users in CKAN from a JSON file.

#### Update

- `update_package(rc, package_id, theme_es, publisher_name, publisher_type)`: Updates a package given its ID.

#### Get

- `export_groups_to_json(rc, file_path)`: Exports all groups to a JSON file.
- `export_organizations_to_json(rc, file_path)`: Exports all organizations to a JSON file.


### Example Output

- `groups.json`: Contains detailed information about all groups.
- `organizations.json`: Contains detailed information about all organizations.

## License

This project is licensed under the MIT License.
