#stepmake_test.py
from model import wStrings
import pytest
from controller import StepMaker


def test_getstep():
    step = StepMaker.get_step()
    minimum_step = 0
    maximum_step = 3
    assert( step >= minimum_step and step <= maximum_step)



def test_getdurration():
    step = 0
    expect = wStrings.Seed.First_Beat
    durration = StepMaker.get_durration(step)
    assert(durration in expect)


    step = 1
    expect = wStrings.Seed.Second_Beat
    durration = StepMaker.get_durration(step)
    assert(durration in expect)


    step = 2
    expect = wStrings.Seed.Third_Beat
    durration = StepMaker.get_durration(step)
    assert(durration in expect)


    step = 3
    expect = wStrings.Seed.Fourth_Beat
    durration = StepMaker.get_durration(step)
    assert(durration in expect)