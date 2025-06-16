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

from urllib.parse import urlencode


def totalErrors(observable, domainId, repositoryGroupId=None, repositoryId=None):
    statuses = observable.call.getStatus(
        domainId=domainId,
        repositoryGroupId=repositoryGroupId,
        repositoryId=repositoryId,
    )
    return sum(int(each["totalerrors"]) for each in statuses)


def status(
    tag, caption, domainId, repositoryGroupId=None, repositoryId=None, observable=None
):
    has_errors = totalErrors(observable, domainId, repositoryGroupId, repositoryId) > 0

    link_args = dict(domainId=domainId)
    if repositoryGroupId is not None:
        link_args["repositoryGroupId"] = repositoryGroupId
    if repositoryId is not None:
        link_args["repositoryId"] = repositoryId

    with tag(
        "a.btn.py-0.btn-success.button-status",
        href="/showGmhHarvesterStatus?{}".format(urlencode(link_args)),
        class_=["btn-danger"] if has_errors else ["btn-success"],
        title="Status",
    ):
        with tag("i.bi.bi-graph-up.pe-2"):
            yield ""
        yield "GMH Status"
