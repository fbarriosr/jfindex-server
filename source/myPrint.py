import os
def printElement(element, large):
    print (element.replace(element, element * large,1))
    return 0
		
def printElementName(name,element, large):
    s = element.replace(element, element * large,1)
    name = ' '+name+' '
    t1 = len(name)
    t2 = len(s)

    position = int( t2/2 - t1/2 -1)

    s = s[:position] + name + s[position+t1:]
    print (s)

    return 0

def latex(fileName, projects,cifras,modo):
    header = """
\\documentclass[preprint,landscape,12pt]{elsarticle}
\\usepackage[margin=0.5in]{geometry}
\\usepackage{color}
\\usepackage[version=3]{mhchem} % Formula subscripts using \\ce{}
\\usepackage[T1]{fontenc}       % Use modern font encodings
\\usepackage{subcaption}
\\usepackage{latexsym}
\\usepackage{amssymb,amsmath}
\\usepackage{color}
\\usepackage{lineno,hyperref}
\\modulolinenumbers[5]
\\usepackage{adjustbox}
\\newcommand{\\hilight}[1]{\\colorbox{yellow}{#1}}
\\usepackage{rotating}
\\usepackage{multirow}
\\usepackage{commath}
\\usepackage{booktabs,caption}
\\usepackage{mathptmx}      % use Times fonts if available on your TeX system
\\usepackage{threeparttable}

\\journal{JOURNAL}
\\begin{document}
	\\begin{table}
"""
    header += '		\\caption{ Tabla '+ modo+'}'
    header += """
		\\centering
		\\footnotesize
		\\begin{tabular}{lrrrrrrrr}
			\\hline
			\\textbf{Density}    & $\\varepsilon_{_{\\mathrm{H}}}$	& $\\varepsilon_{_{\\mathrm{L}}}$  & $\\varepsilon_{_{\\mathrm{S}}}$& HL$Gap$ & $J(I)$ & $J(A)$ & $J(\\mathrm{HL})$  & \\textbf{$\\left|\\Delta\\,\\mathrm{SL}\\right|$}  \\\\
			\\textbf{Functional} &   &  &     &   &  &  &  &  \\\\
			\\hline \\hline \n
"""

    footer = """
	 		\\hline
		\\end{tabular}
		"""
    footer += '	\\label{tab:'+ modo+'}'
    footer += """
	\\end{table}
\\end{document}
\\endinput

"""

    #print('Tex File:',fileName)
    with open(fileName,'w') as f:
	f.writelines(header) 
	if modo == "hartree":
	    for project in projects:
		aux = ' & '.join(project.valuesHartree(cifras))
		aux += '\\\\\n'
		f.write(aux)
	elif modo=="eV":
	    for project in projects:
		aux = ' & '.join(project.valuesEV(cifras))
		aux += '\\\\\n'
		f.write(aux)
	elif modo=="kcal/mol":
	    for project in projects:
		aux = ' & '.join(project.valuesKcalMol(cifras))
		aux += '\\\\\n'
		f.write(aux)
	elif modo=="kJ/mol":
	    for project in projects:
		aux = ' & '.join(project.valuesKJMol(cifras))
		aux += '\\\\\n'
		f.write(aux)		
	f.writelines(footer) 
	f.close()

    return 0


def csv(fileName, projects,cifras,modo):

    header = ' ; '.join(projects[0].labels())
    header += '\n'
    #print('Csv File:',fileName)
    with open(fileName,'w') as f:
	f.writelines(header) 
	if modo == "hartree":
	    for project in projects:
		aux = ' ; '.join(project.valuesHartree(cifras))
		aux += '\n'
		f.write(aux)
	elif modo=="eV":
	    for project in projects:
		aux = ' ; '.join(project.valuesEV(cifras))
		aux += '\n'
		f.write(aux)
	elif modo=="kcal/mol":
	    for project in projects:
		aux = ' ; '.join(project.valuesKcalMol(cifras))
		aux += '\n'
		f.write(aux)
	elif modo=="kJ/mol":
	    for project in projects:
		aux = ' ; '.join(project.valuesKJMol(cifras))
		aux += '\n'
		f.write(aux)
	f.close()

    return 0
