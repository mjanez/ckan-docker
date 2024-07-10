# Development SRC folder
This folder is used to clone CKAN extensions in development mode.

>**Warning**
> Save the extension code in this folder before updating/deleting the repo, all contents (`src/*)` are in `.gitignore` file.

## Clone repos with bash
Update `repos` with your requirements:
```bash
#!/bin/bash

# Check if the script is running from the src directory
current_dir=$(basename "$(pwd)")
if [ "$current_dir" != "src" ]; then
    echo "This script must be run from the src directory. Please move the script to the src directory and try again."
    exit 1
fi

# Define repositories and tags
declare -A repos=(
    ["ckan/ckanext-xloader"]="1.0.1"
    ["ckan/ckanext-harvest"]="v1.5.6"
    ["ckan/ckanext-geoview"]="v0.1.0"
    ["ckan/ckanext-spatial"]="v2.1.1"
    ["mjanez/ckanext-dcat"]="v1.8.0-alpha"
    ["ckan/ckanext-scheming"]="release-3.0.0"
    ["mjanez/ckanext-resourcedictionary"]="v1.0.1"
    ["ckan/ckanext-pages"]="v0.5.2"
    ["ckan/ckanext-pdfview"]="0.0.8"
    ["mjanez/ckanext-fluent"]="v1.0.1"
    ["mjanez/ckanext-schemingdcat"]="develop"
    ["mjanez/ckanext-mqa"]="develop"
)

# Detect if the script is running on Windows
if [[ "$OSTYPE" == "msys" || "$OSTYPE" == "cygwin" || "$OSTYPE" == "win32" ]]; then
    echo "It seems you are on Windows. Do you want to configure 'core.autocrlf=input' for the cloned repositories? (y/n)"
    read -r response
    if [[ "$response" =~ ^[Yy]$ ]]; then
        config_autocrlf="--config core.autocrlf=input"
    else
        config_autocrlf=""
    fi
else
    config_autocrlf=""
fi

# The script assumes it is running from the src directory, so clone_path is set to "."
clone_path="."

# Clone each repository at its specific tag
for repo in "${!repos[@]}"; do
    tag="${repos[$repo]}"
    repo_name=$(basename "$repo")
    echo "Cloning $repo at tag $tag into $clone_path..."
    if git clone $config_autocrlf --branch "$tag" "https://github.com/$repo.git" "$clone_path/$repo_name"; then
        # Check for replacement .txt files in ../ckan/req_fixes/<repo_name>
        req_fix_path="../ckan/req_fixes/${repo_name}"
        if [ -d "$req_fix_path" ]; then
            echo "Replacing .txt files for $repo_name..."
            # Find and replace all .txt files from req_fix_path to the cloned repo directory
            find "$req_fix_path" -name "*.txt" -exec bash -c 'f="{}"; cp "$f" "'"$clone_path/${repo_name}"'/${f##*/}"' \;
        fi
    else
        echo "Error cloning $repo."
    fi
done
```