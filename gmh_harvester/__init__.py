import importlib.resources as pkg_resources

dynamic_path = (pkg_resources.files(__package__) / "dynamic").as_posix()
securezone_excluded = ["/showGmhHarvesterStatus"]
additionalGlobals = {"API_SERVER": "https://api.kb.dev.seecr.nl"}

from .status import status

hooks = {
    "status.domain": status,
    "status.repositoryGroup": status,
    "status.repository": status,
}
