### Hi there 👋

<!--
**doosan109/doosan109** is a ✨ _special_ ✨ repository because its `README.md` (this file) appears on your GitHub profile.

Here are some ideas to get you started:

- 🔭 I’m currently working on ...
- 🌱 I’m currently learning ...
- 👯 I’m looking to collaborate on ...
- 🤔 I’m looking for help with ...
- 💬 Ask me about ...
- 📫 How to reach me: ...
- 😄 Pronouns: ...
- ⚡ Fun fact: ...
-->this is first edit


- - -
## 2023_2_13

- - -

* fisrt
  * turtlebot3
  * Environment VMware 17 Ubuntu 20.04
* second
  * ROS2 DDS explain
* third
  * cw
  * ros2 run turtlesim turtlesim_node
  * ros2 run turtlesim turtle_teleop_key
  * ros2 run turtlesim turtlesim_node --ros-args --remap __node:=my_turtle
  * ros2 node list
  * rqt
  * ros2 service call /spawn turtlesim/srv/Spawn "{x: 5.5, y: 9, theta: 1.57, name: 'leonardo'}"
  * ros2 topic pub --rate 1 /turtle1/cmd_vel geometry_msgs/msg/Twist '{linear: {x: 2.0, y: 0.0, z: 0.0}, angular: {x: 0.0, y: 0.0, z: 1.8}}'
  * history
  * git config --global user.email "doosan109@naver.com"
  * git config --global user.name "doosan109"
  * https://github.com/freshmea
  * param list
  * ros2 param list
  * ros2 param get /turtlesim background_r
  * ros2 param get /turtlesim background_g
  * ros2 param get /turtlesim background_b
  * ros2 param dump /turtlesim
  * cat turtlesim.yaml
  * ros2 param load /turtlesim turtlesim.yaml
  * ros2 action list -t
  * ros2 action send_goal /turtle1/rotate_absolute turtlesim/action/RotateAbsolute "{theta: 1.7}"
  * ros2 run turtlesim turtlesim_node --ros-args --params-file ./turtlesim.yaml
