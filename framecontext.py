import inspect

def collect_frame_contexts(attr='__frame__', start_depth=1, **immediatecontext):
    """
    Bubbles up the call stack, accumulating
    __frame__ context dicts.
    """

    contexts = []
    frames = inspect.getouterframes( inspect.currentframe() )

    # to exclude our own locals(), start_depth defaults to 1
    for frame, filename, line, function, code_context, index in frames[start_depth:]:

        # search this frame's locals() for the attr
        contexts.insert(0, frame.f_locals.get(attr) )

        # assume that the name 'self' refers to a class instance.
        _self = frame.f_locals.get('self')
        if _self:
            contexts.insert(0, dict( inspect.getmembers(_self) ).get(attr) )

    # these .get()'s will return a lot of None's, filter them out.
    contexts = filter( lambda x: x is not None, contexts)

    # contexts in inner frames override outer frame contexts
    # if provided, immediatecontext takes precedence
    merged_context = {} 
    for context in contexts:
        merged_context.update( context )
    merged_context.update( immediatecontext )

    return merged_context

