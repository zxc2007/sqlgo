import os
import sys
import readline
sys.path.append(os.getcwd())
from src.core.dicts import SQL_STATEMENTS
from src.core.enums.enums import DBMS
from src.core.enums.enums import AUTOCOMPLETE_TYPE
import re
from src.logger.log import logger
from src.core.Exceptions.exceptions import SQLGODataException


class Custom:
    """
    This class defines custom enumeration functionalities for plugins.
    """

    def __init__(self):
        pass

    def sqlQuery(self, query):
        output = None
        sqlType = None
        query = query.rstrip(';')

        try:
            for sqlTitle, sqlStatements in SQL_STATEMENTS.items():
                for sqlStatement in sqlStatements:
                    if query.lower().startswith(sqlStatement):
                        sqlType = sqlTitle
                        break

            if not re.search(r"\b(OPENROWSET|INTO)\b", query, re.I) and (not sqlType or "SELECT" in sqlType):
                infoMsg = "fetching %s query output: '%s'" % (sqlType if sqlType is not None else "SQL", query)
                logger.info(infoMsg)

                if isinstance(DBMS.ACCESS,str):
                    match = re.search(r"(\bFROM\s+)([^\s]+)", query, re.I)
                    if match and match.group(2).count('.') == 1:
                        query = query.replace(match.group(0), "%s%s" % (match.group(1), match.group(2).replace('.', ".dbo.")))

                query = re.sub(r"(?i)\w+%s\.?" % "_masterdb", "", query)

                output = ""

                return output
            elif True:
                warnMsg = "execution of non-query SQL statements is only "
                warnMsg += "available when stacked queries are supported"
                logger.warning(warnMsg)

                return None
            else:
                if sqlType:
                    infoMsg = "executing %s statement: '%s'" % (sqlType if sqlType is not None else "SQL", query)
                else:
                    infoMsg = "executing unknown SQL command: '%s'" % query
                logger.info(infoMsg)


                output = None

        except SQLGODataException as ex:
            logger.warning(str(ex))

        return output

    def sqlShell(self):
        infoMsg = "calling %s shell. To quit type "
        infoMsg += "'x' or 'q' and press ENTER"
        logger.info(infoMsg)


        while True:
            query = None

            try:
                query = query.strip("; ")
            except UnicodeDecodeError:
                print()
                errMsg = "invalid user input"
                logger.error(errMsg)
            except KeyboardInterrupt:
                print()
                errMsg = "user aborted"
                logger.error(errMsg)
            except EOFError:
                print()
                errMsg = "exit"
                logger.error(errMsg)
                break

            if not query:
                continue

            if query.lower() in ("x", "q", "exit", "quit"):
                break

            output = self.sqlQuery(query)

            if output and output != "Quit":
                pass

            elif not output:
                pass

            elif output != "Quit":
                logger.info("No output!")

    def sqlFile(self):
        infoMsg = "executing SQL statements from given file(s)"
        logger.info(infoMsg)

        for filename in re.split(r"[,|;]", ""):
            filename = filename.strip()

            if not filename:
                continue

            snippet = ""

            if snippet and all(query.strip().upper().startswith("SELECT") for query in (_ for _ in snippet.split(';' if ';' in snippet else '\n') if _)):
                for query in (_ for _ in snippet.split(';' if ';' in snippet else '\n') if _):
                    query = query.strip()
                    if query:
                        pass
            else:
                pass