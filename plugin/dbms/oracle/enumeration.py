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
from sqlmap.lib.core.common import getLimitRange
from sqlmap.lib.core.common import isAdminFromPrivileges
from sqlmap.lib.core.common import isInferenceAvailable
from sqlmap.lib.core.common import isNoneValue
from sqlmap.lib.core.common import isNumPosStrValue
from sqlmap.lib.core.common import isTechniqueAvailable
from sqlmap.lib.core.compat import xrange
from sqlmap.lib.core.data import conf
from sqlmap.lib.core.data import kb
from sqlmap.lib.core.data import logger
from sqlmap.lib.core.data import queries
from sqlmap.lib.core.enums import CHARSET_TYPE
from sqlmap.lib.core.enums import DBMS
from sqlmap.lib.core.enums import EXPECTED
from sqlmap.lib.core.enums import PAYLOAD
from sqlmap.lib.core.exception import SqlmapNoneDataException
from sqlmap.lib.core.settings import CURRENT_USER
from sqlmap.lib.request import inject
from sqlmap.plugins.generic.enumeration import Enumeration as GenericEnumeration

class Enumeration(GenericEnumeration):
    def getRoles(self, query2=False):
        infoMsg = "fetching database users roles"

        rootQuery = queries[DBMS.ORACLE].roles

        if conf.user == CURRENT_USER:
            infoMsg += " for current user"
            conf.user = self.getCurrentUser()

        logger.info(infoMsg)

        # Set containing the list of DBMS administrators
        areAdmins = set()

        if any(isTechniqueAvailable(_) for _ in (PAYLOAD.TECHNIQUE.UNION, PAYLOAD.TECHNIQUE.ERROR, PAYLOAD.TECHNIQUE.QUERY)) or conf.direct:
            if query2:
                query = rootQuery.inband.query2
                condition = rootQuery.inband.condition2
            else:
                query = rootQuery.inband.query
                condition = rootQuery.inband.condition

            if conf.user:
                users = conf.user.split(',')
                query += " WHERE "
                query += " OR ".join("%s = '%s'" % (condition, user) for user in sorted(users))

            values = inject.getValue(query, blind=False, time=False)

            if not values and not query2:
                infoMsg = "trying with table 'USER_ROLE_PRIVS'"
                logger.info(infoMsg)

                return self.getRoles(query2=True)

            if not isNoneValue(values):
                for value in values:
                    user = None
                    roles = set()

                    for count in xrange(0, len(value or [])):
                        # The first column is always the username
                        if count == 0:
                            user = value[count]

                        # The other columns are the roles
                        else:
                            role = value[count]

                            # In Oracle we get the list of roles as string
                            roles.add(role)

                    if user in kb.data.cachedUsersRoles:
                        kb.data.cachedUsersRoles[user] = list(roles.union(kb.data.cachedUsersRoles[user]))
                    else:
                        kb.data.cachedUsersRoles[user] = list(roles)

        if not kb.data.cachedUsersRoles and isInferenceAvailable() and not conf.direct:
            if conf.user:
                users = conf.user.split(',')
            else:
                if not len(kb.data.cachedUsers):
                    users = self.getUsers()
                else:
                    users = kb.data.cachedUsers

            retrievedUsers = set()

            for user in users:
                unescapedUser = None

                if user in retrievedUsers:
                    continue

                infoMsg = "fetching number of roles "
                infoMsg += "for user '%s'" % user
                logger.info(infoMsg)

                if unescapedUser:
                    queryUser = unescapedUser
                else:
                    queryUser = user

                if query2:
                    query = rootQuery.blind.count2 % queryUser
                else:
                    query = rootQuery.blind.count % queryUser
                count = inject.getValue(query, union=False, error=False, expected=EXPECTED.INT, charsetType=CHARSET_TYPE.DIGITS)

                if not isNumPosStrValue(count):
                    if count != 0 and not query2:
                        infoMsg = "trying with table 'USER_SYS_PRIVS'"
                        logger.info(infoMsg)

                        return self.getPrivileges(query2=True)

                    warnMsg = "unable to retrieve the number of "
                    warnMsg += "roles for user '%s'" % user
                    logger.warning(warnMsg)
                    continue

                infoMsg = "fetching roles for user '%s'" % user
                logger.info(infoMsg)

                roles = set()

                indexRange = getLimitRange(count, plusOne=True)

                for index in indexRange:
                    if query2:
                        query = rootQuery.blind.query2 % (queryUser, index)
                    else:
                        query = rootQuery.blind.query % (queryUser, index)
                    role = inject.getValue(query, union=False, error=False)

                    # In Oracle we get the list of roles as string
                    roles.add(role)

                if roles:
                    kb.data.cachedUsersRoles[user] = list(roles)
                else:
                    warnMsg = "unable to retrieve the roles "
                    warnMsg += "for user '%s'" % user
                    logger.warning(warnMsg)

                retrievedUsers.add(user)

        if not kb.data.cachedUsersRoles:
            errMsg = "unable to retrieve the roles "
            errMsg += "for the database users"
            raise SqlmapNoneDataException(errMsg)

        for user, privileges in kb.data.cachedUsersRoles.items():
            if isAdminFromPrivileges(privileges):
                areAdmins.add(user)

        return kb.data.cachedUsersRoles, areAdmins
