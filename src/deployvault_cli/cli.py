import argparse
import sys
from .auth import login_user
from .proxy_server import ProxyServer
from .package_installer import install_package

def main():
    parser = argparse.ArgumentParser(description="Install packages from private PyPI repository")
    parser.add_argument("--email", required=True, help="User email for login")
    parser.add_argument("--password", required=True, help="Password for login")
    parser.add_argument("--pkg", required=True, help="Package name to install")
    parser.add_argument("--repo-url", required=True, help="Base URL of the private repository")
    args = parser.parse_args()

    token = login_user(args.email, args.password, args.repo_url)
    if not token:
        sys.exit(1)

    proxy_server = ProxyServer()
    proxy_server.start(token,args.repo_url)

    try:
        install_package(args.pkg, proxy_server.url)
    finally:
        proxy_server.stop()

if __name__ == "__main__":
    main()