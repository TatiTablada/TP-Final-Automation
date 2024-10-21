import unittest
import requests

class TestPokeBerry(unittest.TestCase):

    def setUp(self):
        self.url = "https://pokeapi.co/api/v2/"

    def test_1(self):
        r = requests.get(self.url+'berry/1')
        data = r.json()
        self.assertEqual(data['firmness']['name'], 'soft', "El nombre de firmness no es soft'")
        self.assertEqual(data['size'], 20, "El tamaño no es 20")
        self.assertEqual(data['soil_dryness'], 15, "El valor de soil_dryness no es 15")
        self.assertEqual(r.status_code, 200)


    def test_2(self):
        r = requests.get(self.url + 'berry/2')
        data = r.json() 
        self.assertEqual(data['firmness']['name'], 'super-hard', "El nombre de firmness no es 'super-hard'")
        self.assertGreater(data['size'], 20, "El tamaño no es mayor que 20")
        self.assertEqual(data['soil_dryness'], 15, "El valor de soil_dryness no es 15")
        self.assertEqual(r.status_code, 200)


    def test_3(self):
        r = requests.get(self.url + 'pokemon/pikachu')
        data = r.json() 
        base_experience = data['base_experience']
        self.assertGreater(base_experience, 10, "La experiencia base es menor o igual a 10")
        self.assertLess(base_experience, 1000, "La experiencia base es mayor o igual a 1000")
        tipo = data['types'][0]['type']['name']
        self.assertEqual(tipo,'electric',"El tipo de Pikachu no es 'electric'")
        self.assertEqual(r.status_code, 200)

