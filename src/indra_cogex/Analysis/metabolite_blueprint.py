"""Metabolite-centric analysis."""

from typing import Dict, List, Mapping, Tuple
import pandas as pd
from indra.databases import chebi_client
from indra_cogex.client.enrichment.mla import (
    EXAMPLE_CHEBI_CURIES,
    metabolomics_explanation,
    metabolomics_ora,
)


def discrete_analysis(client, metabolites: str, method: str, alpha: float, keep_insignificant: bool,
                          minimum_evidence_count: int, minimum_belief: float):
    """Perform discrete metabolite set analysis using metabolomics over-representation analysis.

    client: The client object for making API calls
    metabolites (str): A string of metabolite identifiers
    method (str): The statistical method for multiple testing correction
    alpha (float): The significance level
    keep_insignificant (bool): Whether to keep statistically insignificant results
    minimum_evidence_count (int): Minimum number of evidence required for analysis
    minimum_belief (float): Minimum belief score for analysis

    Returns:
    dict: A dictionary containing results from the analysis"""
    metabolite_chebi_ids, errors = parse_metabolites_field(metabolites)

    results = metabolomics_ora(
        client=client,
        chebi_ids=metabolite_chebi_ids,
        method=method,
        alpha=alpha,
        keep_insignificant=keep_insignificant,
        minimum_evidence_count=minimum_evidence_count,
        minimum_belief=minimum_belief,
    )

    return {
        "metabolites": metabolite_chebi_ids,
        "errors": errors,
        "results": results
    }


def enzyme_analysis(client, ec_code: str, chebi_ids: List[str] = None):
    """Perform enzyme analysis and explanation for given EC code and optional ChEBI IDs.


    client: The client object for making API calls
    ec_code (str): The EC code for the enzyme
    chebi_ids (List[str], optional): List of ChEBI IDs for additional context

    Returns:
    List: A list of statements explaining the enzyme's function"""
    stmts = metabolomics_explanation(
        client=client, ec_code=ec_code, chebi_ids=chebi_ids
    )
    return stmts



