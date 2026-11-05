# pytest-timeout cannot see debugpy (its trace function has no module), so a paused
# breakpoint would be killed after the timeout.
def pytest_configure(config):
    import sys

    if sys.gettrace() is not None and config.pluginmanager.has_plugin("pytest_timeout"):
        config.pluginmanager.unregister(name="pytest_timeout")
