extensions = [
    "sphinx_needs",
    "myst_parser",
    "sphinx.ext.doctest",
    "sphinx.ext.linkcheck",
    "sphinxcontrib.spelling",
  #  "sphinx-copybutton",
]

source_suffix = {
    ".md": "markdown",
}

html_theme = "furo"

myst_enable_extensions = [
    "colon_fence"
]
needs_types=[
    dict(directive="req", title="Requirement", prefix="REQ_"),
    dict(directive="spec", title="Specification", prefix="SPEC_"),
]
needs_extra_links = [
    dict(option="verifies", incoming="verified_by", outgoing="verifies"),
]

spelling_lang = "en_US"