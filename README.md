# Market-Alerts

Market is a simple GUI based cross platform application to create price alerts specifically for crypto market. It uses the Wazirx API for fetching the prices 
and PyQT6 for the GUI side of things.

### Installation
- Clone the repository 
  ```sh
  git clone https://github.com/Taru-garg/Market-Alerts
  ```
- In the folder where you cloned the repo type 
  ```sh
  cd Market-Alerts
  ```
- Install the requirements
  ```
   pip3 install -r requirements.txt
  ```
- To create alert
  ```sh
   python3 run.py
  ```
 <b>Note</b>: One can run alert_check.py to check for the alerts. Though there are still some issues in the implementation and the alrt file also needs to be updated to make the process
 much more seamless ideally it would open as soon as the GUI starts.
 
 ### Views 
 
 - Start View
 - New Alert View
 - Old Alert View
