# Flow Log Parser

This project is a Python program that processes flow log data and maps each row to a tag based on a lookup table. The program also generates summary statistics, including counts of matches for each tag and port/protocol combination.

## 🌟 Features

- Parses flow log files and a lookup table.
- Maps flow log entries to tags based on `dstport` and `protocol`.
- Outputs:
  - **Tag Counts**: The number of matches for each tag.
  - **Port/Protocol Combination Counts**: The number of matches for each unique combination of destination port and protocol.
- Handles unmatched rows by tagging them as `Untagged`.
- Case-insensitive matching for protocols.

## 📂 Input Files

### 1. Flow Log File
A plain text file containing network traffic logs, with each row representing a network flow.

**Example (flow_logs.txt):**
```
2 123456789012 eni-0a1b2c3d 10.0.1.201 198.51.100.2 443 49153 6 25 20000 1620140761 1620140821 ACCEPT OK
2 123456789012 eni-4d3c2b1a 192.168.1.100 203.0.113.101 23 49154 6 15 12000 1620140761 1620140821 REJECT OK
```

### 2. Lookup Table File
A CSV file mapping specific `dstport` and `protocol` combinations to a tag.

**Example (lookup_table.csv):**
```csv
dstport,protocol,tag
25,tcp,sv_P1
443,tcp,sv_P2
23,tcp,sv_P1
110,tcp,email
993,tcp,email
143,tcp,email
```

## 📊 Output Files

### 1. Tag Counts
A CSV file listing the number of matches for each tag.

📝 **Example (tag_counts.csv):**
```csv
Tag,Count
sv_P2,1
sv_P1,2
sv_P4,1
email,3
Untagged,9
```

### 2. Port/Protocol Combination Counts
A CSV file listing the number of matches for each unique port/protocol combination.

📝 **Example (port_protocol_counts.csv):**
```csv
Port,Protocol,Count
22,tcp,1
23,tcp,1
25,tcp,1
110,tcp,1
143,tcp,1
443,tcp,1
```

## 🚀 Usage

### Prerequisites
- Python 3.x
- CSV input files (flow logs and lookup table)

### Running the Program
1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/flow-log-parser.git
   cd flow-log-parser
   ```

2. Place your input files (`flow_logs.txt` and `lookup_table.csv`) in the project directory.

3. Run the program:
   ```bash
   python3 parser.py
   ```

4. The output files `tag_counts.csv` and `port_protocol_counts.csv` will be generated in the project directory. (Attached for demo)

## ⚙️ How It Works

1. **Load Lookup Table:**
   - Reads the CSV file and creates a dictionary mapping `(dstport, protocol)` to tags.

2. **Parse Flow Logs:**
   - Reads the flow logs and extracts relevant fields (`dstport` and `protocol`).

3. **Tag Mapping:**
   - Maps each flow log entry to a tag using the lookup table.
   - Unmatched rows are tagged as `Untagged`.

4. **Output Generation:**
   - Generates two output files with counts for tags and port/protocol combinations.

## 📋 Assumptions

- The program supports only the **default flow log format**.
- Only **version 2** of flow logs is supported.
- Input files must conform to the examples provided (flow log and lookup table formats).
- No external libraries are used (e.g., Hadoop, Spark, pandas). The program is designed to be lightweight and run on a local machine without additional dependencies.

---

## 📜 Tests and Analysis

### Tests Performed
- **Functional Tests:** Verified program functionality with sample flow logs and lookup table files.
- **Boundary Tests:** Tested with empty flow logs, unsupported formats, and mismatched lookup table entries.
- **Performance Tests:** Processed large flow log files (up to 10 MB) to ensure the program handles size constraints efficiently.

### Analysis
- The program efficiently parses files and processes mappings using dictionaries for constant-time lookups.
- Modular functions ensure readability and maintainability of the codebase.
- Error handling and validations ensure robustness when dealing with unexpected inputs.


## 🤝 Contributing

Contributions are welcome! Please open an issue or submit a pull request for any improvements or bug fixes.

## 📧 Contact

For any inquiries or feedback, please reach out to [devika24march@gmail.com].
