# -*- coding: utf-8 -*-

import kivy
kivy.require('1.8.0')

from kivy.app import App
from kivy.uix.listview import ListView
from kivy.uix.button import Button
from kivy.adapters.simplelistadapter import SimpleListAdapter

from kivy.adapters.listadapter import ListAdapter
from kivy.uix.listview import ListItemButton, ListView


class AstromaximumApp(App):
    pass
'''
    def build(self):
        data = [{'text': str(i), 'is_selected': False} for i in range(100)]
        args_converter = lambda row_index, rec: {'text': rec['text'],
                                                 'size_hint_y': None,
                                                 'height': 25}
        list_adapter = ListAdapter(data=data,
                                   args_converter=args_converter,
                                   cls=ListItemButton,
                                   selection_mode='single',
                                   allow_empty_selection=False)
        list_view = ListView(adapter=list_adapter)
        return list_view
'''
if __name__ == '__main__':
    AstromaximumApp().run()
