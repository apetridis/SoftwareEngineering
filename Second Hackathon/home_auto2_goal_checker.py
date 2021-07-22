#!/usr/bin/env python3

from goalee import Target, RedisMiddleware
from goalee.topic_goals import TopicMessageReceivedGoal, TopicMessageParamGoal
from goalee.area_goals import RectangleAreaGoal, CircularAreaGoal
from goalee.complex_goal import ComplexGoal, ComplexGoalAlgorithm
from goalee.types import Point


if __name__ == '__main__':
    middleware = RedisMiddleware()
    t = Target(middleware, name='KichenTarget',
               score_weights=[0.25, 0.25, 0.25, 0.25])

    g = ComplexGoal(name='KitchenHumidity',
                    max_duration=None,
                    min_duration=None)
    gs = TopicMessageParamGoal(topic='kitchen.humidity',
                               name='HumidityControlKitchen',
                               condition=lambda msg: True if (msg['humidity'] > 0.5 or msg['humidity'] < 0.3) else False,
                               max_duration=600.0,
                               min_duration=None)
    g.add_goal(gs)
    gs = TopicMessageParamGoal(topic='kitchen.humidifier',
                               name='HumidifierKichenEnabled',
                               condition=lambda msg: True if msg['state'] == 1 else False,
                               max_duration=None,
                               min_duration=None)
    g.add_goal(gs)
    ## More Goals to Generate here
    t.add_goal(g)
    g = ComplexGoal(name='LivingRoomHumidity',
                    max_duration=None,
                    min_duration=None)
    gs = TopicMessageParamGoal(topic='livingroom.humidity',
                               name='HumidityControlLivingRoom',
                               condition=lambda msg: True if (msg['humidity'] > 0.5 or msg['humidity'] < 0.3) else False,
                               max_duration=600.0,
                               min_duration=None)
    g.add_goal(gs)
    gs = TopicMessageParamGoal(topic='livingroom.humidifier',
                               name='HumidifierLivingRoomEnabled',
                               condition=lambda msg: True if msg['state'] == 1 else False,
                               max_duration=None,
                               min_duration=None)
    g.add_goal(gs)
    ## More Goals to Generate here
    t.add_goal(g)
    g = ComplexGoal(name='BedroomHumidity',
                    max_duration=None,
                    min_duration=None)
    gs = TopicMessageParamGoal(topic='bedroom.humidity',
                               name='HumidityControlBedroom',
                               condition=lambda msg: True if (msg['humidity'] > 0.5 or msg['humidity'] < 0.3) else False,
                               max_duration=600.0,
                               min_duration=None)
    g.add_goal(gs)
    gs = TopicMessageParamGoal(topic='bedroom.humidifier',
                               name='HumidifierBedroomEnabled',
                               condition=lambda msg: True if msg['state'] == 1 else False,
                               max_duration=None,
                               min_duration=None)
    g.add_goal(gs)
    ## More Goals to Generate here
    t.add_goal(g)
    g = ComplexGoal(name='BathroomHumidity',
                    max_duration=None,
                    min_duration=None)
    gs = TopicMessageParamGoal(topic='bathroom.humidity',
                               name='HumidityControlBathroom',
                               condition=lambda msg: True if (msg['humidity'] > 0.5 or msg['humidity'] < 0.3) else False,
                               max_duration=600.0,
                               min_duration=None)
    g.add_goal(gs)
    gs = TopicMessageParamGoal(topic='bathroom.humidifier',
                               name='HumidifierBathroomEnabled',
                               condition=lambda msg: True if msg['state'] == 1 else False,
                               max_duration=None,
                               min_duration=None)
    g.add_goal(gs)
    ## More Goals to Generate here
    t.add_goal(g)

    t.run_concurrent()
