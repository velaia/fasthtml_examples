import time

from fasthtml.common import Button, Div, Img, NotStr, Style, fast_app

css = """
.htmx-settling img {
  opacity: 0;
}
img {
 transition: opacity 300ms ease-in !important;
}
"""

app, rt = fast_app(hdrs=[Style(css)])


@app.get
def page():
    return Div(hx_get=get_content.rt(), hx_trigger="load", cls="container")(
        Img(src="/img/bars.svg", alt="Result loading...", cls="htmx-indicator", width="150"),
    )


@app.get
def get_content():
    time.sleep(3)
    return Div(
        NotStr("<ins>This simple text takes 3s to load!</ins>"),
        Button("Reload", hx_target="body", hx_get="/page"),
    )


DESC = "Demonstrates how to lazy load content"
HTMX_URL = "https://htmx.org/examples/lazy-load/"
DOC = """
This example shows how to lazily load an element on a page. We start with an initial state that looks like this:
::page::
Which shows a progress indicator as we are loading the graph. The graph is then loaded and faded gently into view via a settling CSS transition:
::css::
"""
