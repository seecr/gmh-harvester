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
