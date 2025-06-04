import pytest
from Prova_Escrita_05 import llibres_per_categoria, esta_disponible, usuari_te_prestecs, dies_prestec_total

# Dades de prova
biblioteca = [
    {
        "llibre": "El Quixot",
        "autor": "Cervantes",
        "categoria": "novel·la",
        "prestecs": [
            {"usuari": "Joan", "dies": 15, "retornat": True},
            {"usuari": "Maria", "dies": 20, "retornat": True},
            {"usuari": "Pere", "dies": 12, "retornat": True}
        ]
    },
    {
        "llibre": "1984",
        "autor": "Orwell",
        "categoria": "ciència-ficció",
        "prestecs": [
            {"usuari": "Pere", "dies": 10, "retornat": True},
            {"usuari": "Anna", "dies": 25, "retornat": True},
            {"usuari": "Marta", "dies": 18, "retornat": False}
        ]
    },
    {
        "llibre": "El Senyor dels Anells",
        "autor": "Tolkien",
        "categoria": "fantasia",
        "prestecs": [
            {"usuari": "Maria", "dies": 30, "retornat": True},
            {"usuari": "Joan", "dies": 22, "retornat": True},
            {"usuari": "Pere", "dies": 15, "retornat": False}
        ]
    },
    {
        "llibre": "Crim i Càstig",
        "autor": "Dostoievski",
        "categoria": "novel·la",
        "prestecs": [
            {"usuari": "Anna", "dies": 28, "retornat": True},
            {"usuari": "Marta", "dies": 14, "retornat": True},
            {"usuari": "Joan", "dies": 21, "retornat": True}
        ]
    }
]

# Test llibres_per_categoria
@pytest.mark.parametrize("categoria, esperat", [
    ("novel·la", ["El Quixot", "Crim i Càstig"]),
    ("ciència-ficció", ["1984"]),
    ("fantasia", ["El Senyor dels Anells"]),
    ("poesia", []),
])
def test_llibres_per_categoria(categoria, esperat):
    assert llibres_per_categoria(biblioteca, categoria) == esperat

# Test esta_disponible
@pytest.mark.parametrize("llibre, esperat", [
    ("El Senyor dels Anells", False),
    ("El Quixot", True),
    ("1984", False),
    ("Crim i Càstig", True),
])
def test_esta_disponible(llibre, esperat):
    assert esta_disponible(biblioteca, llibre) == esperat

# Test usuari_te_prestecs
@pytest.mark.parametrize("usuari, esperat", [
    ("Pere", True),
    ("Joan", False),
    ("Maria", False),
    ("Anna", False),
])
def test_usuari_te_prestecs(usuari, esperat):
    assert usuari_te_prestecs(biblioteca, usuari) == esperat

# Test dies_prestec_total
@pytest.mark.parametrize("llibre, esperat", [
    ("El Senyor dels Anells", 67),
    ("1984", 53),
    ("El Quixot", 47),
    ("Crim i Càstig", 63),
])
def test_dies_prestec_total(llibre, esperat):
    assert dies_prestec_total(biblioteca, llibre) == esperat
