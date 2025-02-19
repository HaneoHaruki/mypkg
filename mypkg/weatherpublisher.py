# SPDX-FileCopyrightText: 2025 Haruki Haneo
# SPDX-License-Identifier: BSD-3-Clause

import os
import requests
from rclpy.node import Node
from std_msgs.msg import String
import rclpy

class WeatherPublisher(Node):
    def __init__(self):
        super().__init__('weather_publisher')
        self.publisher_ = self.create_publisher(String, 'weatherpublisher', 10)
        self.timer = self.create_timer(1.0, self.publish_weather)

    def get_weather_data(self):
        try:
            api_key = os.getenv('WEA_API_KEY')
            city = 'Okinawa'
            url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric'

            response = requests.get(url)
            response.raise_for_status()
            weather_data = response.json()

            temperature = weather_data['main']['temp']
            humidity = weather_data['main']['humidity']
            return temperature, humidity
        except Exception:
            return None, None

    def publish_weather(self):
        temperature, humidity = self.get_weather_data()
        if temperature is not None and humidity is not None:
            msg = String()
            msg.data = f'Temperature: {temperature}°C, Humidity: {humidity}%'
            self.publisher_.publish(msg)

def main(args=None):
    rclpy.init(args=args)
    node = WeatherPublisher()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()





##class Talker(Node):
    ##def __init__(self):
        ##super().__init__("talker")
        ##self.pub = self.create_publisher(Int16, "countup", 10)
        ##self.n = 0
        ##self.create_timer(0.5, self.cb)
        
##rclpy.init()
##node = Node("talker")
##pub = node.create_publisher(Int16, "countup", 10)
##n = 0

    ##def cb():
        ##global n
        ##msg = Int16()
        ##msg.data = n
        ##pub.publish(msg)
        ##n += 1
    ##def cb(self):
        ##msg = Int16()
        ##msg.data = self.n
        ##self.pub.publish(msg)
        ##self.n += 1


##def main():
    ##node.create_timer(0.5, cb)
    ##rclpy.spin(node)


##def main():
    ##rclpy.init()
    ##node = Talker()
    ##rclpy.spin(node)
