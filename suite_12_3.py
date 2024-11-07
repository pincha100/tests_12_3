import unittest
from tests_12_2 import RunnerTest, TournamentTest  # Импортируем классы тестов

# Создаем TestSuite и добавляем тестовые классы
suite = unittest.TestSuite()
suite.addTests(unittest.TestLoader().loadTestsFromTestCase(RunnerTest))
suite.addTests(unittest.TestLoader().loadTestsFromTestCase(TournamentTest))

# Создаем и запускаем TextTestRunner
runner = unittest.TextTestRunner(verbosity=2)
runner.run(suite)
