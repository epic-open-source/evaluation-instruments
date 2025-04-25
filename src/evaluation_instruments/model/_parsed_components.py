from dataclasses import dataclass
from typing import Optional


@dataclass(init=False)
class TokenUsage:
    prompt_tokens: Optional[int] = None
    completion_tokens: Optional[int] = None
    total_tokens: Optional[int] = None

    def __init__(
        self,
        prompt_tokens: Optional[int] = None,
        completion_tokens: Optional[int] = None,
        total_tokens: Optional[int] = None,
        **kwargs,
    ):
        self.prompt_tokens = prompt_tokens
        self.completion_tokens = completion_tokens
        self.total_tokens = total_tokens
        if self.total_tokens is None and (self.prompt_tokens is not None or self.completion_tokens is not None):
            self.total_tokens = (self.prompt_tokens or 0) + (self.completion_tokens or 0)

        if kwargs:
            self.other = kwargs

    def __str__(self):
        return f"Total Tokens={self.total_tokens}"

    def __repr__(self):
        return (
            f"TokenUsage(prompt_tokens={self.prompt_tokens}, "
            f"completion_tokens={self.completion_tokens}, "
            f"total_tokens={self.total_tokens})"
        )

    def __add__(self, other):
        self.validate_compatible(other)

        new_obj = TokenUsage()

        for attr in self.__dataclass_fields__:
            new_value = None
            if getattr(self, attr) is not None or getattr(other, attr) is not None:
                new_value = (getattr(self, attr) or 0) + (getattr(other, attr) or 0)
            setattr(new_obj, attr, new_value)

        return new_obj

    def validate_compatible(self, other):
        for attr in self.__dataclass_fields__:
            if not hasattr(other, attr):
                raise AttributeError(f"Comparison not supported with {type(other)}")
        return True

    def __eq__(self, other):
        self.validate_compatible(other)

        return (
            (True if self.prompt_tokens is None else self.prompt_tokens == other.prompt_tokens)
            and (True if self.completion_tokens is None else self.completion_tokens == other.completion_tokens)
            and (True if self.total_tokens is None else self.total_tokens == other.total_tokens)
        )

    def __gt__(self, other):
        """
        This is NOT traditional python greater than, but supports using > for threshold checks.
        The comparison is non-symmetric, returning true if ANY of the attributes are greater than
        other.

        Intended usage is around thresholds when 'accumulated' > 'capacity' for any subcomponent.
        """
        self.validate_compatible(other)

        for attr in self.__dataclass_fields__:
            self_value = getattr(self, attr)
            other_value = getattr(other, attr)

            if self_value is not None and other_value is not None:
                if self_value > other_value:
                    return True
        return False

    def __ge__(self, other):
        return self == other or self > other

    def __lt__(self, other):
        self.validate_compatible(other)

        any_larger = self == other  # equal is not strictly less than
        for attr in self.__dataclass_fields__:
            self_value = getattr(self, attr)
            other_value = getattr(other, attr)

            if self_value is not None and other_value is not None:
                if self_value > other_value:
                    any_larger = True
        return not any_larger

    def __le__(self, other):
        return self == other or self < other
