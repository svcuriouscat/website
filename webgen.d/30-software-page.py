## Responsible for creating software page's HTML file

import webgen

def stage(data):
    useRelativePaths = data["config"].getboolean("Site", "UseRelativePaths", fallback=None)

    html = webgen.renderTemplate(data["templates"]["page"], {
        "title":       webgen.getWebPageTitle(data["config"]["Site"]["Name"], ["Software"]),
        "description": "All the amazing digital tools",
        "navigation": webgen.renderTemplate(data["templates"]["navigation"], {
            "activePage": "software",
        }),
        "criticalcss": webgen.compileSass(open("../src/styles/critical.scss", "r").read()),
        "css":         webgen.buildPath("/" + data["definitions"]["filenames"]["css"], "/software/", relative=useRelativePaths),
        "class":        "software content",
        "content":     webgen.renderMarkdown(open("../data/software.md", "r").read()),
    })
    htmlFile = webgen.mkfile(
        data["definitions"]["runtime"]["cwd"],
        data["config"]["Filesystem"]["DestinationDirPath"],
        data["config"]["Site"]["SoftwarePath"],
        data["definitions"]["filenames"]["index"]
    )
    htmlFile.write(html)
    htmlFile.close()
    ## Copy asset files
    webgen.cpr(
        webgen.resolveFsPath(data["definitions"]["runtime"]["cwd"], "data", "software"),
        webgen.resolveFsPath(data["definitions"]["runtime"]["cwd"], data["config"]["Filesystem"]["DestinationDirPath"], "assets", data["config"]["Site"]["SoftwarePath"])
    )

    ## Add software page link to sitemap
    if data["config"].getboolean("Site", "CreateSitemap", fallback=False):
        data["sitemap"].append("/" + data["config"]["Site"]["SoftwarePath"] + "/")
