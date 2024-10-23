from .quick_ckanapi import main
from .config import parse_args, load_config

if __name__ == "__main__":
    args = parse_args()
    config = load_config(args.config, site=args.site)
    config.site = args.site  # Add the site name to the config object
    main(config)