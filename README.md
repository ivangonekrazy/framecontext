collect_frame_contexts
======================
Walks up the stack, searching each frame's locals() for a dictionary named
"__frame__" and accumulating its keys.

Impetus for this was an idea to annotate logging statements
by having something walk up the callstack and gather 'context'
from calling frames or class instances.




