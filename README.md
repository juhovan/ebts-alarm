### EBTS alarm panel

Interact between Home Assistant and EBTS alarm panel

## Environment
EBTS_IP = IP address of EBTS
EBTS_PIN = EBTS level 2 pin code
EBTS_USER = Username for EBTS user with "Change settings" permission
EBTS_PASSOWRD = Password for EBTS user

## Endpoints
- /getstate Get current alarm state (1 = disarmed, 2 = armed away, 3 = armed home)
- /setstate Set alarm state `'{"state": "{{ state }}"}'`
- /setmessage Set custom message for alarm panel ` '{"slot": "{{ slot }}","message": "{{ message }}"}'`
