import src.app_gui as app_gui


def run(options):
    try:
        app_gui.open_tool_window(options)
    except Exception as error:
        raise error

    # app_audit.remove_elements(options['tmp_folder'])
