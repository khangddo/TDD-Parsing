import sys
import matplotlib.pyplot as vis
import csv
import pandas as pan
import csv
import numpy as np

def command_latency(list, axis):
    x = []
    y = []
    i = 1
    for row in list:
        reader_ts, reader_cmd, tag_ts, tag_cmd, dur = row.split(',', 4)
        x.append(i)
        y.append(float(dur))
        i += 1
    axis[3].plot(x, y)
    axis[3].set_title("Round Trip (us)")
    axis[3].set_ylim(bottom=0)
    

def rssi_vs_timestamps(list, axis):
    # Reader Signal Strength
    x = []
    y = []
    for row in list:
        timestamp, rssi, phase = row.split(',', 2)
        x.append(timestamp)
        y.append(float(rssi))
    # x = timestamp (us) (list)
    # y = Convertes RSSI (dBm) value to power (Watt) (list)
    axis[0].plot(x, y)
    axis[0].set_title("RSSI vs Timestamp")
    axis[0].set_ylim(top=-40)
    axis[0].set_ylim(bottom=-43)

def phase_vs_timestamps(list, axis):
    # Reader Signal Strength
    x = []
    y = []
    for row in list:
        timestamp, rssi, phase = row.split(',', 2)
        x.append(timestamp)
        y.append(float(phase))
    # x = timestamp (us) (list)
    # y = Convertes RSSI (dBm) value to power (Watt) (list)
    axis[1].plot(x, y)
    axis[1].set_title("Phase vs Timestamp")
    axis[1].set_ylim(bottom=0)

def distance_vs_timestamps(list, axis):
    # Reader Signal Strength
    x = []
    y = []
    for row in list:
        timestamp, rssi, distance = row.split(',', 2)
        x.append(timestamp)
        y.append(float(distance))
    # x = timestamp (us) (list)
    # y = distance (m) (list)
    axis[2].plot(x, y)
    axis[2].set_title("Distance vs Timestamp")
    axis[2].set_ylim(top=2.8)
    axis[2].set_ylim(bottom=2.5)

def csv_parser(csv_file):
    list_of_rows = []
    with open(csv_file) as file:
        data = csv.reader(file, delimiter=',')
        next(data) # skip headers
        for row in file:
            list_of_rows.append(row)

    return list_of_rows

                     
if __name__ == "__main__":
    signal_quality = csv_parser(sys.argv[1])
    tag_distance_estimates = csv_parser(sys.argv[2])
    reader_tag_sync = csv_parser(sys.argv[3])

    figure, axis = vis.subplots(4, 1)

    rssi_vs_timestamps(signal_quality, axis)
    phase_vs_timestamps(signal_quality, axis)
    distance_vs_timestamps(tag_distance_estimates, axis)
    command_latency(reader_tag_sync, axis)

    figure.subplots_adjust(hspace=1)


    for ax in axis:
        ax.tick_params(axis='both', labelrotation=45)

    vis.show()
    print("END")
