extensions = [
    "sphinx-needs",
    "myst_parser",
    "sphinx-copybutton",
]

source_suffix = {
    ".md": "markdown",
}

#html_theme = "furo"

myst_enable_extensions = [
    "colon_fence"
]
sphinx_external_needs=[
    dict(directive="req", title="Requirement", prefix="REQ_", color="#BFD8D2",style="node", style_data={"shape": "box"}),
    dict(directive="spec", title="Specification", prefix="SPEC_", color="#F5B7B1",style="node", style_data={"shape": "box3d"}),
]
