servers = [
    {
        "hostname": "example-server",
        "ip": "192.168.1.10",
        "os": "Ubuntu",
        "role": "Web Server",
        "services": ["Apache", "SSH"]
    },
]

def add_server():
    server_name = input("Enter server name: ")
    server_ip = input("Enter server IP: ")
    server_os = input("Enter server OS: ")
    server_role = input("Enter server role: ")
    server_services = input("Enter server services (comma separated): ").split(",")
    server = {
        "hostname": server_name,
        "ip": server_ip,
        "os": server_os,
        "role": server_role,
        "services": [service.strip() for service in server_services]
    }
    servers.append(server)
    print("Server added successfully!")
    writter()
    
def show_servers():
    if not servers:
        print("No servers in inventory.")
        return
    for server in servers:
        print("-" * 30)
        print(f"Hostname: {server['hostname']}")
        print(f"IP: {server['ip']}")
        print(f"OS: {server['os']}")
        print(f"Role: {server['role']}")
        print(f"Services: {', '.join(server['services'])}")
        print("-" * 30)

def search_server():
    search_term = input("Enter hostname or IP to search: ")
    found_servers = [
        server for server in servers
        if server['hostname'] == search_term or server['ip'] == search_term
    ]

    if not found_servers:
        print("No servers found.")
        return
    for server in found_servers:
        print("-" * 30)
        print(f"Hostname: {server['hostname']}")
        print(f"IP: {server['ip']}")
        print(f"OS: {server['os']}")
        print(f"Role: {server['role']}")
        print(f"Services: {', '.join(server['services'])}")
        print("-" * 30)

def update_server():
    search_term = input("Enter hostname or IP of the server to update: ")
    found_servers = [server for server in servers if server['hostname'] == search_term or server['ip'] == search_term]
    if not found_servers:
        print("Server not found.")
        return
    server = found_servers[0]
    print(f"Updating server: {server['hostname']}")
    new_hostname = input(f"Enter new hostname (current: {server['hostname']}): ") or server['hostname']
    new_ip = input(f"Enter new IP (current: {server['ip']}): ") or server['ip']
    new_os = input(f"Enter new OS (current: {server['os']}): ") or server['os']
    new_role = input(f"Enter new role (current: {server['role']}): ") or server['role']
    new_services = input(f"Enter new services (comma separated, current: {', '.join(server['services'])}): ").split(",") or server['services']
    servers[servers.index(server)] = {
        "hostname": new_hostname,
        "ip": new_ip,
        "os": new_os,
        "role": new_role,
        "services": [service.strip() for service in new_services]
    }
    print("Server updated successfully!")
    writter()

def delete_server():
    search_term = input("Enter hostname or IP of the server to delete: ")
    found_servers = [server for server in servers if server['hostname'] == search_term or server['ip'] == search_term]
    if not found_servers:
        print("Server not found.")
        return
    server = found_servers[0]
    servers.remove(server)
    print("Server deleted successfully!")
    writter()

def writter():
    with open("servers.txt", "w") as f:
        for server in servers:
            f.write(f"{server['hostname']},{server['ip']},{server['os']},{server['role']},{','.join(server['services'])}\n")
        

def menu():
    while True:
        print("\nServer Inventory Management")
        print("1. Add Server")
        print("2. Show Servers")
        print("3. Search Server")
        print("4. Update Server")
        print("5. Delete Server")
        print("6. Exit")
        choice = input("Enter your choice: ")
        if choice == '1':
            add_server()
        elif choice == '2':
            show_servers()
        elif choice == '3':
            search_server()
        elif choice == '4':
            update_server()
        elif choice == '5':
            delete_server()
        elif choice == '6':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    menu()