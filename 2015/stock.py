x= "=-('Company 1'!B3*Data!$E$4+'Company 1'!C3*Data!$E$5+'Company 1'!D3*Data!$E$6+'Company 1'!E3*Data!$E$7+'Company 1'!F3*Data!$E$8)"
n="2"
a=x.replace("1",n)
y=a.find("E3")
g="F"
b=a.replace("E",g)
z=b[:y]+"E3"+b[y+2:]
print(z)