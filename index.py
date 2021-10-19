# %%
import subprocess

import ipywidgets as widgets


uploader = widgets.FileUpload(accept="", multiple=False)
vbox = widgets.VBox([uploader])


def on_change(change):
    global vbox
    filename = list(uploader.value.keys())[0]
    original_image = uploader.value[filename]["content"]
    inverted_image = subprocess.run(
        "convert -channel RGB -negate - -",
        input=original_image,
        capture_output=True,
        shell=True,
        check=True,
    ).stdout
    vbox.children = [uploader, widgets.Image(value=inverted_image)]


uploader.observe(on_change, "value")
vbox
