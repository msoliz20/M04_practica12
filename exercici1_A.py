import xml.etree.ElementTree as ET

p = ET.Element('students')

c1 = ET.SubElement(p, 'student')

a1 = ET.SubElement(c1, 'name')
a1.text = "Marco"
b1 = ET.SubElement(c1, 'surname')
b1.text = "Soliz"
c11 = ET.SubElement(c1, 'email')
c11.text = "msoliz@gmail.com"
d1 = ET.SubElement(c1, 'dni')
d1.text = "27372812S"

c2 = ET.SubElement(p, 'student')

a2 = ET.SubElement(c2, 'name')
a2.text = "Jorge"
b2 = ET.SubElement(c2, 'surname')
b2.text = "Angel"
c22 = ET.SubElement(c2, 'email')
c22.text = "angel@gmail.com"
d2 = ET.SubElement(c2, 'dni')
d2.text = "2837823D"

c3 = ET.SubElement(p, 'student')

a3 = ET.SubElement(c3, 'name')
a3.text = "Miguel"
b3 = ET.SubElement(c3, 'surname')
c33 = ET.SubElement(c3, 'email')
d3 = ET.SubElement(c3, 'dni')

c4 = ET.SubElement(p, 'student')

a4 = ET.SubElement(c4, 'name')
b4 = ET.SubElement(c4, 'surname')
c44 = ET.SubElement(c4, 'email')
d4 = ET.SubElement(c4, 'dni')
tree = ET.ElementTree(p)
tree.write("school.xml")

ET.indent(p)
ET.dump(p)