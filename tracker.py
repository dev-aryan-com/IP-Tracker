import requests
import time

# Function to fetch IP details using ipinfo.io
def track_ip(ip_address):
    url = f"https://ipinfo.io/{ip_address}/json"

    try:
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            print("IP Address Details:")
            print(f"IP: {data.get('ip')}")
            print(f"Hostname: {data.get('hostname')}")
            print(f"City: {data.get('city')}")
            print(f"Region: {data.get('region')}")
            print(f"Country: {data.get('country')}")
            print(f"Location (lat,long): {data.get('loc')}")
            print(f"Organization: {data.get('org')}")
            print(f"Timezone: {data.get('timezone')}")
            print()
        else:
            print("Error fetching details. Check the IP address or try again later.")
            print()
    except Exception as e:
        print(f"An error occurred: {e}")
        print()

# Function to get the user's own IP
def get_self_ip():
    try:
        response = requests.get("https://ipinfo.io/json")
        if response.status_code == 200:
            return response.json().get('ip')
        else:
            print("Error fetching your IP address.")
            return None
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

if __name__ == "__main__":
    while True:
        print("IP Tracker v1.0")
        print()
        print("Enter [S] to track your own IP")
        print("Enter an IP address to track")
        print("Enter [X] to exit")
        print()
        choice = input("Enter your choice : ").strip().lower()
        print()
		
        if choice == "s":
            print("Fetching your IP details...")
            print()
            self_ip = get_self_ip()
            if self_ip:
                track_ip(self_ip)
                time.sleep(0.5)
        elif choice == "x":
            print("Thanks for using!")
            break
        else:
            print(f"Fetching details for IP address: {choice}")
            print()
            track_ip(choice)
            time.sleep(0.5)