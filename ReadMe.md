# Network Scanner
This is project I worked during the Christmas holidays in 2023.

<H2> Description </H2>
This Python-based tool simplifies network exploration and reconnaissance using the Nmap library.  It provides a user-friendly experience and generates informative scan reports.

<H3>Features:</H3>

* **Guided Input:** Validates target IP addresses and networks (CIDR notation) for accurate scanning.
* **Flexible Nmap Options:**  Lets you select common Nmap options to customize scans for service detection, OS identification, or simple ping checks.
* **Efficient Host Discovery:**  Determines which hosts on the network are live. 
* **Hostname Resolution:**  Attempts to find hostnames associated with IP addresses,  making device identification easier.
* **Clear Reporting:**  Produces structured text reports.  Optionally generates PDF reports using Pandoc for convenient sharing. 

<H3>Ideal for: </H3>

* Network administrators 
* Security analysts
* Anyone interested in understanding their network topology

<H2> Disclaimer: </H2>
This tool is designed for authorized network analysis.  It is essential to obtain permission before scanning any network that you do not directly control. Unauthorized network scanning may have legal consequences.

<H2>Requirements</H2>

**Python:** Tested on version 3.6 (Python version 3.6 or Newer)

**External Libriaries**
* **python-nmap:** Required for communicating with Nmap
* **pandoc:** Optional, for creating results in pdf format

<code>pip install requirements.txt</code>

<H2>Installation</H2>

1. **Clone the respository:**

<code> git clone </code>

2. **(Optional) Create a Virtual Environment:**

It's recommended to create a virtual environment to manage dependencies (refer to venv documentation: https://docs.python.org/3/library/venv.html).

3. **Install Dependencies:**

<code> pip3 install requirements.txt </code>

4. **Install Pandoc:** 

Refer to the Pandoc installation instructions for your operating system: https://pandoc.org/installing.html

<H2>Usage</H2>

1. <code> python3 nscanner.py </code>

2. **Input:** The script will prompt you to enter a valid target and Desired Nmap Scan Option

3. **Output:** If Pandoc is installed a pdf is generated, or a txt file will be created.


<H2> Demonstration</H2>



The password for the video is legionxsoul

Thankyou, for using the tool brought to you ny Legion Soul





