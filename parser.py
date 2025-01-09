import csv
from collections import defaultdict

# function to load the lookup table
def load_lookup_table(lookup_file):
    lookup = {}
    with open(lookup_file, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            key = (row['dstport'], row['protocol'].strip().lower())
            lookup[key] = row['tag']
    return lookup

# function to parse flow logs
def parse_flow_logs(log_file):
    flow_logs = []
    with open(log_file, 'r') as file:
        for line in file:
            parts = line.split()
            
            if len(parts) >= 14: 
                flow_logs.append({
                    'dstport': parts[5],
                    'protocol': 'tcp' if parts[7] == '6' else 'udp', 
                })
    return flow_logs

def process_logs(flow_logs, lookup):
    tag_counts = defaultdict(int)
    port_protocol_counts = defaultdict(int)

    for log in flow_logs:
        dstport = log['dstport']
        protocol = log['protocol']
        key = (dstport, protocol)
        
        tag = lookup.get(key, 'Untagged')
        tag_counts[tag] += 1

        port_protocol_counts[key] += 1

    return tag_counts, port_protocol_counts

# Writing tag counts to output file
def write_tag_counts(tag_counts, output_file):
    with open(output_file, 'w') as file:
        writer = csv.writer(file)
        writer.writerow(['Tag', 'Count'])
        for tag, count in tag_counts.items():
            writer.writerow([tag, count])

# Writing port/protocol counts to output file
def write_port_protocol_counts(port_protocol_counts, output_file):
    with open(output_file, 'w') as file:
        writer = csv.writer(file)
        writer.writerow(['Port', 'Protocol', 'Count'])
        for (port, protocol), count in port_protocol_counts.items():
            writer.writerow([port, protocol, count])

def main(flow_log_file, lookup_file, tag_output_file, port_protocol_output_file):
    
    lookup = load_lookup_table(lookup_file)
    
    flow_logs = parse_flow_logs(flow_log_file)

    tag_counts, port_protocol_counts = process_logs(flow_logs, lookup)

    write_tag_counts(tag_counts, tag_output_file)
    write_port_protocol_counts(port_protocol_counts, port_protocol_output_file)

# Example usage
if __name__ == "__main__":
    flow_log_file = 'flow_logs.txt'
    lookup_file = 'lookup_table.csv'
    tag_output_file = 'tag_counts.csv'
    port_protocol_output_file = 'port_protocol_counts.csv'

    main(flow_log_file, lookup_file, tag_output_file, port_protocol_output_file)
