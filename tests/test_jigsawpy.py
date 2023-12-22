import unittest
import os
import tempfile

from .case_0_ import case_0_
from .case_1_ import case_1_
from .case_2_ import case_2_
from .case_3_ import case_3_
from .case_4_ import case_4_
from .case_5_ import case_5_
from .case_6_ import case_6_
from .case_7_ import case_7_
from .case_8_ import case_8_


class TestAllCases(unittest.TestCase):
    """
    A unit-test class for testing all cases in example.py 

    """    
    
    
    def example(self, IDnumber=0):

    #--------------- delegate to the individual example cases...
        src_path = os.path.join(
            os.path.abspath(
                os.path.dirname(__file__)), os.pardir, "files")
        
        dst_path = self.dst_path
        
        if   (IDnumber == +0):
            case_0_(src_path, dst_path)

        elif (IDnumber == +1):
            case_1_(src_path, dst_path)

        elif (IDnumber == +2):
            case_2_(src_path, dst_path)

        elif (IDnumber == +3):
            case_3_(src_path, dst_path)

        elif (IDnumber == +4):
            case_4_(src_path, dst_path)

        elif (IDnumber == +5):
            case_5_(src_path, dst_path)

        elif (IDnumber == +6):
            case_6_(src_path, dst_path)

        elif (IDnumber == +7):
            case_7_(src_path, dst_path)

        elif (IDnumber == +8):
            case_8_(src_path, dst_path)

        elif (IDnumber == -1):
            for i in range(9): self.example(i)

        return    
    
    def setUp(self):
        # Initialize a target and surface for testing
        self.temp_dir = tempfile.TemporaryDirectory()
        self.dst_path =  self.temp_dir.name
    
        return
    
    def tearDown(self):
        # Clean up temporary directory
        self.temp_dir.cleanup() 
        return

    def test_all_cases(self):
        self.example(IDnumber=-1)
        expected_files = [
                "airfoil.jig", "airfoil.msh", "bunny.log", "case_0a.vtk", "case_0c.vtk",
                "case_1b.vtk", "case_2b.vtk", "case_3b.vtk", "case_4a.vtk", "case_5a.vtk",
                "case_6a.vtk", "case_6c.vtk", "case_7b.vtk", "case_8b.vtk", "lakes.log",
                "piece.jig", "piece.msh", "airfoil.log", "bunny.jig", "bunny.msh",
                "case_0b.vtk", "case_1a.vtk", "case_2a.vtk", "case_3a.vtk", "case_3c.vtk",
                "case_4b.vtk", "case_5b.vtk", "case_6b.vtk", "case_7a.vtk", "case_8a.vtk",
                "lakes.jig", "lakes.msh", "piece.log", "spacing.msh"
            ]

        for file in expected_files:
            self.assertTrue(os.path.exists(os.path.join(self.dst_path,file)))
        
        return
    

if __name__ == '__main__':
    unittest.main()    