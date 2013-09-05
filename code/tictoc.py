import time

starts = []

def tic( msg = None ):
    if msg is not None:
        print ( '+' * (len( starts )+1) ), msg
    
    starts.append( ( time.time(), msg ) )

def toc():
    end = time.time()
    duration = end - starts[-1][0]
    
    if starts[-1][1] is None:
        print ( '=' * len( starts ) ), 'tictoc():', duration
    else:
        print ( '-' * len( starts ) ), starts[-1][1], duration
    
    del starts[-1]
