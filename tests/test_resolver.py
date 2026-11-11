"""Unit tests for cross-document-entity-resolver."""
import unittest
from cross_document_entity_resolver.resolver import EntityResolver

class TestEntityResolver(unittest.TestCase):
    def setUp(self):
        self.resolver = EntityResolver()

    def test_canonical_registration_and_lookup(self):
        self.resolver.register_canonical_entity("e1", "PostgreSQL", ["Postgres", "pgsql"])
        e = self.resolver.resolve_mention("postgres")
        self.assertIsNotNone(e)
        self.assertEqual(e.canonical_id, "e1")
        self.assertEqual(e.canonical_name, "PostgreSQL")

    def test_case_and_symbol_insensitivity(self):
        self.resolver.register_canonical_entity("e2", "C++", ["cpp", "c-plus-plus"])
        self.assertIsNotNone(self.resolver.resolve_mention("C++"))
        self.assertIsNotNone(self.resolver.resolve_mention("cpp"))
