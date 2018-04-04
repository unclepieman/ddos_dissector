
# coding: utf-8

# In[ ]:


import subprocess
import os


# In[ ]:


def nfdump_filter_anon(input_file, pattern, dst_ip):
    
    
    # Filtering based on host/proto and ports
    if len(pattern['src_ports']) > 1:
        filter_out = "dst ip " + dst_ip + " and proto " + str(pattern['ip_protocol']) + " and dst port " + str(pattern["dst_ports"].keys()[0])
    elif len(pattern['dst_ports']) > 1:
        filter_out = "dst ip " + dst_ip + " and proto " + str(pattern['ip_protocol']) + " and src port " + str(pattern["src_ports"].keys()[0])
        
    #proper filename based on start timestamp(converted to epoch) and selected port
    date = str(pattern["start_timestamp"])[:10]
    formatis = '%Y-%m-%d'
    epoch = int(time.mktime(time.strptime(date, formatis)))

    filename = str(epoch) + "_" + pattern["selected_port"] + ".nfdump"
    
    #running nfdump with the filters created above
    p = subprocess.Popen(["nfdump -r " + input_file + " -w output/nfdumptemp " + "'" + filter_out + "'"], shell=True, stdout=subprocess.PIPE)
    p.communicate()
    p.wait()
    #
    #
    #
    #NEED to add the replacing in ips
    #
    #
    #
    return "created nfdump temp file - NOT anonymized"

