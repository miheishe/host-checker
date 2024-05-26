import requests
import time
import os

def read_hosts(file_path):
    with open(file_path, 'r') as file:
        return [line.strip() for line in file.readlines()]

def check_host(host):
    protocols = ['http', 'https']
    results = []
    for protocol in protocols:
        url = f"{protocol}://{host}"
        try:
            response = requests.get(url, timeout=5)
            results.append((url, response.status_code))
        except requests.RequestException as e:
            results.append((url, str(e)))
    return results

def main():
    hosts_file = os.getenv('HOSTS_FILE', 'hosts.txt')
    while True:
        hosts = read_hosts(hosts_file)
        for host in hosts:
            results = check_host(host)
            for url, status in results:
                print(f"{url}: {status}")
        time.sleep(60)  # Wait for a minute before the next check cycle

if __name__ == "__main__":
    main()
