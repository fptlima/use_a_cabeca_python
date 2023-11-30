def sanitize (time_string):
    if '-' in time_string:
        splitter = '-'
    elif ':' in time_string:
        splitter = ":"
    else:
        return(time_string)
    (mins, secs) = time_string.split(splitter)
    return(mins + "." + secs)

mins = [1, 2, 3]
secs = [ m * 60 for m in mins]
print(secs)

meters = [1, 10, 3]
feet = [m * 3.281 for m in meters]
print(feet)

lower = ["I", "don't", "like", "spam"]
upper = [s.upper() for s in lower]
print(upper)

dirty = ["2-22","2:22","2.22"]
clear = [sanitize(t) for t in dirty]
print(clear)

clean = [float(s) for s in clear]
print(clean)

transform = [float(sanitize(t)) for t in ["2-22","2:22","2.22"]]
print(transform)