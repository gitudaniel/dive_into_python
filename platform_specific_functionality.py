"""Platform specific functionality

This module shows how to handle usecases for various operating
systems. Namely windows, mac and linux.
"""
# Bind the name getpass to the appropriate function

try:
    import termios, TERMIOS
except ImportError:
    try:
        import msvcrt
    except ImportError:
        try:
i            from EasyDialogs import AskPasswork # For apple users
        except ImportError:
            getpass = default_getpass
        else:
            getpass = AskPassword
    else:
        getpass = win_getpass
else:
    getpass = unix_getpass

