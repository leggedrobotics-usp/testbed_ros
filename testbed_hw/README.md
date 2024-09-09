<!-- <p align="center">
  <a href="" rel="noopener">
 <img width=200px height=200px src="https://i.imgur.com/6wj0hh6.jpg" alt="Project logo"></a>
</p> -->

<h1 align="center">tesbed_hw</h1>

<p align="center"> Hardware integration for the ODRI Dual Motor Test Bed (based on the ODRI Master Board)
    <br>
</p>

## 📝 Table of Contents
- [About](#about)
- [Usage](#usage)
- [Author](#author)
- [Acknowledgments](#acknowledgement)

## 🧐 About <a name = "about"></a>

This package integrates with the real hardware of the Dual Motor Test Bed using the ODRI Master Board hardware interface ([ros2_hardware_interface_odri](https://github.com/stack-of-tasks/ros2_hardware_interface_odri)).

## 🎈 Usage <a name="usage"></a>

Make sure to edit the ```interface ``` definition in ```config/testbed_config.yaml``` to match your hardware. Use ```ifconfig``` to find the correct interface name.

The provided launch file (```launch/load.launch.py```) loads the robot URDF with the corresponding ros2_control plugins. The controller manager is also started. Use the **testbed_control** package to load the controllers.

## ✍️ Author <a name = "author"></a>

<a href="https://github.com/Vtn21">
 <img style="border-radius: 50%;" src="https://avatars.githubusercontent.com/u/13922299?s=460&u=2e2554bb02cc92028e5cba651b04459afd3c84fd&v=4" width="100px;" alt=""/>
 <br />
 <sub><b>Victor T. N. 🤖</b></sub></a>

Made with ❤️ by [@Vtn21](https://github.com/Vtn21)

## 🎉 Acknowledgements <a name = "acknowledgement"></a>

<a href="https://github.com/open-dynamic-robot-initiative">
 <img style="border-radius: 50%;" src="https://avatars.githubusercontent.com/u/54143164?s=200&v=4" width="100px;" alt=""/>
 <br />
 <sub><b>Open Dynamic Robot Initiative</b></sub></a>

 Designers of the Dual Motor Test Bed

<!-- [![Gmail Badge](https://img.shields.io/badge/-victor.noppeney@usp.br-c14438?style=flat-square&logo=Gmail&logoColor=white&link=mailto:victor.noppeney@usp.br)](mailto:victor.noppeney@usp.br) -->

<!-- -  - Idea & Initial work -->

<!-- See also the list of [contributors](https://github.com/kylelobo/The-Documentation-Compendium/contributors) who participated in this project. -->