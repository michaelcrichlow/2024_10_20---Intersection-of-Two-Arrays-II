def intersect(nums1: list[int], nums2: list[int]) -> list[int]:
    local_array = []
    if len(nums1) <= len(nums2):
        for val in nums1:
            if val in nums2:
                local_array.append(val)
                nums2.remove(val)
    elif len(nums2) <= len(nums1):
        for val in nums2:
            if val in nums1:
                local_array.append(val)
                nums1.remove(val)

    return local_array


def main() -> None:
    assert (intersect([1, 2, 2, 1], [2, 2]) == [2, 2])
    assert (intersect([4, 9, 5], [9, 4, 9, 8, 4]) == [4, 9])
    assert (intersect([1, 2, 2, 1], [2]) == [2])
    assert (intersect([3, 1, 2], [1, 1]) == [1])
    print("all tests passed!")


if __name__ == '__main__':
    main()
