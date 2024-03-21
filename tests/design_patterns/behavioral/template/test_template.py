from design_patterns.behavioral.template.template import *


def test_workflow():
    # Assign
    concrete_class = ConcreteClass1()

    # Act
    s = concrete_class.workflow()

    # Assert
    assert s == "component1component2local_method"
