from simple_calc import runthis
from sequence_calc import runthis2
from graph_plotter import runthis3
from comp_sci_calc import runthis4
i = 1

def run():
    print("type 'simple calc' for basic calcs, 'sequence calc' for calculating sequences, 'graph calc' for graph "
          "plotting, 'base-n calc' for conversion computer values, 'exit' to close program")
    global loop
    loop = str(input("which calculator you want: "))
    if loop == "simple calc":
        runthis()
    elif loop == "sequence calc":
        runthis2()
    elif loop == "graph calc":
        runthis3()
    elif loop == "base-n calc":
        runthis4()
    elif loop == "exit":
        exit

run()
