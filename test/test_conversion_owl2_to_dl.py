import os
import unittest

from rdflib import Graph

from fuzzy_dl_owl2.fuzzyowl2.fuzzyowl2_to_fuzzydl import FuzzyOwl2ToFuzzyDL
# from fuzzy_dl_owl2.fuzzydl.parser.dl_parser import DLParser
from fuzzy_dl_owl2.fuzzydl.parser import DLParserFast as DLParser


class TestConversionOwl2ToDl(unittest.TestCase):
    """Tests converting OWL2 Turtle files to FuzzyDL text via RDF/XML."""

    def _turtle_to_rdfxml(self, ttl_path: str) -> str:
        """Serialize Turtle to RDF/XML in the results directory."""
        self.assertTrue(os.path.exists(ttl_path), f"Turtle input missing: {ttl_path}")
        g = Graph()
        g.parse(ttl_path, format="turtle")
        out_name = os.path.basename(ttl_path).replace(".ttl", ".owl")
        out_dir = os.path.join(os.path.dirname(__file__), "results")
        os.makedirs(out_dir, exist_ok=True)
        out_path = os.path.join(out_dir, f"conv_{out_name}")
        g.serialize(out_path, format="xml")
        self.assertTrue(os.path.exists(out_path), f"RDF/XML not written: {out_path}")
        return out_path

    def _convert(self, ttl_path: str) -> str:
        """Convert Turtle→RDF/XML→DL and return the DL file path."""
        owl_path = self._turtle_to_rdfxml(ttl_path)
        out_name = os.path.basename(ttl_path).replace(".ttl", ".txt")
        out_dir = os.path.join(os.path.dirname(__file__), "results")
        out_path = os.path.join(out_dir, f"conv_{out_name}")
        if os.path.exists(out_path):
            os.remove(out_path)

        converter = FuzzyOwl2ToFuzzyDL(owl_path, out_path)
        converter.translate_owl2ontology()
        converter.ontology._world.close()

        self.assertTrue(os.path.exists(out_path), f"DL output missing: {out_path}")
        self.assertGreater(os.path.getsize(out_path), 0, f"DL output empty: {out_path}")
        return out_path

    def _dl_text(self, path: str) -> str:
        with open(path, "r") as f:
            return f.read()

    def _dl_parses(self, dl_path: str) -> None:
        kb, queries = DLParser.get_kb(dl_path)
        self.assertIsNotNone(kb, "DLParser failed to parse generated DL")
        has_content = (
            len(kb.assertions) > 0
            or len(kb.atomic_concepts) > 0
            or len(kb.roles_with_parents) > 0
            or len(kb.reflexive_roles) > 0
            or len(kb.symmetric_roles) > 0
            or len(kb.transitive_roles) > 0
            or len(kb.inverse_roles) > 0
        )
        self.assertTrue(has_content, "Parsed KB has no assertions, concepts, or roles")

    def test_concepts(self):
        path = self._convert("../examples/conversion_owl/concepts.ttl")
        text = self._dl_text(path)
        self.assertIn("Animal", text, "Animal concept missing")
        self.assertIn("Plant", text, "Plant concept missing")
        self.assertIn("Person", text, "Person concept missing")
        self.assertIn("disjoint", text, "disjoint missing")
        self._dl_parses(path)

    def test_roles(self):
        path = self._convert("../examples/conversion_owl/roles.ttl")
        text = self._dl_text(path)
        self.assertIn("hasFriend", text, "hasFriend role missing")
        self.assertIn("hasAncestor", text, "hasAncestor role missing")
        self.assertIn("hasParent", text, "hasParent role missing")
        self.assertIn("hasChild", text, "hasChild role missing")
        self._dl_parses(path)

    def test_individuals(self):
        path = self._convert("../examples/conversion_owl/individuals.ttl")
        text = self._dl_text(path)
        self.assertIn("Alice", text, "Alice individual missing")
        self.assertIn("Bob", text, "Bob individual missing")
        self.assertIn("Person", text, "Person concept missing")
        self._dl_parses(path)

    def test_datatypes(self):
        path = self._convert("../examples/conversion_owl/datatypes.ttl")
        text = self._dl_text(path)
        self.assertIn("age", text, "age data property missing")
        self.assertIn("name", text, "name data property missing")
        self.assertIn("Person", text, "Person concept missing")
        self._dl_parses(path)


if __name__ == "__main__":
    unittest.main()