import argparse

DEFAULT_REPO_URL = "https://deployvault0-2a449bf8dc4e.herokuapp.com"

def parse_arguments():
    parser = argparse.ArgumentParser(description="DeployVault CLI for package installation and account configuration")

    parser.add_argument("-config", action="store_true", help="Enter configuration mode")
 
 
    parser.add_argument("--email", help="User email for login or configuration")
    parser.add_argument("--password", help="Password for login")
    parser.add_argument("--pkg", help="Package name to install")
    parser.add_argument("--repo-url", default=DEFAULT_REPO_URL, 
                        help=f"Base URL of the private repository (default: {DEFAULT_REPO_URL})")
    return parser.parse_args()