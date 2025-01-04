import schemdraw
import schemdraw.elements as elm

with schemdraw.Drawing() as d:
    d += elm.BatteryCell().down().label('V')
    d += elm.Line().right()
    d += elm.Line().right()
    d += elm.Resistor().up().label('R3')
    d += elm.Dot(open=True).label('V3')
    d += elm.Resistor().left().label('R2')
    d += elm.Dot(open=True).label('V2')
    d += elm.Resistor().left().label('R1')
    d += elm.Dot(open=True).label('V1')
d.draw()
