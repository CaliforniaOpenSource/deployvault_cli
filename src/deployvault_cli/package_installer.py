import subprocess
from .proxy_server import ProxyServer
from .auth import login_user

def install_package_flow(pkg, repo_url, token):
    proxy_server = ProxyServer()
    proxy_server.start(token, repo_url)

    try:
        install_package(pkg, proxy_server.url)
    finally:
        proxy_server.stop()

def install_package(package_name, proxy_url):
    try:
        print("install package url: ",f"{proxy_url}/{package_name}")
        subprocess.run(["pip", "install", "--no-index", "--find-links", f"{proxy_url}/{package_name}", package_name], check=True)
        print(f"Successfully installed {package_name}")
    except subprocess.CalledProcessError as e:
        print(f"Failed to install {package_name}. Error: {e}")