import sys
import matplotlib.pyplot as vis
<<<<<<< HEAD
=======
import cvs
>>>>>>> 4255737 (testing cvs parser output)

def visual(timestamp_map):
    map = timestamp_map

    # Tag Latency
    # x = timestamp (us) (list)
    # y = response duration (us) (list)
    vis.plot(x, y)
    vis.xlabel("x")
    vis.ylabel("y")
    vis.tiltle("Tag Latency")
    vis.show()
    
    # GEN2 State Transitions (bar chart)
    # x = timestamp (us) (list)
    # y = GEN2_STATE (list)
    vis.bar(x, y)
    vis.xlabel("x")
    vis.ylabel("y")
    vis.tiltle("GEN2 State Transitions")
    vis.show()
    
    # RX_BIT_LEN Overtime
    # x = timestamp (us) (list)
    # y = RX_BIT_LEN (list)
    vis.plot(x, y)
    vis.xlabel("x")
    vis.ylabel("y")
    vis.tiltle("RX_BIT_LEN Overtime")
    vis.show()
    
    # Tag Reply to Reader Next Command Duration
    # x = timestamp (us) (list)
    # y = duration (us) (list)
    vis.plot(x, y)
    vis.xlabel("x")
    vis.ylabel("y")
    vis.tiltle("Tag Reply to Reader Next Command Duration")
    vis.show()
    
    # Reader Signal Strength
    # x = timestamp (us) (list)
    # y = Convertes RSSI (dBm) value to power (Watt) (list)
    vis.plot(x, y)
    vis.xlabel("x")
    vis.ylabel("y")
    vis.tiltle("Reader Signal Strength")
    vis.show()
<<<<<<< HEAD
    
=======

def cvs_parser(cvs_file):
    with open(cvs_file, newline = '') as cvs:
        reader = cvs.DictReader(cvs)
        for line in reader:
            print(line)
                     
if __name__ == "__main__":
    cvs_parser(sys.argv[2])
>>>>>>> 4255737 (testing cvs parser output)
