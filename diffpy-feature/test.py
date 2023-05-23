import difflib
from rich.console import Console
from myers import myers_diff, display_diff, validate_args

if __name__ == '__main__':
    # use sys.argv to get the arguments
    a_lines, b_lines = validate_args()
    diff = myers_diff(a_lines, b_lines)
    display_diff(diff)
