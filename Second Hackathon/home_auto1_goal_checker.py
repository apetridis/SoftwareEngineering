#!/usr/bin/env python3

from goalee import Target, RedisMiddleware
from goalee.topic_goals import TopicMessageReceivedGoal, TopicMessageParamGoal
from goalee.area_goals import RectangleAreaGoal, CircularAreaGoal
from goalee.complex_goal import ComplexGoal, ComplexGoalAlgorithm
from goalee.types import Point


if __name__ == '__main__':
    middleware = RedisMiddleware()
    t = Target(middleware, name='MyAppTarget',
               score_weights=[0.5, 0.5])

    g = TopicMessageParamGoal(topic='kitchen.gas',
                              name='GasRaised',
                              condition=lambda msg: True if msg['gas'] > 0.3 else False,
                              max_duration=None,
                              min_duration=None)
    t.add_goal(g)
    g = ComplexGoal(name='GasGoal',
                    max_duration=None,
                    min_duration=None)
    gs = TopicMessageParamGoal(topic='alarm',
                               name='AlarmEnable',
                               condition=lambda msg: True if msg['state'] == 1 else False,
                               max_duration=None,
                               min_duration=None)
    g.add_goal(gs)
    gs = TopicMessageParamGoal(topic='bathroom.thermostat',
                               name='ThermostatBathroomDisabled',
                               condition=lambda msg: True if msg['state'] == 0 else False,
                               max_duration=None,
                               min_duration=None)
    g.add_goal(gs)
    gs = TopicMessageParamGoal(topic='kitchen.thermostat',
                               name='ThermostatKitchenDisabled',
                               condition=lambda msg: True if msg['state'] == 0 else False,
                               max_duration=None,
                               min_duration=None)
    g.add_goal(gs)
    gs = TopicMessageParamGoal(topic='corridor.thermostat',
                               name='ThermostatCorridorDisabled',
                               condition=lambda msg: True if msg['state'] == 0 else False,
                               max_duration=None,
                               min_duration=None)
    g.add_goal(gs)
    gs = TopicMessageParamGoal(topic='livingroom.thermostat',
                               name='ThermostatLivingRoomDisabled',
                               condition=lambda msg: True if msg['state'] == 0 else False,
                               max_duration=None,
                               min_duration=None)
    g.add_goal(gs)
    gs = TopicMessageParamGoal(topic='bedroom.thermostat',
                               name='ThermostatBedroomDisabled',
                               condition=lambda msg: True if msg['state'] == 0 else False,
                               max_duration=None,
                               min_duration=None)
    g.add_goal(gs)
    gs = TopicMessageParamGoal(topic='kitchen.kitchen_relay',
                               name='RelaysKitchenDisabled',
                               condition=lambda msg: True if msg['state'] == 0 else False,
                               max_duration=None,
                               min_duration=None)
    g.add_goal(gs)
    gs = TopicMessageParamGoal(topic='livingroom.tv_relay',
                               name='RelaysLivingRoomDisabled',
                               condition=lambda msg: True if msg['state'] == 0 else False,
                               max_duration=None,
                               min_duration=None)
    g.add_goal(gs)
    gs = TopicMessageParamGoal(topic='kitchen.humidifier',
                               name='HumidifierKichenDisabled',
                               condition=lambda msg: True if msg['state'] == 0 else False,
                               max_duration=None,
                               min_duration=None)
    g.add_goal(gs)
    gs = TopicMessageParamGoal(topic='livingroom.humidifier',
                               name='HumidifierLivingRoomDisabled',
                               condition=lambda msg: True if msg['state'] == 0 else False,
                               max_duration=None,
                               min_duration=None)
    g.add_goal(gs)
    gs = TopicMessageParamGoal(topic='bedroom.humidifier',
                               name='HumidifierBedroomDisabled',
                               condition=lambda msg: True if msg['state'] == 0 else False,
                               max_duration=None,
                               min_duration=None)
    g.add_goal(gs)
    gs = TopicMessageParamGoal(topic='bathroom.humidifier',
                               name='HumidifierBathroomDisabled',
                               condition=lambda msg: True if msg['state'] == 0 else False,
                               max_duration=None,
                               min_duration=None)
    g.add_goal(gs)
    ## More Goals to Generate here
    t.add_goal(g)

    t.run_seq()
