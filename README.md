# EBTS alarm panel

Interact between Home Assistant and EBTS alarm panel

## Environment
EBTS_IP = IP address of EBTS<br>
EBTS_PIN = EBTS level 2 pin code<br>
EBTS_USER = Username for EBTS user with "Change settings" permission<br>
EBTS_PASSOWRD = Password for EBTS user<br>

## Endpoints
- /getstate Get current alarm state (1 = disarmed, 2 = armed away, 3 = armed home)
- /setstate Set alarm state `'{"state": "{{ state }}"}'`
- /setmessage Set custom message for alarm panel ` '{"slot": "{{ slot }}","message": "{{ message }}"}'`
