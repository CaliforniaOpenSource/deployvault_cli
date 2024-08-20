
import sys
from .package_installer import install_package
from .account_config import get_email, save_email
from .auth import login_user
from .package_installer import install_package_flow
from .parser import parse_arguments

# Default repository URL


def configure_account(args):
    if args.email:
        save_email(args.email)
        print(f"Email updated to: {args.email}")
    else:
        current_email = get_email()
        if current_email:
            print(f"Current email: {current_email}")
        else:
            print("No email currently set.")
        print("To update the email, use: deployvault_cli -config --email <new email>")



def main():
    args = parse_arguments()

    if args.config:
        configure_account(args)
        return

    # Regular package installation mode
    if not args.password or not args.pkg:
        print("Error: --password and --pkg are required for package installation.")
        parse_arguments().print_help()
        sys.exit(1)

    # Use the default repo URL if not provided
    repo_url = args.repo_url

    # Use email from config file if not provided as argument
    email = args.email or get_email()
    if not email:
        print("Error: Email not provided and not found in configuration file")
        sys.exit(1)

    # Save email to configuration file
    save_email(email)

    token = login_user(email, args.password, repo_url)
    if not token:
        sys.exit(1)

    install_package_flow(args.pkg, repo_url, token)

if __name__ == "__main__":
    main()