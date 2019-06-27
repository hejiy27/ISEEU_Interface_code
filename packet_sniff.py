import pyshark
import numpy
from . import entropy
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from ISEEU_Utility import file_control
import datetime

def packet_sniff(time):
    #Specify Arguments
    max_ent_rate = 5
    min_ent_rate = 1

    cap=pyshark.LiveCapture(interface='eth0',only_summaries="IP" "protocol")

    #packet Sniffing for a given time
    cap.sniff(timeout=time)

    pkts = [str(pkt).split(" ")[2:5] for pkt in cap._packets]
    cap.close()

    #Change the rows and columns of list.
    analytical_resource = numpy.transpose(pkts)

    #Calculate Entropy
    victim_entropy = entropy.calculate_entropy(analytical_resource[0])
    attack_entropy = entropy.calculate_entropy(analytical_resource[1])

    #Print Result
    symbol = victim_entropy["values_symbol"]
    max_symbol = max(symbol,key=symbol.get)
    ent = victim_entropy["entropy"]
    victim_result = "---------- Victim_Status ----------\n" \
                    "total_symbol_count = {count}\n" \
                    "The number of IPs that were found the most = {IP} : {IP_count}\n" \
                    "Entropy rate = {ent}".format(
        count=victim_entropy["total_symbol_count"],
        IP = max_symbol,
        IP_count = symbol[max_symbol],
        ent = ent)
    print(victim_result)

    if ent <= min_ent_rate or ent >= max_ent_rate:
        print("You are Victim!")
    else :
        print("You are not Victim")

    symbol = attack_entropy["values_symbol"]
    max_symbol = max(symbol,key=symbol.get)
    ent = attack_entropy["entropy"]
    attack_result = "---------- Attack_Status ----------\n" \
                    "total_symbol_count = {count}\n" \
                    "The number of IPs that were found the most = {IP} : {IP_count}\n" \
                    "Entropy rate = {ent}".format(
        count=attack_entropy["total_symbol_count"],
        IP = max_symbol,
        IP_count = symbol[max_symbol],
        ent = ent)
    print(attack_result)

    if ent <= min_ent_rate or ent >= max_ent_rate:
        print("You are Attacker!")
    else :
        print("You are not Attacker")

    print("\nPacket Test ends....")
    
    #Data Save
    dt = datetime.datetime.now()
    file_date = dt.strftime("%Y%m%d%H%M")
    save_path = "{}/result/Packet".format(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
    with file_control.file_open(save_path,file_date,'w') as save_file:
        save_file.write(victim_result+"\n"+attack_result)
