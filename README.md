# AI SOC Automation Project

## How to Run

1. Install dependencies:
pip install -r requirements.txt

2. Run detection engine:
sudo python3 detector/log_detector.py

3. Simulate attack:
echo "PORT_SCAN from 192.168.1.100" >> logs/system.log

4. Run dashboard:
python3 dashboard/app.py

Open browser:
http://127.0.0.1:5000
