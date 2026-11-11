"""CLI for cross-document-entity-resolver."""
import sys
import argparse
from .resolver import EntityResolver

def main():
    parser = argparse.ArgumentParser(description="Cross-Document Entity Resolver CLI")
    parser.add_argument("--demo", action="store_true", help="Resolve entity aliases across documents")
    args = parser.parse_args()

    if args.demo:
        resolver = EntityResolver()
        resolver.register_canonical_entity("ent_gcp_bq", "BigQuery", ["BQ", "Google BigQuery", "GCP BigQuery"])
        
        m1 = resolver.resolve_mention("Google BigQuery")
        m2 = resolver.resolve_mention("bq")
        print(f"Mention 1 resolved to: {m1.canonical_name} (ID: {m1.canonical_id})")
        print(f"Mention 2 resolved to: {m2.canonical_name} (Total mentions: {m2.document_mentions})")
    else:
        parser.print_help()
    sys.exit(0)

if __name__ == "__main__":
    main()
