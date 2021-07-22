#!/usr/bin/env python3

from goalee import Target, RedisMiddleware
from goalee.topic_goals import TopicMessageReceivedGoal, TopicMessageParamGoal
from goalee.area_goals import RectangleAreaGoal, CircularAreaGoal
from goalee.complex_goal import ComplexGoal, ComplexGoalAlgorithm
from goalee.types import Point


if __name__ == '__main__':
    middleware = RedisMiddleware()
    t = Target(middleware, name='MyAppTarget',
               score_weights=[0.2, 0.2, 0.2, 0.2, 0.2])

    g = ComplexGoal(name='ControlRegionA',
                    max_duration=None,
                    min_duration=None)
    g.add_goal(gs)
    g.add_goal(gs)
    ## More Goals to Generate here
    t.add_goal(g)
    g = ComplexGoal(name='ControlRegionB',
                    max_duration=None,
                    min_duration=None)
    g.add_goal(gs)
    g.add_goal(gs)
    ## More Goals to Generate here
    t.add_goal(g)
    g = ComplexGoal(name='ControlRegionC',
                    max_duration=None,
                    min_duration=None)
    g.add_goal(gs)
    g.add_goal(gs)
    ## More Goals to Generate here
    t.add_goal(g)
    g = ComplexGoal(name='ControlRegionD',
                    max_duration=None,
                    min_duration=None)
    g.add_goal(gs)
    g.add_goal(gs)
    ## More Goals to Generate here
    t.add_goal(g)
    g = ComplexGoal(name='Quality',
                    max_duration=None,
                    min_duration=None)
    gs = TopicMessageParamGoal(topic='garden.air_quality',
                               name='QualitySomeFall',
                               condition=lambda msg: True if ((msg['regionA'] < 0.5 or msg['regionB'] < 0.5) or (msg['regionC'] < 0.5 or msg['regionD'] < 0.5)) else False,
                               max_duration=None,
                               min_duration=None)
    g.add_goal(gs)
    g.add_goal(gs)
    gs = TopicMessageParamGoal(topic='garden.air_quality',
                               name='QualityAllRaised',
                               condition=lambda msg: True if ((msg['regionA'] > 0.8 and msg['regionB'] > 0.8) and (msg['regionC'] > 0.8 and msg['regionD'] > 0.8)) else False,
                               max_duration=None,
                               min_duration=None)
    g.add_goal(gs)
    g.add_goal(gs)
    ## More Goals to Generate here
    t.add_goal(g)

    t.run_concurrent()
