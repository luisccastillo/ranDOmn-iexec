import os
import sys
import json
import requests

QNRG_URL = "https://qrng.anu.edu.au/API/jsonI.php?length=256&type=uint8"
CSNRG_URL = "https://csrng.net/csrng/csrng.php?min=0&max=255"


def get_requested_ruint8_count():
    ruint8_count = 1
    if len(sys.argv) > 1:
        try:
            ruint8_count_input = int(sys.argv[1])
            if 1 <= ruint8_count_input <= 256:
                return ruint8_count_input
        except ValueError:
            pass
    return ruint8_count


def call_api(url):
    response = requests.get(url)
    if response.ok:
        return response.text


def get_ruint8_output_list(ruint8_count):
    ruint8_output_list = []
    try:
        ruint8_input_list = json.loads(call_api(QNRG_URL))["data"]
        ruint8_index = json.loads(call_api(CSNRG_URL))[0]["random"]
    except:
        ruint8_count = 0
    for _ in range(ruint8_count):
        ruint8 = ruint8_input_list[ruint8_index]
        ruint8_output_list.append(ruint8)
        ruint8_index += 1
        if ruint8_index >= len(ruint8_input_list):
            ruint8_index = 0
    return ruint8_output_list


def save_result(ruint8_output_list):
    iexec_out = os.environ['IEXEC_OUT']
    result_filepath = os.path.join(iexec_out, 'ruint8_list.txt')
    with open(result_filepath, 'w+') as f:
        f.write(str(ruint8_output_list))
    computed_file_content = {"deterministic-output-path": result_filepath}
    with open(iexec_out + '/computed.json', 'w+') as f:
        json.dump(computed_file_content, f)


if __name__ == '__main__':
    ruint8_count = get_requested_ruint8_count()
    ruint8_output_list = get_ruint8_output_list(ruint8_count)
    save_result(ruint8_output_list)
