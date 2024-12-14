# IP Tracker - v1.0

A simple Python-based IP tracker display details for a specific IP address or your own IP address.


## 📖 Introduction

The **IP Tracker** is a Python script that allows you to:

*   Fetch details of any valid public IP address.
*   Get information such as city, region, country, latitude/longitude, ISP, and timezone.
*   Track your own IP address with just one click.

This is a beginner-friendly project for Python enthusiasts to learn about API integration and networking concepts.


## 🚀 Features

*   Tracks your own IP address.
*   Tracks any other public IP address.
*   Provides detailed information such as hostname, city, region, and timezone.
*   Lightweight and easy to use.

## 📦 Installation

To run the IP Tracker, follow these steps:

1.  Clone the repository from GitHub:
    
    ```bash
    git clone https://github.com/dev-aryan-com/IP-Tracker.git
    ```
    
2.  Navigate to the project directory:
    
    ```bash
    cd IP-Tracker
    ```
    
3.  Install the required dependencies:
    
    ```bash
    pip install requests
    ```

    
## ⚙️ Usage

Run the script using Python:

```bash
python tracker.py
```

When the script runs, you will see the following options:

*   **Enter \[S\]** to track your own IP address.
*   **Enter an IP address** to fetch its details.
*   **Enter \[X\]** to exit the program.

Example:

```bash
IP Tracker v1.0

Enter [S] to track your own IP
Enter an IP address to track
Enter [X] to exit

Enter your choice : S

Fetching your IP details...

IP Address Details:
IP: 203.0.113.5
Hostname: example.com
City: Bangalore
Region: Karnataka
Country: IN
Location (lat,long): 12.9716,77.5946
Organization: AS12345 ISP Name
Timezone: Asia/Kolkata
```

## 🐞 Issues

If you encounter any bugs or have suggestions for improvements, feel free to open an issue in the repository. Make sure to provide as much detail as possible.

## 📜 License

This project is licensed under the MIT License. See the LICENSE file for details.

## 👨‍💻 Author

⭐️ From [Aryan Raj](https://github.com/dev-aryan-com)
