import re


def compare_version(version1, version2) -> bool:
    """
    Compare two version strings
    """

    def normalize(v):
        return [int(x) for x in re.sub(r'(\.0+)*$', '', v).split(".")]

    s1, s2 = normalize(version1), normalize(version2)
    if len(s1) != len(s2):
        return len(s1) > len(s2)

    for i, j in zip(s1, s2):
        if i >= j:
            return True
    return False
def is_ver_str(v_str:str):
    return re.match(r"^\d+\.\d+\.\d+$",v_str) is not None

if __name__ == '__main__':
    print(compare_version("1.0.1", "1.0.0"))
