from design_patterns.creational.prototype_pattern.prototype_pattern import VehiclePart


def test_prototype_pattern():
    original_part = VehiclePart()
    cloned_part = original_part.clone()

    assert original_part is not cloned_part, "Original and cloned are the same object"
    assert isinstance(cloned_part, original_part.__class__), "Cloned part is not the same class as original part"