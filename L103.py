#the authors' name are: Holly, Haley and Anna

github_names = {"Brown" : "Cody",
"Bub" : "Julia",
"Doherty" : "Catherine",
"Dunn" : "Margaret",
"Greene" : "Haley",
"Guthrie Beckstrom" : "Isabela",
"Hongell" : "Danielle",
"Hurley" : "Camryn",
"Kevin" : "Ellen",
"Kieft" : "Brenna",
"Miloserny" : "Amanda",
"Nyhuis" : "Kaylen",
"Reger" : "Cadyn",
"Rusch" : "Emily",
"Salazar" : "Britney",
"Schutz": "Julia",
"Shadid" : "Christina",
"Skrip" : "Holly",
"Sullivan" : "Anna",
"Verstraete": "Adrianne",
"Wardlow" : "Sarah"}

def first_initial(d, letter):
    total = 0
    vals = d.values()
    list = sorted(vals)
    for item in list:
        if item[0] == letter:
            total += 1
    print (total, "names have this first initial.")

def last_initial(d, letter):
    total = 0
    for key in d:
        if key[0] == letter:
            total += 1
    print (total, "names have this last initial.")

first_initial(github_names, "C")

last_initial(github_names, "K")
