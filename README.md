# Firefuzz

Firefuzz is a password spraying tool designed to find default credentials by bypassing firewall rate limitations. It accomplishes this by changing the static IP address within a local network.

## Demo

Watch a demo of Firefuzz in action: [Demo Video](https://github.com/Jarvis0p/Firefuzz/assets/102745332/7cdca38f-acf4-4265-ae31-c3b2c9e98cef)


## Requirements

To install the necessary Python modules for Firefuzz, you can use the provided `requirements.txt` file. Run the following command in your terminal:

```bash
pip install -r requirements.txt
```
## Usage

### Linux (Root Privilege Required)

1. Clone the Firefuzz repository:

2. Navigate to the Firefuzz directory:

3. Run the Firefuzz code for Linux with root privilege:

```bash
sudo python3 firefuzz-linux.py
```

### Windows (Administrative Privilege Required)

1. Clone the Firefuzz repository.

2. Open Command Prompt with administrative privilege. To do this, search for "Command Prompt" in the Start menu, right-click it, and select "Run as administrator."

6. Navigate to the Firefuzz directory using the `cd` command:

7. Run the Firefuzz code for Windows with administrative privilege:

## Note

- This tool should be used responsibly and only on systems and networks you have explicit permission to test. Unauthorized use of this tool may violate the law.

- Be cautious when using this tool on your own network, as it may trigger security alerts or cause disruptions.

- The provided IP address and network configurations in the code are examples. Modify them to match your specific network setup.

- The tool may require adjustments to work with different network interfaces or configurations, depending on your operating system.

- Always run the tool with the necessary privileges to change network configurations, as mentioned in the instructions.



