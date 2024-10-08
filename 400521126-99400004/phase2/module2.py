from phase0.FA_class import DFA
from phase0.FA_class import State
from phase1.module1 import convert_into_bit_address
from utils import utils
from utils.utils import imageType


def chack_address(address: str, fa: DFA):
    curr: State = fa.init_state
    for c in address:
        curr = curr.transitions[c]
    return fa.is_final(curr)


def solve_percentage(fa: DFA, image: imageType) -> float:
    address = convert_into_bit_address(image)
    match = 0
    for add in address:
        if chack_address(add, fa):
            match += 1
    return match / len(address)


def solve(json_str: str, image: imageType) -> bool:
    fa = DFA.deserialize_json(json_str)
    res = solve_percentage(fa, image)
    print(str(res * 100) + "%")
    return res == 1


if __name__ == "__main__":
    print(
        solve(
            '{"states": ["q_0", "q_1", "q_2", "q_3", "q_4"], "initial_state": "q_0", "final_states": ["q_3"], '
            '"alphabet": ["0", "1", "2", "3"], "q_0": {"0": "q_1", "1": "q_1", "2": "q_2", "3": "q_2"}, "q_1": {"0": '
            '"q_3", "1": "q_3", "2": "q_3", "3": "q_4"}, "q_2": {"0": "q_4", "1": "q_3", "2": "q_3", "3": "q_3"}, '
            '"q_3": {"0": "q_3", "1": "q_3", "2": "q_3", "3": "q_3"}, "q_4": {"0": "q_4", "1": "q_4", "2": "q_4", '
            '"3": "q_4"}}',
            [[1, 1, 1, 1],
             [1, 0, 1, 0],
             [0, 1, 0, 1],
             [1, 1, 1, 1]]
        )
    )
