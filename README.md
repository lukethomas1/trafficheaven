To use InputGenerator.StopLight:

from InputGenerator.StopLight import StopLight

test_light = StopLight()

test_light.fill()

test_light.randomize()

test_light.calc_costs()

inputs = test_light.get_input()

outputs = test_light.get_output()
