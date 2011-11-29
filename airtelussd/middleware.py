from werkzeug.debug import DebuggedApplication


def make_werkzeug_debugger(app, global_conf):
    """
    We want to be able to expose the Werkzeug debugger in a paste
    pipline.
    """
    return DebuggedApplication(app, evalex=True)
