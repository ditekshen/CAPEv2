# Copyright (C) 2019 ditekshen
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

from lib.cuckoo.common.abstracts import Signature

class QuasarRATMutexes(Signature):
    name = "quasarrat_mutexes"
    description = "Creates QuasarRAT RAT mutexes"
    severity = 3
    categories = ["RAT"]
    families = ["QuasarRAT"]
    authors = ["ditekshen"]
    minimum = "0.5"

    def run(self):
        indicators = [
            "^QSR_MUTEX_[A-Z0-9a-z]{18}$",
            "VMFvdCsC7RFqerZinfV0sxJFo",
            "9s1IUBvnvFDb76ggOFFmnhIK",
            "ERveMB6XRx2pmYdoKjMnoN1f",
            "ABCDEFGHIGKLMNOPQRSTUVWXYZ",
        ]

        for indicator in indicators:
            match = self.check_mutex(pattern=indicator, regex=True)
            if match:
                self.data.append({"mutex": match})
                return True

        return False