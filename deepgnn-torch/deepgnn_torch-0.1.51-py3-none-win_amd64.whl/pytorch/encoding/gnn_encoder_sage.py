# Copyright (c) Microsoft Corporation.
# Licensed under the MIT License.

"""Various encoders implementations."""
from typing import Callable

import numpy as np
import torch
import torch.nn as nn
import torch.nn.functional as F
from deepgnn.graph_engine import Graph, FeatureType
from deepgnn import get_logger


class SageEncoder(nn.Module):
    """Encode a node's using 'convolutional' GraphSage approach."""

    def __init__(
        self,
        features,
        query_func,
        feature_dim: int,
        aggregator: nn.Module,
        num_sample: int,
        intermediate_dim: int,
        embed_dim: int = 256,
        edge_type: int = 0,
        activation_fn: Callable = F.relu,
        base_model=None,
    ):
        """Initialization.

        Args:
            features: callback used to generate node feature embedding.
            query_func: query funtion used to fetch data from graph engine.
            feature_dim: used to specify dimension of features when fetch data from graph engine.
            intermediate_dim: used to define the trainable weight metric. if there is a feature
                encoder, intermeidate_dim means the dimension of output of specific feature encoder,
                or it will be the same as feature_dim.
            embed_dim: output embedding dimension of SageEncoder.
        """
        super(SageEncoder, self).__init__()

        get_logger().info(
            f"[SageEncoder] feature_dim:{feature_dim}, intermediate_dim:{intermediate_dim}, "
            f"embed_dim:{embed_dim}, edge_type:{edge_type}."
        )

        if base_model:
            self.base_model = base_model
        self.features = features
        if query_func is None:
            self.query_func = self.query_feature
        else:
            self.query_func = query_func
        self.aggregator = aggregator
        self.num_sample = num_sample
        self.edge_types = np.array([edge_type], dtype=np.int32)
        self.activation_fn = activation_fn
        self.weight = nn.Parameter(
            torch.empty(2 * intermediate_dim, embed_dim, dtype=torch.float32)
        )
        nn.init.xavier_uniform_(self.weight)

    def query(
        self,
        nodes: np.array,
        graph: Graph,
        feature_type: FeatureType,
        feature_idx: int,
        feature_dim: int,
    ):
        context = {}
        neigh_nodes = graph.sample_neighbors(nodes, self.edge_types, self.num_sample)[
            0
        ].flatten()
        neigh_nodes_unique, idx = np.unique(neigh_nodes, return_inverse=True)

        context["node_feats"] = self.query_func(
            nodes, graph, feature_type, feature_idx, feature_dim
        )

        neigh_feats_unique = self.query_func(
            neigh_nodes_unique, graph, feature_type, feature_idx, feature_dim
        )

        if isinstance(neigh_feats_unique, dict):
            context["neighbor_feats"] = {
                "node_feats": neigh_feats_unique["node_feats"][idx],
                "neighbor_feats": neigh_feats_unique["neighbor_feats"][idx],
                "node_count": idx.size,
            }
        else:
            context["neighbor_feats"] = neigh_feats_unique[idx]
        context["node_count"] = len(nodes)
        return context

    def query_feature(
        self,
        nodes: np.array,
        graph: Graph,
        feature_type: FeatureType,
        feature_idx: int,
        feature_dim: int,
    ):
        features = graph.node_features(
            nodes, np.array([[feature_idx, feature_dim]]), feature_type
        )
        return features

    def forward(self, context: dict):
        """Generate embeddings for a batch of nodes."""
        neigh_feats = self.aggregator.forward(
            context["neighbor_feats"], context["node_count"][0]
        )

        self_feats = self.features(context["node_feats"])
        combined = torch.cat([self_feats, neigh_feats], dim=1)
        combined = self.activation_fn(torch.matmul(combined, self.weight))
        return combined
