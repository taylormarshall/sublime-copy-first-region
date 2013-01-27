import sublime
import sublime_plugin

__author__ = 'Taylor Marshall'


class CopyFirstRegionCommand(sublime_plugin.TextCommand):
  """Copies the first region selected by the user.

  First is considered to be the region that occurs earliest in the file.
  """

  def run(self, edit):
    for region in self.view.sel():
      if not region.empty():
        sublime.set_clipboard(self.view.substr(region))
        return
