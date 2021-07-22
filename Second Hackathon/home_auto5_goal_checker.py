#!/usr/bin/env python3

from goalee import Target, RedisMiddleware
from goalee.topic_goals import TopicMessageReceivedGoal, TopicMessageParamGoal
from goalee.area_goals import RectangleAreaGoal, CircularAreaGoal
from goalee.complex_goal import ComplexGoal, ComplexGoalAlgorithm
from goalee.types import Point


if __name__ == '__main__':
    middleware = RedisMiddleware()
    t = Target(middleware, name='MyAppTarget',
               score_weights=[0.3333333333333333, 0.3333333333333333, 0.3333333333333333])

    g = ComplexGoal(name='InLivingRoom',
                    max_duration=None,
                    min_duration=None)
    gs = TopicMessageReceivedGoal(topic='livingroom.intruder_detected',
                                  name='IntruderPresenceLivingRoom',
                                  max_duration=None,
                                  min_duration=None)

    g.add_goal(gs)
    gs = TopicMessageParamGoal(topic='livingroom.light',
                               name='LivingRoomBlink',
                               condition=lambda msg: True if msg['doBlink'] == 1 else False,
                               max_duration=None,
                               min_duration=None)
    g.add_goal(gs)
    g.add_goal(gs)
    ## More Goals to Generate here
    t.add_goal(g)
    g = ComplexGoal(name='InKitchen',
                    max_duration=None,
                    min_duration=None)
    gs = TopicMessageReceivedGoal(topic='kitchen.intruder_detected',
                                  name='IntruderPresenceKitchen',
                                  max_duration=None,
                                  min_duration=None)

    g.add_goal(gs)
    gs = TopicMessageParamGoal(topic='kitchen.light',
                               name='KitchenBlink',
                               condition=lambda msg: True if msg['doBlink'] == 1 else False,
                               max_duration=None,
                               min_duration=None)
    g.add_goal(gs)
    g.add_goal(gs)
    ## More Goals to Generate here
    t.add_goal(g)
    g = ComplexGoal(name='InBedroom',
                    max_duration=None,
                    min_duration=None)
    gs = TopicMessageReceivedGoal(topic='bedroom.intruder_detected',
                                  name='IntruderPresenceBedroom',
                                  max_duration=None,
                                  min_duration=None)

    g.add_goal(gs)
    gs = TopicMessageParamGoal(topic='bedroom.light',
                               name='BedroomBlink',
                               condition=lambda msg: True if msg['doBlink'] == 1 else False,
                               max_duration=None,
                               min_duration=None)
    g.add_goal(gs)
    g.add_goal(gs)
    ## More Goals to Generate here
    t.add_goal(g)

    t.run_concurrent()
