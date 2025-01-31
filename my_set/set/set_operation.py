class set_operation:

    def test_t0_add_element(set, element):
        set.add(element)
        return set

    def test_to_remove_element(set, element):

        if element in set:
            set.remove(element)
        else:
            raise KeyError(f"Element {element} not found in set.")
        return set

    def to_if_element_exists(set, element):

        return element in set

    def union_sets(set1, set2):

        return set1.union(set2)

