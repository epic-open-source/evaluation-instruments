import pytest

from evaluation_instruments.model import TokenUsage


class Test_TokenUsage:
    @pytest.mark.parametrize(
        "prompt_tokens,completion_tokens,total_tokens,expected_total",
        [
            (10, 5, 15, 15),  # All parameters provided
            (10, 5, None, 15),  # Auto-calculate total_tokens
            (None, None, 15, 15),  # Only total_tokens
            (None, None, None, None),  # No parameters
        ],
    )
    def test_token_usage_init(self, prompt_tokens, completion_tokens, total_tokens, expected_total):
        """Test TokenUsage initialization with different parameters."""
        usage = TokenUsage(prompt_tokens=prompt_tokens, completion_tokens=completion_tokens, total_tokens=total_tokens)
        assert usage.prompt_tokens == prompt_tokens
        assert usage.completion_tokens == completion_tokens
        assert usage.total_tokens == expected_total

    def test_token_usage_str_repr(self):
        """Test string representation of TokenUsage."""
        usage = TokenUsage(prompt_tokens=10, completion_tokens=5, total_tokens=15)
        assert str(usage) == "Total Tokens=15"
        assert repr(usage) == "TokenUsage(prompt_tokens=10, completion_tokens=5, total_tokens=15)"

    @pytest.mark.parametrize(
        "params1, params2, is_equal",
        [
            # Equal objects
            ((10, 5, 15), (10, 5, 15), True),
            # Unequal objects
            ((10, 5, 15), (20, 10, 30), False),
            # Equality checks all values in self, so not symmetric
            ((10, 5, 15), (10, None, 15), False),
            ((10, None, 15), (10, 5, 15), True),
            # Different total tokens
            ((10, 5, 15), (10, 5, 20), False),
            # Both have None values
            ((10, None, None), (10, None, None), True),
        ],
    )
    def test_token_usage_equality(self, params1, params2, is_equal):
        """Test equality comparison of TokenUsage objects."""
        usage1 = TokenUsage(*params1)
        usage2 = TokenUsage(*params2)
        assert (usage1 == usage2) == is_equal

    @pytest.mark.parametrize(
        "params1, params2, expected_counts",
        [
            # Addition of two complete objects
            ((10, 5, 15), (20, 10, 30), (30, 15, 45)),
            # Addition with None values; total accumulates if not specified
            ((10, None, None), (None, 5, 15), (10, 5, 25)),
            # Addition with None and total
            ((None, None, 15), (None, 5, 15), (None, 5, 30)),
            # Addition with all None values
            ((None, None, None), (None, None, None), (None, None, None)),
        ],
    )
    def test_token_usage_addition(self, params1, params2, expected_counts):
        """Test addition of TokenUsage objects."""
        usage1 = TokenUsage(*params1)
        usage2 = TokenUsage(*params2)
        expected = TokenUsage(*expected_counts)

        assert expected == usage1 + usage2

    @pytest.mark.parametrize(
        "params1, params2, expected_comparisons",
        [
            # [lt, le, gt, ge]
            # First object smaller than second
            ((10, 5, 15), (20, 10, 30), (True, True, False, False)),
            # First object larger than second
            ((20, 10, 30), (10, 5, 15), (False, False, True, True)),
            # Equal objects
            ((10, 5, 15), (10, 5, 15), (False, True, False, True)),
            # Mixed values (only total tokens matter for comparison)
            ((30, 5, 35), (20, 10, 30), (False, False, True, True)),
            ((10, 20, 30), (20, 5, 25), (False, False, True, True)),
            # None values (comparison works based on available values)
            ((10, None, None), (5, None, None), (False, False, True, True)),
            ((None, 5, 15), (None, 10, 20), (True, True, False, False)),
            # Most likely is comparing total tokens to a full object
            ((None, None, 15), (1, 19, 20), (True, True, False, False)),
            ((None, None, 15), (1, 14, 15), (False, True, False, True)),
            ((None, None, 15), (1, 1, 2), (False, False, True, True)),
        ],
    )
    def test_token_usage_comparison(self, params1, params2, expected_comparisons):
        """Test comparison operations (<, <=, >, >=) between TokenUsage objects."""
        usage1 = TokenUsage(*params1)
        usage2 = TokenUsage(*params2)

        lt_expected, le_expected, gt_expected, ge_expected = expected_comparisons
        assert (usage1 < usage2) == lt_expected
        assert (usage1 <= usage2) == le_expected
        assert (usage1 > usage2) == gt_expected
        assert (usage1 >= usage2) == ge_expected

    def test_token_usage_incompatible_object(self):
        """Test validation fails with incompatible object."""
        usage = TokenUsage(10, 5, 15)

        class IncompatibleObject:
            pass

        with pytest.raises(AttributeError):
            usage.validate_compatible(IncompatibleObject())

    def test_token_usage_comparison_with_incompatible_object(self):
        """Test comparison with incompatible object raises error."""
        usage = TokenUsage(10, 5, 15)

        class IncompatibleObject:
            pass

        with pytest.raises(AttributeError):
            usage > IncompatibleObject()

    def test_token_usage_compatible_object(self):
        """Test validation succeeds with compatible object."""
        usage = TokenUsage(10, 5, 15)

        class CompatibleObject:
            def __init__(self):
                self.prompt_tokens = 5
                self.completion_tokens = 2
                self.total_tokens = 7

        assert usage.validate_compatible(CompatibleObject()) is True
