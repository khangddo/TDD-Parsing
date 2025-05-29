import sys
import matplotlib.pyplot as vis
import csv
import pandas as pan
import csv
import numpy as np

# def visual(timestamp_map):
#     map = timestamp_map

#     # Tag Latency
#     # x = timestamp (us) (list)
#     # y = response duration (us) (list)
#     vis.plot(x, y)
#     vis.xlabel("x")
#     vis.ylabel("y")
#     vis.tiltle("Tag Latency")
#     vis.show()
    
#     # GEN2 State Transitions (bar chart)
#     # x = timestamp (us) (list)
#     # y = GEN2_STATE (list)
#     vis.bar(x, y)
#     vis.xlabel("x")
#     vis.ylabel("y")
#     vis.tiltle("GEN2 State Transitions")
#     vis.show()
    
#     # RX_BIT_LEN Overtime
#     # x = timestamp (us) (list)
#     # y = RX_BIT_LEN (list)
#     vis.plot(x, y)
#     vis.xlabel("x")
#     vis.ylabel("y")
#     vis.tiltle("RX_BIT_LEN Overtime")
#     vis.show()
    
#     # Tag Reply to Reader Next Command Duration
#     # x = timestamp (us) (list)
#     # y = duration (us) (list)
#     vis.plot(x, y)
#     vis.xlabel("x")
#     vis.ylabel("y")
#     vis.tiltle("Tag Reply to Reader Next Command Duration")
#     vis.show()

def command_latency(list, axis):
    x = []
    y = []
    i = 1
    for row in list:
        reader_ts, reader_cmd, tag_ts, tag_cmd, dur = row.split(',', 6)
        x.append(i)
        y.append(dur)
        i += 1
    axis[2].plot(x, y)
    axis[2].set_title("Round Trip (us)")
    

def rssi_vs_time(list, axis):
    # Reader Signal Strength
    x = []
    y = []
    for row in list:
        timestamp, kind, tx, ok, rssi, phase, payload = row.split(',', 6)
        if ok == "true":
            x.append(timestamp)
            y.append(rssi)
    # x = timestamp (us) (list)
    # y = Convertes RSSI (dBm) value to power (Watt) (list)
    axis[1].plot(x, y)
    axis[1].set_title("RSSI vs Time")

def phase_vs_time(list, asix):
    # Reader Signal Strength
    x = []
    y = []
    for row in list:
        timestamp, kind, tx, ok, rssi, phase, payload = row.split(',', 6)
        if ok == "true":
            x.append(timestamp)
            y.append(phase)
    # x = timestamp (us) (list)
    # y = Convertes RSSI (dBm) value to power (Watt) (list)
    axis[0].plot(x, y)
    axis[0].set_title("Phase vs Time")


def csv_parser(csv_file):
    list_of_rows = []
    with open(csv_file) as file:
        data = csv.reader(file, delimiter=',')
        next(data) # skip headers
        for row in file:
            list_of_rows.append(row)

    return list_of_rows

                     
if __name__ == "__main__":
    new_reader = csv_parser(sys.argv[1])
    new_sync = csv_parser(sys.argv[2])
    figure, axis = vis.subplots(3, 1)
    rssi_vs_time(new_reader, axis)
    phase_vs_time(new_reader, axis)
    command_latency(new_sync, axis)

    figure.subplots_adjust(hspace=0.5)

    rssi_y = []

    axis[0].set_yticks([0, 100, 200, 300, 500])
    axis[1].set_yticks([-100, -80, -60, -40, -20])
    axis[2].set_yticks([0, 50, 100, 150, 200])

    for ax in axis:
        ax.tick_params(axis='both', labelrotation=45)

    vis.show()
