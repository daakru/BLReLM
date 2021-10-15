import re


class UE3_Config_Parser():
    def __init__(self):
        self.classes = {}
        self.arrays = {}
        self.structs = {}
        self.comments = {}
        self.invalid = {}

    def is_comment(self, line):
        """
        Most people seem to be under the impression that the semicolon denotes
        comments in configuration files, but they aren't.

        This behavior is intentional. Technically any character can represent a
        different key-value pair. Typically, a semicolon is placed at the
        beginning of a new line. It works like a comment, but it's not actually.

            ; This is a Comment
            ; So is this!

        Parameters
        ----------
        line : TYPE
            DESCRIPTION.

        Returns
        -------
        None.

        """
        return line.startswith(';')

    def is_valid(self, line):
        """
        Typical configuration files consist of sections of key-value pairs,
        arranged as follows:
            [Section]
            Key=Value

        Special Characters:

            +  Adds a line if that property doesn't exist yet (from a previous
               configuration file or earlier in the same configuration file).

            -  Removes a line (but it has to be an exact match).

            .  Adds a new property.

            !  Removes a property; but you don't have to have an exact match,
                just the name of the property.

        Note: . is like + except it will potentially add a duplicate line.
            This is useful for the bindings (as seen in DefaultInput.ini),
            for instance, where the bottom-most binding takes effect, so if
            you add something like:

                [Engine.PlayerInput]
                Bindings=(Name="Q",Command="Foo")
                .Bindings=(Name="Q",Command="Bar")
                .Bindings=(Name="Q",Command="Foo")

            It will work appropriately. Using a + there would fail to add the
            last line, and your bindings would be incorrect. Due to
            configuration file combining, the above usage pattern can happen.

        Parameters
        ----------
        line : TYPE
            DESCRIPTION.

        Returns
        -------
        None.

        """
        # Invalid Line Definitions:
        # Starts with [] but has text after
        # Has \\ at end of line but has whitespace after
        # Starts with anything but ; or [ and does not have an = anywhere
        # Defining arrays in place is a mess
        re_primarykey = r'^([^;[][^= \n]*)( *= *)\S'
        # replace = '=8'
        # res_str = re.sub(pattern, replace, line)
        match = re.match(re_primarykey, line)
        if match is not None:
            print(match)
            primary_key = match.group(1)
            if match.group().endswith('('):
                # Might be a struct
                pass
            elif match.group().endswith('['):
                # Might be an array
                pass
            breakpoint()
            # subline = line.split('=', 1)
            # primary_key = subline[0].strip()
            # value = subline[1].lstrip()
        pass

    def handle_section_header(self, line):
        """
        Variables used by native code in the configuration file will normally
        have a simple section title.

        For instance, the first section that appears in the DefaultEngnine.ini
        configuration file is simply named [URL].

        However, any variable used by UnrealScript code usually has a fully
        qualified class name which follows the format [(package).(classname)].

        For instance, the [Engine.Engine] section in DefaultEngine.ini points
        to the Engine class stored within the Engine package.

        There are some exceptions to this rule, such as [WinDrv.WindowsClient].
        """
        if ' ' in line.strip():
            pass
        pass

    def parse_localization_file(self, filepath, enc='utf-16-le'):
        with open(filepath, 'r', encoding=enc) as locfile:
            for idx, line in enumerate(locfile):
                if self.is_comment(line):
                    self.comments[idx] = line
                    continue
                elif not self.is_valid(line):
                    self.invalid[idx] = line
                    continue
                elif line.startswith('['):
                    self.handle_section_header(line)
