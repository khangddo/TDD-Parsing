import sys

def tdd(tdd_file):
    map = []
    with open(tdd_file, "r") as file:
        tag = {'RX_STATE': "", 'RX_STATE': "", 'RX_STATE': "", 'RX_STATE': "",
                'TS_LSB(us)': "", 'TS_MSB(us)': "", 'Timestamp (us)': "",
                'Command': "", 'RX_BIT_LEN': "", 'RX_DATA': "", 'RX_DATA': "",
                'TS_LSB(us)': "", 'TS_MSB(us)': "", 'Timestamp (us)': "",
                'GEN2_STATE': "", 'FLAGS': "", 'COMPARE_VALID_B': "",
                'MIF_CAL_DONE': "", 'LOCAL_CONFIG': "", 'GLOBAL_CONFIG':"",
                'CAL_WORD': "", 'CONFIG_WORD': ""}
        print("file read: ")
        curr_line = 0
        for line in file:
                print(line)
                line = line.strip()
                if line:
                    tag[line.split[1][:-1]] = line.split[2]
                    if line.split[1][:-1] == 'CONFIG_WORD':
                         map.append(tag)
                     
if __name__ == "__main__":
    tdd(sys.argv[2])