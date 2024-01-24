SQL_STATEMENTS = {
    "SQL SELECT statement": (
        "select ",
        "show ",
        " top ",
        " distinct ",
        " from ",
        " from dual",
        " where ",
        " group by ",
        " order by ",
        " having ",
        " limit ",
        " offset ",
        " union all ",
        " rownum as ",
        "(case ",
    ),

    "SQL data definition": (
        "create ",
        "declare ",
        "drop ",
        "truncate ",
        "alter ",
    ),

    "SQL data manipulation": (
        "bulk ",
        "insert ",
        "update ",
        "delete ",
        "merge ",
        "load ",
    ),

    "SQL data control": (
        "grant ",
        "revoke ",
    ),

    "SQL data execution": (
        "exec ",
        "execute ",
        "values ",
        "call ",
    ),

    "SQL transaction": (
        "start transaction ",
        "begin work ",
        "begin transaction ",
        "commit ",
        "rollback ",
    ),

    "SQL administration": (
        "set ",
    ),
}