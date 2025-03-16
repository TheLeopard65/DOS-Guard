# DOS-Guard

## Overview

**DOS-Guard** is a powerful network packet monitoring tool built with Flask and Scapy. It captures and analyzes network packets in real-time, providing insights into network traffic and potential DDoS attacks. With a user-friendly web interface, DOS-Guard allows users to visualize packet data and monitor network activity effectively.

## Features

- **Real-time Packet Sniffing**: Capture and analyze network packets as they traverse your network.
- **Web Dashboard**: A responsive web interface that displays captured packet data and statistics.
- **Protocol Analysis**: Identify and categorize packets by protocol (TCP, UDP, ICMP, etc.).
- **DDoS Detection**: Monitor for potential DDoS attacks based on packet statistics.
- **SQLite Database**: Store captured packet data for historical analysis and reporting.

## Getting Started

### Prerequisites

Before you begin, ensure you have the following installed:

- Python 3.x
- pip (Python package installer)
- Scapy
- Flask
- Flask-SocketIO
- Eventlet

### Installation

1. **Clone the repository**:

   ```bash
   git clone https://github.com/TheLeopard65/DOS-Guard.git
   cd DOS-Guard
   ```

2. **Create a virtual environment** (optional but recommended):

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install the required packages**:

   ```bash
   pip install -r requirements.txt
   ```

### Usage

1. **Run the application**:

   ```bash
   python detector.py
   ```

2. **Access the web interface**:

   Open your web browser and navigate to `http://localhost:5000`.

3. **Start capturing packets**:

   The application will automatically start capturing packets and display them in real-time on the dashboard.

### Database Initialization

The application will create an SQLite database file named `Events.db` in the project directory. The necessary tables will be created automatically upon the first run.

## Contributing

Contributions are welcome! If you have suggestions for improvements or new features, please fork the repository and submit a pull request.

1. Fork the repository.
2. Create your feature branch (`git checkout -b feature/YourFeature`).
3. Commit your changes (`git commit -m 'Add some feature'`).
4. Push to the branch (`git push origin feature/YourFeature`).
5. Open a pull request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- [Flask](https://flask.palletsprojects.com/) - The web framework used.
- [Scapy](https://scapy.readthedocs.io/en/latest/) - The packet manipulation library.
- [Socket.IO](https://socket.io/) - For real-time communication between the server and client.

---

**Happy Sniffing!** 🚀
