import os


class DetectTerm:
    terminal_list = [
        "konsole",
        "terminator",
        "tilda",
        "guake",
        "yakuake",
        "roxterm",
        "eterm",
        "Rxvt",
        "wterm",
        "lxterminal",
        "termKit",
        "st",
        "gnome-terminal",
        "final_term",
        "finalTerm",
        "terminology",
        "xfce4_terminal",
        "xterm",
        "lilyterm",
        "sakura",
        "rxvt-unicode"
    ]



    @staticmethod
    def find_terminal():
        for term in DetectTerm.terminal_list:
            if not os.system(term + " &"):
                return term
