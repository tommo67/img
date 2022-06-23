from GrabzIt import GrabzItImageOptions
from GrabzIt import GrabzItClient

grabzIt = GrabzItClient.GrabzItClient("OTNmNmRlZjk4OWZkNGM5ZThmOWZhYWY2YjZjZTg5NjQ=", "P0s/P0BsPzlWP3U/az9XPz9sPzwCGD9qPz8STnIWQAA=")

options = GrabzItImageOptions.GrabzItImageOptions()
options.format = "png"

grabzIt.FileToImage("example.html", options)
# Then call the Save or SaveTo method
grabzIt.SaveTo("result.png")
