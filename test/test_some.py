import unittest

from parser_interface import ParserInterface


class TestSome(unittest.TestCase):

    def test_query1(self):
        p = ParserInterface("../examples/TestSuite/some1.txt")
        self.assertEqual(0.8, p.solve(), "TestSome")

    def test_query2(self):
        p = ParserInterface("../examples/TestSuite/some2.txt")
        self.assertEqual(0.8, p.solve(), "TestSome")

    def test_query3(self):
        p = ParserInterface("../examples/TestSuite/some3.txt")
        self.assertEqual(0.6, p.solve(), "TestSome")

    def test_query4(self):
        p = ParserInterface("../examples/TestSuite/some4.txt")
        self.assertEqual(0.8, p.solve(), "TestSome")

    def test_bare_filler_is_parsed_as_concept(self):
        # (some R *top*) with a bare filler: the fast parser must yield a
        # TruthConcept, not an AtomicConcept named "*top*" (which left the
        # filler's degree unconstrained in the MILP; impliesRole1 then had a
        # true optimum of 0.0 under Gurobi).
        from fuzzy_dl_owl2.fuzzydl.knowledge_base import KnowledgeBase
        from fuzzy_dl_owl2.fuzzydl.parser import dl_parser_fast
        from fuzzy_dl_owl2.fuzzydl.parser.dl_parser_clean import DLParser
        from fuzzy_dl_owl2.fuzzydl.util.constants import ConceptType

        DLParser.kb = KnowledgeBase()
        DLParser.queries_list = []
        # (some R *bottom*) is simplified to *bottom* itself, hence no filler.
        cases = (
            ("(some R *top*)", ConceptType.SOME, ConceptType.TOP),
            ("(some R *bottom*)", ConceptType.BOTTOM, None),
            ("(some R C)", ConceptType.SOME, ConceptType.ATOMIC),
        )
        for text, expected_type, expected_filler in cases:
            with self.subTest(text=text):
                parser = dl_parser_fast._Parser(dl_parser_fast._tokenize_best(text))
                concept = parser.parse_concept()
                self.assertEqual(expected_type, concept.type, text)
                if expected_filler is not None:
                    self.assertEqual(expected_filler, concept.curr_concept.type, text)


if __name__ == "__main__":
    unittest.main()
