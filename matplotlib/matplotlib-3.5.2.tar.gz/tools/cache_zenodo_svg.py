import urllib.request
from io import BytesIO
import os
from pathlib import Path


def download_or_cache(url, version):
    """
    Get bytes from the given url or local cache.

    Parameters
    ----------
    url : str
        The url to download.
    sha : str
        The sha256 of the file.

    Returns
    -------
    BytesIO
        The file loaded into memory.
    """
    cache_dir = _get_xdg_cache_dir()

    if cache_dir is not None:  # Try to read from cache.
        try:
            data = (cache_dir / version).read_bytes()
        except IOError:
            pass
        else:
            return BytesIO(data)

    with urllib.request.urlopen(
        urllib.request.Request(url, headers={"User-Agent": ""})
    ) as req:
        data = req.read()

    if cache_dir is not None:  # Try to cache the downloaded file.
        try:
            cache_dir.mkdir(parents=True, exist_ok=True)
            with open(cache_dir / version, "xb") as fout:
                fout.write(data)
        except IOError:
            pass

    return BytesIO(data)


def _get_xdg_cache_dir():
    """
    Return the XDG cache directory.

    See
    https://specifications.freedesktop.org/basedir-spec/basedir-spec-latest.html
    """
    cache_dir = os.environ.get("XDG_CACHE_HOME")
    if not cache_dir:
        cache_dir = os.path.expanduser("~/.cache")
        if cache_dir.startswith("~/"):  # Expansion failed.
            return None
    return Path(cache_dir, "matplotlib")


if __name__ == "__main__":
    data = {
        "v3.5.1": "5773480",
        "v3.5.0": "5706396",
        "v3.4.3": "5194481",
        "v3.4.2": "4743323",
        "v3.4.1": "4649959",
        "v3.4.0": "4638398",
        "v3.3.4": "4475376",
        "v3.3.3": "4268928",
        "v3.3.2": "4030140",
        "v3.3.1": "3984190",
        "v3.3.0": "3948793",
        "v3.2.2": "3898017",
        "v3.2.1": "3714460",
        "v3.2.0": "3695547",
        "v3.1.3": "3633844",
        "v3.1.2": "3563226",
        "v3.1.1": "3264781",
        "v3.1.0": "2893252",
        "v3.0.3": "2577644",
        "v3.0.2": "1482099",
        "v3.0.1": "1482098",
        "v2.2.5": "3633833",
        "v3.0.0": "1420605",
        "v2.2.4": "2669103",
        "v2.2.3": "1343133",
        "v2.2.2": "1202077",
        "v2.2.1": "1202050",
        "v2.2.0": "1189358",
        "v2.1.2": "1154287",
        "v2.1.1": "1098480",
        "v2.1.0": "1004650",
        "v2.0.2": "573577",
        "v2.0.1": "570311",
        "v2.0.0": "248351",
        "v1.5.3": "61948",
        "v1.5.2": "56926",
        "v1.5.1": "44579",
        "v1.5.0": "32914",
        "v1.4.3": "15423",
        "v1.4.2": "12400",
        "v1.4.1": "12287",
        "v1.4.0": "11451",
    }
    doc_dir = Path(__file__).parent.parent.absolute() / "doc"
    target_dir = doc_dir / "_static/zenodo_cache"
    citing = doc_dir / "users/project/citing.rst"
    target_dir.mkdir(exist_ok=True, parents=True)
    header = []
    footer = []
    with open(citing, "r") as fin:
        target = header
        for ln in fin:
            if target is not None:
                target.append(ln.rstrip())
            if ln.strip() == ".. START OF AUTOGENERATED":
                target.extend(["", ""])
                target = None
            if ln.strip() == ".. END OF AUTOGENERATED":
                target = footer
                target.append(ln)

    with open(citing, "w") as fout:
        fout.write("\n".join(header))
        for version, doi in data.items():
            svg_path = target_dir / f"{doi}.svg"
            if not svg_path.exists():
                url = f"https://zenodo.org/badge/doi/10.5281/zenodo.{doi}.svg"
                payload = download_or_cache(url, f"{doi}.svg")
                with open(svg_path, "xb") as svgout:
                    svgout.write(payload.read())
            fout.write(
                f"""
{version}
   .. image:: ../../_static/zenodo_cache/{doi}.svg
      :target:  https://doi.org/10.5281/zenodo.{doi}"""
            )
        fout.write("\n\n")
        fout.write("\n".join(footer))
        fout.write('\n')
