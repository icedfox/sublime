import sublime, sublime_plugin, time

class InsertFileHeaderCommand(sublime_plugin.TextCommand):
	def run(self, edit, **args):
		line = 0

		pt = self.view.text_point(line, 0)

		self.view.insert(edit, line, '\n\n')
		
		self.view.sel().clear()
		self.view.sel().add(sublime.Region(pt))

		self.view.show(pt)

		self.view.run_command("insert", { "characters": "/** \n"})
		self.view.run_command("insert", { "characters": " * \n"})
		self.view.run_command("insert", { "characters": "* Created on " + time.strftime("%c") +"\n"})
		self.view.run_command("insert_snippet", { "name": "Packages/User/file-header.sublime-snippet" })
