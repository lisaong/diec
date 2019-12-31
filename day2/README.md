# Day2 Workshop

## Use Case - IOTA micro vending machine

![use_case](assets/use_case.png)

You work in an animal wildlife sanctuary and take care of a flock of endangered bird species that frequently visit the sanctuary. Due to environmental pollution, the birds need additional nutrients to survive long term.

To improve the health of the birds, the wildlife conservation agency has decided to enhance the bird food with supplementary nutrients. You’ve installed smart feeders scattered across the sanctuary, connected to cellular networks.

The nutrient feeding system needs to meet these requirements:
- Each bird should only consume an optimum amount of supplements assigned to it (no overdose!)
- Unauthorised birds/non-birds should not consume the nutrients
- Provide different mixes of supplements, depending on environmental conditions

This can be solved in a variety of ways. The key advantages that IOTA offers:
- Distributed ledger eliminates the need to centralise and dispatch the feed requests
- Decouples the feeders (producers) from the birds (consumers)
- Built-in way to uniquely identify the feeders and birds
- Supports fine-grained (micro) transactions

Proposed solution using IOTA
- Create an IOTA address for the feeder which is used for monitoring when new funds are added
- Each bird has a QR code attached (in a humane way) pointing to its IOTA wallet
- When a bird visits a feeder:
  1. Scan the bird’s QR code to get its IOTA wallet
  2. Release supplements and deduct from the bird’s balance as it consumes the food. 
  3. Stop adding supplements if the balance is empty.
- [Not covered in workshop] A central system that:
  - Monitors and replenishes the birds’ IOTA wallets based on demand and prescription
  -  Monitors and replenishes the feeders based on transaction volume

## Architecture
![architecture](assets/architecture.png)

## Microbit to MQTT relay
![relay](assets/microbit_to_mqtt.png)

## Installation
### Setting up test IOTA Tangle

Go to: https://github.com/iota-community/one-command-tangle

```
sudo curl -L "https://github.com/docker/compose/releases/download/1.25.0/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
sudo chmod +x /usr/local/bin/docker-compose
git clone https://github.com/iota-community/one-command-tangle.git
cd one-command-tangle
sudo docker-compose up
```

Add 14265 as inbound port.

To test locally, download IOTA light wallet on laptop: https://github.com/iotaledger/wallet/releases

```
Host: Custom, use http://your_url:14265
Login with seed: SEED99999999999999999999999999999999999999999999999999999999999999999999999999999
```
Note: When you first log into the IOTA Light Wallet, go to RECEIVE > ATTACH TO TANGLE to see your full balance.

### Raspberry Pi

To find the microbit serial port path:
1. Disconnect the Micro:bit
2. `ls /dev/ttyA*`
3. Connect the Micro:bit over USB to the Raspberry Pi
4. `ls /dev/ttyA*`
5. The path is whatever is new in step 4 after the Micro:bit is plugged in. If nothing new comes up, try expand the search path by doing `ls /dev/tty*` instead (note that you'll see a lot more paths here)
6. Launch the docker container **after** connecting the Micro:bit to the Raspberry Pi:
```
cd ~/diec/day2/docker
sh ./launch_docker.sh
```

Running the microservices:
1. Edit `iota_client.py` on the Raspberry Pi to use the URL for your test IOTA Tangle.
2. Generate 1 IOTA seed and address:
```
python3 iota_client.py --gen_address
```
3. Edit feeder/iota_wallets.json. Sender accounts must use the IOTA seed, whereas recipient accounts can use an IOTA address. You basically run steps 1 and 2 three times (where step 2 is optional for the recipient account).
4. Edit docker/.env to update the IOTA Tangle url and Micro:bit serial port path.
5. Run compose
```
cd ~/diec/day2/docker
docker-compose up -d
docker-compose logs -f -t
```
6. Flip the Micro:bit left and right, while clicking button A or B. If all goes well, you should observe traffic like the following:

| Topic | Publisher | Key Subscriber | Payload |
| -- | -- | -- | -- |
|/dev/ttyXXXX/arrival|microbit_to_mqtt.py|nutrient_microservice.py|arrival trigger with bird identifier|
|/dev/ttyXXXX/stream|microbit_to_mqtt.py|nutrient_microservice.py|sensor stream for id/fingerprinting of bird|
|/dev/ttyXXXX/iota|nutrient_microservice.py|iota_microservice.py|nutrient amounts to request payment for|
|/dev/ttyXXXX/dispenser|iota_microservice.py|microbit_to_mqtt.py|IOTA bundle hash of completed transaction|

After an IOTA transaction is issued and confirmed, the Micro:bit will display the bundle hash on its screen.

```
microbit_1  | 2019-12-31T10:36:49.864805335Z pub: {'ts_ms': 47490, 'gest': 'face up', 'accX_mg': -268, 'accY_mg':60, 'accZ_mg': -976, 'temp_C': 30, 'head_degN': 261}
microbit_1  | 2019-12-31T10:36:49.865019554Z pub: {'ts_ms': 47611, 'gest': 'face up', 'accX_mg': -272, 'accY_mg':64, 'accZ_mg': -984, 'temp_C': 30, 'head_degN': 263}
microbit_1  | 2019-12-31T10:36:49.865098512Z pub: {'ts_ms': 47730, 'gest': 'face up', 'accX_mg': -260, 'accY_mg':64, 'accZ_mg': -976, 'temp_C': 30, 'head_degN': 263}
microbit_1  | 2019-12-31T10:36:49.865164606Z pub: {'ts_ms': 47851, 'gest': 'face up', 'accX_mg': -264, 'accY_mg':56, 'accZ_mg': -972, 'temp_C': 30, 'head_degN': 262}
nutrient_1  | 2019-12-31T10:36:53.322551427Z /dev/ttyACM0/stream {'ts_ms': 44876, 'gest': 'face up', 'accX_mg': -268, 'accY_mg': 52, 'accZ_mg': -972, 'temp_C': 30, 'head_degN': 262}

<etc>

nutrient_1  | 2019-12-31T10:36:54.989229448Z nutrient profile {'vitamin A': 15, 'vitamin D3': 20, 'omega-3': 20, 'omega-6': 23, 'lysine': 18, 'id': '123'}
nutrient_1  | 2019-12-31T10:36:54.989346791Z pub: {'vitamin A': 15, 'vitamin D3': 20, 'omega-3': 20, 'omega-6': 23, 'lysine': 18, 'id': '123'}
nutrient_1  | 2019-12-31T10:36:54.989380646Z /dev/ttyACM0/stream {'ts_ms': 53335, 'gest': 'face up', 'accX_mg': 24, 'accY_mg': 252, 'accZ_mg': -896, 'temp_C': 30, 'head_degN': 271}
nutrient_1  | 2019-12-31T10:36:54.989412364Z /dev/ttyACM0/stream {'ts_ms': 53454, 'gest': 'face up', 'accX_mg': 312, 'accY_mg': -4, 'accZ_mg': -440, 'temp_C': 30, 'head_degN': 279}
nutrient_1  | 2019-12-31T10:36:54.989451271Z /dev/ttyACM0/arrival {'ts': 53572, 'id': '123\r\nface up'}
nutrient_1  | 2019-12-31T10:36:55.221156948Z /dev/ttyACM0/arrival {'ts': 53674, 'id': '123'}

<etc>

nutrient_1  | 2019-12-31T10:36:55.454948875Z load: offset 500
nutrient_1  | 2019-12-31T10:36:55.455083197Z clean
nutrient_1  | 2019-12-31T10:36:55.455118041Z analyze: 0
nutrient_1  | 2019-12-31T10:36:55.455149031Z combine: 14
iota_1      | 2019-12-31T10:36:57.737318509Z Sending iotas ...
iota_1      | 2019-12-31T10:36:57.737468405Z    Sender seed: SEED99999999999999999999999999999999999999999999999999999999999999999999999999999
iota_1      | 2019-12-31T10:36:57.737513092Z    Recipient address: XQKBUNOERH9CJLLRQTNOLMWBJYUCGXORVNGEOEMBHNCPRVVBNSNNUOJMZODVUJXCOMMYXVLVNNJMBQMYX
iota_1      | 2019-12-31T10:36:57.737547884Z    Amount (iotas): 76
iota_1      | 2019-12-31T10:36:57.737580436Z    Change address: FJHSSHBZTAKQNDTIKJYCZBOZDGSZANCZSWCNWUOCZXFADNOQSYAHEJPXRLOVPNOQFQXXGEGVDGICLMOXX

```

### Windows
```
conda create -n iota python=3
conda activate iota

pip install -r docker\requirements.txt
```

Install mosquitto (tested with 64 bit version): https://mosquitto.org/download/
```
cd C:\Program Files\mosquitto
mosquitto.exe
```

To find the microbit serial port path:
1. Connect the Micro:bit over USB. The driver should automatically install (will require admin privileges)
2. Start -> Device Manager
  - Expand Ports (COM & LPT)
  - Look for something like "USB Serial Device (COM4)" (the last digit will change depending on your computer)
3. Now you can do something like `python microbit_test.py COM4`

The remaining instructions to request IOTA accounts and run the services are the same as Raspberry Pi.

## References
- https://github.com/iotaledger/iota.lib.py (curl extension not available for Raspberry Pi)

