# ============================================================================
# FILE: sorter/line.py
# AUTHOR: PanagiotisS
# DESCRIPTION: Simple filter to sort candidates by line number.
#              Based on sorter/word.py from Tomohito OZAKI.
# License: MIT license
# ============================================================================
from ..base import Base


class Filter(Base):

    def __init__(self, vim):
        super().__init__(vim)

        self.name = 'sorter/line'
        self.description = 'sort candidates by the line number'

    def filter(self, context):
        return sorted(context['candidates'],
                key=lambda x: int(x['action__line']))
