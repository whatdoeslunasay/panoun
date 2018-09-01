# Pseudo-Code für erste Entwürfe:

import Panoun

# 1:

inputstr = "Das ist Alex. Er ist 20 Jahre alt, geht gerne schwimmen und studiert Informatik."

Panoun.transform(inputstr, from="male", to="xie") # idealerweise ist from-Parameter optional, wenn es automatisch erkannt wird.

# returnt: "Das ist Alex. Xie ist 20 Jahre alt, geht gerne schwimmen und studiert Informatik."

# 2:

inp = "Auf dem Kongress waren sehr viele Informatiker, aber auch Vertreter aus Politik und Wirtschaft."

Panoun.transform(inputstr, form="generic_masc", to="inclusive_asterisk")

# returnt: "Auf dem Kongress waren sehr viele Informatiker*innen, aber auch Vertreter*innen aus Politik und Wirtschaft."

# 3: 
# mit explizit angegebenen Pronomen

inp = "B spielt mit dem Hund. [Er] wirft ihm einen Ball zu."

Panoun.transform(inp, from="male", to="female", explicit_pronouns=True) 
# Klammern/Markup im Originalstring werden intern gespeichert, aber für Ausgabe rausgenommen, damit nicht auffällt, was damit gemacht wurde. Es sei denn natürlich, man will das noch.

# returnt "B spielt mit dem Hund. Sie wirft ihm einen Ball zu." 


