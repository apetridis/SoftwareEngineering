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

    g = ComplexGoal(name='HumanLivingRoomDetected',
                    max_duration=None,
                    min_duration=None)
    gs = TopicMessageReceivedGoal(topic='livingroom.human_detected',
                                  name='HumanPresenceLivingRoom',
                                  max_duration=None,
                                  min_duration=None)

    g.add_goal(gs)
    g.add_goal(gs)
    ## More Goals to Generate here
    t.add_goal(g)
    g = ComplexGoal(name='HumanKitchenDetected',
                    max_duration=None,
                    min_duration=None)
    gs = TopicMessageReceivedGoal(topic='kitchen.human_detected',
                                  name='HumanPresenceKitchen',
                                  max_duration=None,
                                  min_duration=None)

    g.add_goal(gs)
    g.add_goal(gs)
    ## More Goals to Generate here
    t.add_goal(g)
    g = ComplexGoal(name='HumanBedroomDetected',
                    max_duration=None,
                    min_duration=None)
    gs = TopicMessageReceivedGoal(topic='bedroom.human_detected',
                                  name='HumanPresenceBedroom',
                                  max_duration=None,
                                  min_duration=None)

    g.add_goal(gs)
    g.add_goal(gs)
    ## More Goals to Generate here
    t.add_goal(g)

    t.run_concurrent()
