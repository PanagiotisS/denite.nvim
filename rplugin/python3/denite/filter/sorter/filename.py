# ============================================================================
# FILE: sorter/filename.py
# AUTHOR: PanagiotisS
# DESCRIPTION: Simple filter to sort candidates by ascii order of file name
#              and line number.
#              Based on sorter/word.py from Tomohito OZAKI.
# License: MIT license
# ============================================================================
from ..base import Base


class Filter(Base):

    def __init__(self, vim):
        super().__init__(vim)

        self.name = 'sorter/filename'
        self.description = 'sort candidates by the file name/line number'

    def filter(self, context):
        return sorted(context['candidates'],
                      key=lambda x: (x['action__path'], int(x['action__line'])))
