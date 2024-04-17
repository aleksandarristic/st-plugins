import sublime, sublime_plugin, time

class InsertDatetimeCommand(sublime_plugin.TextCommand):
    """
    Inserts datetime at current editor at cursor position
    """
    DT_FMT = '%d-%m-%Y %H:%M'
    def run(self, edit):
        dt_str = f'### {time.strftime(InsertDatetimeCommand.DT_FMT)}\n'

        regions = self.view.sel()

        # replace selection in the first region with dt_str
        self.view.replace(edit, regions[0], dt_str)
        
        # unselect the text by clearing the sel() and adding the pt
        end = regions[0].b
        pt = sublime.Region(end, end)
        self.view.sel().clear()
        self.view.sel().add(pt)
