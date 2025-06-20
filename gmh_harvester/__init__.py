## begin license ##
#
# Gemeenschappelijke Metadata Harvester (GMH) uitbreidingen
#
# Copyright (C) 2025 Koninklijke Bibliotheek (KB) https://www.kb.nl
# Copyright (C) 2025 Seecr (Seek You Too B.V.) https://seecr.nl
#
# This file is part of "GMH-Harvester-Addon"
#
# "GMH-Harvester-Addon" is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#
# "GMH-Harvester-Addon" is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with "GMH-Harvester-Addon"; if not, write to the Free Software
# Foundation, Inc., 51 Franklin St, Fifth Floor, Boston, MA  02110-1301  USA
#
## end license ##

import importlib.resources as pkg_resources

dynamic_path = (pkg_resources.files(__package__) / "dynamic").as_posix()
securezone_excluded = ["/showGmhHarvesterStatus"]
additionalGlobals = {
    "API_SERVERS": {
        "kb-acc": "https://api.acc.kb.seecr.nl",
        "kb-prod": "https://api.kb.seecr.nl",
    }
}

from .status import status

hooks = {
    "status.domain": status,
    "status.repositoryGroup": status,
    "status.repository": status,
}
