import os
import unittest

from rdflib import OWL, RDF, RDFS, Graph, Namespace

from fuzzy_dl_owl2.fuzzydl.fuzzydl_to_owl2 import FuzzydlToOwl2
from fuzzy_dl_owl2.fuzzyowl2.fuzzyowl2_to_fuzzydl import FuzzyOwl2ToFuzzyDL
# from fuzzy_dl_owl2.fuzzydl.parser.dl_parser import DLParser
from fuzzy_dl_owl2.fuzzydl.parser import DLParserFast as DLParser


class TestConversionRoundtrip(unittest.TestCase):
    """Round-trip tests: DL → OWL2 → DL with content verification."""

    BASE = Namespace("http://www.semanticweb.org/ontologies/fuzzydl_ontology#")
    CLASS_NS = Namespace("http://www.semanticweb.org/ontologies/fuzzydl_ontology/class#")
    IND_NS = Namespace("http://www.semanticweb.org/ontologies/fuzzydl_ontology/individual#")
    OP_NS = Namespace("http://www.semanticweb.org/ontologies/fuzzydl_ontology/object-property#")

    def _run_roundtrip(self, dl_source: str, base_name: str) -> tuple[str, str]:
        self.assertTrue(os.path.exists(dl_source), f"Source missing: {dl_source}")
        out_dir = os.path.join(os.path.dirname(__file__), "results")
        os.makedirs(out_dir, exist_ok=True)
        owl_file = os.path.join(out_dir, f"rt_{base_name}.owl")
        dl_file = os.path.join(out_dir, f"rt_{base_name}.txt")
        for f in (owl_file, dl_file):
            if os.path.exists(f):
                os.remove(f)

        c1 = FuzzydlToOwl2(dl_source, owl_file)
        c1.run()
        self.assertTrue(os.path.exists(owl_file), f"OWL missing: {owl_file}")

        c2 = FuzzyOwl2ToFuzzyDL(owl_file, dl_file)
        c2.translate_owl2ontology()
        c1.ontology._world.close()
        c2.ontology._world.close()
        self.assertTrue(os.path.exists(dl_file), f"DL missing: {dl_file}")
        return owl_file, dl_file

    def _verify_owl(self, owl_path: str, expected_classes: list[str]) -> None:
        g = Graph()
        g.parse(owl_path)
        for cls in expected_classes:
            self.assertIn(
                (self.CLASS_NS[cls], RDF.type, OWL.Class),
                g,
                f"Class {cls} not in OWL output",
            )

    def _verify_dl(self, dl_path: str, expected_concepts: list[str]) -> None:
        kb, queries = DLParser.get_kb(dl_path)
        self.assertIsNotNone(kb, f"Failed to parse DL: {dl_path}")
        has_content = len(kb.assertions) > 0 or len(kb.atomic_concepts) > 0
        self.assertTrue(has_content, "Round-trip KB empty")
        for concept in expected_concepts:
            self.assertIn(
                concept,
                kb.atomic_concepts,
                f"Concept {concept} missing in round-trip KB",
            )

    def test_concepts_and_individuals(self):
        owl, dl = self._run_roundtrip(
            "../examples/conversion_dl/concepts_and_individuals.txt",
            "concepts_and_individuals",
        )
        self._verify_owl(owl, ["Human", "Animal", "Plant", "Mammal"])
        self._verify_dl(dl, ["Human", "Animal", "Plant"])

    def test_roles(self):
        owl, dl = self._run_roundtrip("../examples/conversion_dl/roles.txt", "roles")
        self._verify_owl(owl, ["A", "B"])
        self._verify_dl(dl, ["A", "B"])

    def test_datatypes(self):
        owl, dl = self._run_roundtrip("../examples/conversion_dl/datatypes.txt", "datatypes")
        self._verify_owl(owl, ["Person"])
        self._verify_dl(dl, ["Person"])


if __name__ == "__main__":
    unittest.main()