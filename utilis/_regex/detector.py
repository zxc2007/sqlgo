import re
import os
import sys
import os
import sys
current_directory = os.getcwd()

sys.path.append(current_directory)



from src.logger.log import logger
from src.core.common.column.commoncolumn import common_columns_list

def extract_context(text, keyword):
    pattern = re.compile(r'\b(?:\S+\s+){0,5}' + re.escape(keyword) + r'(?:\s+\S+){0,5}\b', re.IGNORECASE)

    matches = pattern.finditer(text)

    results = []

    for match in matches:
        results.append(match.group(0))

    return results

def count_keywords(text, keywords):
    keyword_counts = {}

    for keyword in keywords:
        keyword_counts[keyword] = len(extract_context(text, keyword))

    return keyword_counts

def Detect(text):
    sample_text = ""
    sample_text += text

    # Keywords to search for
    global keywords
    keywords = ['id', 'error', 'host', 'admin','mysql','sql','oracle','connector','connection','Error','Connector','Connect']
    keywords.extend(common_columns_list)

    # Count occurrences of keywords
    keyword_counts = count_keywords(sample_text, keywords)

    # Print keyword counts
    for keyword, count in keyword_counts.items():
        logger.info(f"{keyword.capitalize()} count: {count}")

    # Print 5 sentences before and after each keyword occurrence
    for keyword in keywords:
        logger.info(f"\nSentences around '{keyword}':")
        occurrences = extract_context(sample_text, keyword)
        for occurrence in occurrences:
            return occurrence.strip()