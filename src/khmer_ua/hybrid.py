"""Deprecated import path for the deterministic Khmer rule engine.

The former provider-voting ensemble has been removed. This compatibility
module contains no external backend, neural inference, or candidate voting.
"""
from .rule_engine import HybridKhmerEngine, RuleBasedKhmerEngine, create_hybrid_engine

__all__ = ["HybridKhmerEngine", "RuleBasedKhmerEngine", "create_hybrid_engine"]
