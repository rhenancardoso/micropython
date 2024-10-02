include("$(PORT_DIR)/boards/manifest.py")
freeze("./modules")
package("microdot",base_path="../../../../../src/lib/microdot/src")
