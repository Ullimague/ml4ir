from ml4ir.model.scoring.scoring_base import ScoringBase


class PairwiseScoring(ScoringBase):
    def get_scoring_fn(self, **kwargs):
        """
        Define a pointwise ranking scoring function with specified architecture
        """

        def _scoring_fn(features):
            raise NotImplementedError

        return _scoring_fn
