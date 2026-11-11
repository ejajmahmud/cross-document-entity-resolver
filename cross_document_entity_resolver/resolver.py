"""Core Entity Resolver implementation."""
import re
from dataclasses import dataclass
from typing import Dict, List, Set

@dataclass
class ResolvedEntity:
    canonical_id: str
    canonical_name: str
    aliases: Set[str]
    document_mentions: int

class EntityResolver:
    """Merges cross-document entity aliases into unified canonical knowledge graph nodes."""
    
    def __init__(self):
        self.alias_to_canonical: Dict[str, str] = {}
        self.entities: Dict[str, ResolvedEntity] = {}

    def _normalize_name(self, name: str) -> str:
        clean = re.sub(r"[^a-zA-Z0-9\s]", "", name.lower())
        return " ".join(clean.split())

    def register_canonical_entity(self, canonical_id: str, canonical_name: str, initial_aliases: List[str] = None) -> None:
        aliases = set(initial_aliases or [])
        aliases.add(canonical_name)
        self.entities[canonical_id] = ResolvedEntity(
            canonical_id=canonical_id,
            canonical_name=canonical_name,
            aliases=aliases,
            document_mentions=1
        )
        for a in aliases:
            self.alias_to_canonical[self._normalize_name(a)] = canonical_id

    def resolve_mention(self, mention_text: str) -> Optional[ResolvedEntity]:
        norm = self._normalize_name(mention_text)
        cid = self.alias_to_canonical.get(norm)
        if cid and cid in self.entities:
            entity = self.entities[cid]
            entity.document_mentions += 1
            return entity
        return None

    def add_alias(self, canonical_id: str, new_alias: str) -> bool:
        if canonical_id in self.entities:
            self.entities[canonical_id].aliases.add(new_alias)
            self.alias_to_canonical[self._normalize_name(new_alias)] = canonical_id
            return True
        return False
