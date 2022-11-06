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

def count_first_names(d, name):
    total=0
    for key in d:
        if d[key]==name:
            total+=1
    print("There are", total, name, "'s in this dictionary")

count_first_names(github_names, "Julia")
