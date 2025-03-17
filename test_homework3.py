# Artur Kazukevich
# Date: 30/05/2024
# Description: Homework 3 Test Suit
# Grodno IT Academy Python 3.9.5

import unittest
import Homework3 as homework

class TestHomework2(unittest.TestCase):
    #homework 2 testing suite
    def test_pairs(self):
        self.assertEqual(homework.pairs(''), 0,msg="Expected 0 pairs with empty string")
        self.assertEqual(homework.pairs('1'), 0)
        self.assertEqual(homework.pairs('1 1'), 1)
        self.assertEqual(homework.pairs('1 1 1'), 3)
        self.assertEqual(homework.pairs('1 1 1 1'), 6)
        self.assertEqual(homework.pairs('1 2 1 1 1'), 6)
        self.assertEqual(homework.pairs('1 2 1 2 1 1'), 7)

    def test_uniques(self):
        self.assertEqual(homework.uniques([]),[])
        self.assertEqual(homework.uniques(["1","2"]),["1","2"])
        self.assertEqual(homework.uniques(["1","2","1"]),["2"])
        self.assertEqual(homework.uniques(["1","2","1", "1"]),["2"])
        self.assertEqual(homework.uniques(["1","2","1", "1", "2"]),[])
        self.assertEqual(homework.uniques(["1","2","3"]),["1","2","3"])
        self.assertEqual(homework.uniques(["1","2","3", "1"]),["2","3"])

    def test_ordered_list(self):
        self.assertEqual(homework.ordered_list([-1,0,1,2]),[-1,1,2,0])
        self.assertEqual(homework.ordered_list([-1,2,0,1,0,2]),[-1,2,1,2,0,0])
        self.assertEqual(homework.ordered_list([0,-1,0,1,2]),[-1,1,2,0,0])
        self.assertEqual(homework.ordered_list([-1,3,0,1,2]),[-1,3,1,2,0])
        self.assertEqual(homework.ordered_list([-1,0,1,5,2]),[-1,1,5,2,0])

    def test_tuple_to_list(self):
        self.assertEqual(homework.tuple_to_list(('a', 'b', 'c')),['a', 'b', 'c'])
        self.assertEqual(homework.tuple_to_list(('b', 'c')),['b', 'c'])
        self.assertEqual(homework.tuple_to_list(('a',)),['a'])

    def test_euclid(self):
        self.assertEqual(homework.euclid(150,304),2)
        self.assertEqual(homework.euclid(1000,10),10)
        self.assertEqual(homework.euclid(13,21),1)
        self.assertEqual(homework.euclid(0,21),21)

    def test_cities(self):
        self.assertEqual(homework.cities('2\nRussia Moscow Petersburg Novgorod Kaluga\nUkraine Kiev Donetsk Odessa\n3\nOdessa\nMoscow\nNovgorod'),'Ukraine\nRussia\nRussia')
        self.assertEqual(homework.cities('2\nRussia Moscow Petersburg Novgorod Kaluga\nUkraine Kiev Donetsk Odessa\n3\nOdessa\nDonetsk\nNovgorod'),'Ukraine\nUkraine\nRussia')
        self.assertEqual(homework.cities('2\nBelarus Minsk Brest Grodno Vitebsk Gomel Mogilev\nFrance Paris Brest Marselle\n3\nBrest\nParis\nMinsk'),'Belarus France\nFrance\nBelarus')
        self.assertEqual(homework.cities('2\nFrance Paris Brest Marselle\nBelarus Minsk Brest Grodno Vitebsk Gomel Mogilev\n3\nBrest\nParis\nMinsk'),'France Belarus\nFrance\nBelarus')

    def test_languages(self):
        for line in homework.languages('3\n2\nRussian\nEnglish\n3\nRussian\nBelarusian\nEnglish\n3\nRussian\nItalian\nFrench').split('\n'):
            self.assertIn(line,'1\nRussian\n5\nRussian\nFrench\nItalian\nEnglish\nBelarusian'.split('\n'))
        for line in homework.languages('3\n2\nRussian\nEnglish\n3\nRussian\nBelarusian\nEnglish\n3\nRussian\nItalian\nEnglish').split('\n'):
            self.assertIn(line,'2\nRussian\nEnglish\n4\nRussian\nItalian\nEnglish\nBelarusian'.split('\n'))

    def test_list_gen(self):
        self.assertEqual(homework.list_gen(['x','y'], ['y','z','v']), ['xy', 'xz', 'xv', 'yy', 'yz', 'yv'])
        self.assertEqual(homework.list_gen(['x','y','z'], ['y','z','v']), ['xy', 'xz', 'xv', 'yy', 'yz', 'yv', 'zy', 'zz', 'zv'])
        self.assertEqual(homework.list_gen([], ['y','z','v']), [])
        self.assertEqual(homework.list_gen([str(i) for i in range(1,5)], ['x']), ['1x', '2x', '3x', '4x'])

    def test_dict_gen(self):
        self.assertEqual(homework.dict_gen(20),{1: 1, 2: 8, 3: 27, 4: 64, 5: 125, 6: 216, 7: 343, 8: 512, 9: 729, 10: 1000, 11: 1331, 12: 1728, 13: 2197, 14: 2744, 15: 3375, 16: 4096, 17: 4913, 18: 5832, 19: 6859, 20: 8000})
        self.assertEqual(homework.dict_gen(2),{1: 1, 2: 8})

    def test_multiplication_table(self):
        gens = [homework.multiplication_table(0), homework.multiplication_table(1), homework.multiplication_table(2), homework.multiplication_table(3)]
        sample_gen = (_ for _ in range(3))
        answers = ["0", '0 0\n0 1', '0 0 0\n0 1 2\n0 2 4', '0 0 0 0\n0 1 2 3\n0 2 4 6\n0 3 6 9']
        for index in range(len(gens)):
            output = ""
            gen = gens[index]
            for i in gen:
                output += i + "\n"
            else:
                output = output[:-1]
            self.assertEqual(output,answers[index])
            self.assertEqual(type(gen), type(sample_gen))

if __name__ == '__main__':
    unittest.main(verbosity=2)
