import copy


class VehiclePart:
    def clone(self):
        return copy.deepcopy(self)


# class PrototypePattern:
#     @staticmethod
#     def main():
#         original_part = VehiclePart()
#         cloned_part = original_part.clone()
#
#         assert original_part is not cloned_part, "Original and cloned are the same object"
#         assert isinstance(cloned_part, original_part.__class__), "Cloned part is not the same class as original part"
#
#         print("Original part: ", original_part)
#         print("Cloned part: ", cloned_part)
#         print("Original and cloned are not the same object.")
#
#         print("Original part class: ", original_part.__class__.__name__)
#         print("Cloned part class: ", cloned_part.__class__.__name__)
#         print("Original and cloned are the same class.")
#
#         # In summary, this saves times in creating the similar objects from the same class.

# if __name__ == "__main__":
#     PrototypePattern.main()


if __name__ == "__main__":
    original_part = VehiclePart()
    cloned_part = original_part.clone()

    assert original_part is not cloned_part, "Original and cloned are the same object"
    assert isinstance(cloned_part, original_part.__class__), "Cloned part is not the same class as original part"
