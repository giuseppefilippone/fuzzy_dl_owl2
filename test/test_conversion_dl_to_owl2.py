import os
import unittest

from rdflib import OWL, RDF, RDFS, Graph, Namespace

from fuzzy_dl_owl2.fuzzydl.fuzzydl_to_owl2 import FuzzydlToOwl2


class TestConversionDlToOwl2(unittest.TestCase):
    """Tests converting FuzzyDL text files to OWL2 RDF/XML, verifying output with rdflib."""

    BASE = Namespace("http://www.semanticweb.org/ontologies/fuzzydl_ontology#")
    CLASS_NS = Namespace("http://www.semanticweb.org/ontologies/fuzzydl_ontology/class#")
    IND_NS = Namespace("http://www.semanticweb.org/ontologies/fuzzydl_ontology/individual#")
    OP_NS = Namespace("http://www.semanticweb.org/ontologies/fuzzydl_ontology/object-property#")

    def _convert(self, dl_path: str) -> str:
        """Run DL→OWL2 and return the output file path."""
        self.assertTrue(os.path.exists(dl_path), f"Input missing: {dl_path}")
        out_name = os.path.basename(dl_path).replace(".txt", ".owl")
        out_dir = os.path.join(os.path.dirname(__file__), "results")
        os.makedirs(out_dir, exist_ok=True)
        out_path = os.path.join(out_dir, f"conv_{out_name}")
        if os.path.exists(out_path):
            os.remove(out_path)

        converter = FuzzydlToOwl2(dl_path, out_path)
        converter.run()
        converter.ontology._world.close()

        self.assertTrue(os.path.exists(out_path), f"OWL output missing: {out_path}")
        return out_path

    def _load_graph(self, owl_path: str) -> Graph:
        g = Graph()
        g.parse(owl_path)
        self.assertGreater(len(g), 0, "Parsed RDF graph is empty")
        return g

    def _class_declared(self, g: Graph, name: str) -> bool:
        return (self.CLASS_NS[name], RDF.type, OWL.Class) in g

    def _individual_declared(self, g: Graph, name: str) -> bool:
        return (self.IND_NS[name], RDF.type, OWL.NamedIndividual) in g

    def _subclass(self, g: Graph, sub: str, sup: str) -> bool:
        return (self.CLASS_NS[sub], RDFS.subClassOf, self.CLASS_NS[sup]) in g

    def _disjoint(self, g: Graph, c1: str, c2: str) -> bool:
        return (self.CLASS_NS[c1], OWL.disjointWith, self.CLASS_NS[c2]) in g

    def test_concepts_and_individuals(self):
        path = self._convert("../examples/conversion_dl/concepts_and_individuals.txt")
        g = self._load_graph(path)

        for cls in ("Human", "Animal", "Plant", "Mammal"):
            self.assertTrue(self._class_declared(g, cls), f"Class {cls} not declared")

        self.assertTrue(self._subclass(g, "Mammal", "Human"), "Mammal subclass of Human missing")
        self.assertTrue(self._disjoint(g, "Human", "Plant"), "Human disjoint Plant missing")

        for ind in ("alice", "bob"):
            self.assertTrue(self._individual_declared(g, ind), f"Individual {ind} not declared")

        self.assertTrue(
            (self.IND_NS["alice"], RDF.type, self.CLASS_NS["Human"]) in g,
            "alice type Human missing",
        )
        self.assertTrue(
            (self.IND_NS["bob"], RDF.type, self.CLASS_NS["Animal"]) in g,
            "bob type Animal missing",
        )

        self.assertTrue(
            (self.IND_NS["alice"], self.OP_NS["knows"], self.IND_NS["bob"]) in g,
            "alice knows bob missing",
        )

    def test_datatypes(self):
        path = self._convert("../examples/conversion_dl/datatypes.txt")
        g = self._load_graph(path)
        self.assertTrue(self._class_declared(g, "Person"), "Person class missing")
        self.assertTrue(self._individual_declared(g, "john"), "john individual missing")

    def test_roles(self):
        path = self._convert("../examples/conversion_dl/roles.txt")
        g = self._load_graph(path)
        self.assertTrue(self._class_declared(g, "A"), "A class missing")
        self.assertTrue(self._class_declared(g, "B"), "B class missing")


if __name__ == "__main__":
    unittest.main()