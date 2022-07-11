## Responsible for creating landing page's HTML file

import utils

def stage(data):
    html = utils.renderTemplate(data["templates"]["page"], {
        "title":       data["config"]["Site"]["Name"],
        "description": "Sailing blog of SV Curious Cat",
        "logo":        utils.renderTemplate(data["templates"]["link"], {
            "href": ".",
            "content": "Curious Cat",
        }),
        # "navigation":  utils.generateTopBarNavigation(data["config"]["Site"]["DbPath"] + "/"),
        "css":         data["definitions"]["filenames"]["css"],
        "name":        "home",
        "content":     utils.renderMarkdown(open("../data/home.md", "r").read()),
    })
    htmlFile = utils.mkfile(
        data["definitions"]["runtime"]["cwd"],
        data["config"]["Filesystem"]["DestinationDirPath"],
        data["definitions"]["filenames"]["index"]
    )
    htmlFile.write(html)
    htmlFile.close()
    ## Add home page link to sitemap
    if data["config"].getboolean("Site", "CreateSitemap", fallback=False):
        data["sitemap"].append("/")
