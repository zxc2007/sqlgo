import os
import sys
sys.path.append(os.getcwd())
import thirdparty.nmap as nmap
from utilis._regex.getdomain import extract_domain
from src.logger.log import logger

def find_os(url):
    _retval = None
    if "http" in str(url) or "https" in str(url):
        url = extract_domain(url)
        logger.info(f"Extracted domain: {url}")
        
        if url is not None:
            nm = nmap.PortScanner()
            
            # Add a logger.info statement to check the command being executed
            scan_command = f"nmap -O {url}"
            logger.info(f"Executing command: {scan_command}")
            
            nm.scan(hosts=url, arguments="-O")
            
            # Add a logger.info statement to check the scan results
            logger.info(f"Scan results: {nm.all_hosts()}")

            if extract_domain(url) in nm.all_hosts():
                os_match = nm[extract_domain(url)].get("osmatch")
                if os_match:
                    _retval = os_match[0].get("name")
                    logger.info(f"Detected OS: {_retval}")
                else:
                    logger.info("No OS match found.")
            else:
                logger.info(f"Host {extract_domain(url)} not found in scan results.")
        else:
            logger.info("Failed to extract domain from URL.")
    else:
        logger.info("Invalid URL format.")

    return _retval
# logger.info(find_os("https://scanme.org/"))
# Provide a sample URL for testing
