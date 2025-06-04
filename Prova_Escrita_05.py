def llibres_per_categoria(biblioteca, categoria):
    return [llibre["llibre"] for llibre in biblioteca if llibre["categoria"] == categoria]

def esta_disponible(biblioteca, titol):
    for llibre in biblioteca:
        if llibre["llibre"] == titol:
            return all(prestec["retornat"] for prestec in llibre["prestecs"])
    return False

def usuari_te_prestecs(biblioteca, nom_usuari):
    for llibre in biblioteca:
        for prestec in llibre["prestecs"]:
            if prestec["usuari"] == nom_usuari and not prestec["retornat"]:
                return True
    return False

def dies_prestec_total(biblioteca, titol):
    for llibre in biblioteca:
        if llibre["llibre"] == titol:
            return sum(prestec["dies"] for prestec in llibre["prestecs"])
    return 0
