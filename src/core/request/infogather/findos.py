"""
# SQLGO License - Version 1.1

Copyright (C) 2023-2024 Heisenberg

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>.


"""
import os
import sys
from utilis._regex.getdomain import extract_domain
from src.logger.log import logger
try:
    import nmap
except:
    pass

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
