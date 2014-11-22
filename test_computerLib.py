import unittest
import computerLib as c
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from slmsDbLib import Computer



class TestQuery(unittest.TestCase):
    def setUp(self):
        self.engine = create_engine('sqlite:///slms.database')
        self.session = Session(engine)
        Base.metadata.create_all(self.engine)
        self.Computer = Computer('ABC123', 'Test computer')
        self.session.add(self.Computer)
        self.session.commit()

    def tearDown(self):
        Base.metadata.drop_all(Computer.engine)

    def test_query_computer(self):
        expected = [self.Computer]
        result = self.session.query(Computer).all()
        self.assertEqual(result, expected)
        
if __name__ == '__main':
    unittest.main()