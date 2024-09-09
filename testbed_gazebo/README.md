<!-- <p align="center">
  <a href="" rel="noopener">
 <img width=200px height=200px src="https://i.imgur.com/6wj0hh6.jpg" alt="Project logo"></a>
</p> -->

<h1 align="center">testbed_gazebo</h1>

<p align="center"> Gazebo (modern/Ignition) integration for the ODRI Dual Motor Test Bed
    <br>
</p>

## 📝 Table of Contents
- [About](#about)
- [Usage](#usage)
- [Author](#author)
- [Acknowledgments](#acknowledgement)

## 🧐 About <a name = "about"></a>

This package creates a simulated version of the ODRI Dual Motor Test Bed using the Gazebo (modern/Ignition) simulator.

## 🎈 Usage <a name="usage"></a>

The provided launch file (```launch/empty_world.launch.py```) loads the robot URDF in Gazebo (headless mode) and also calls the [gz_rtf_publisher](https://github.com/leggedrobotics-usp/gz_rtf_publisher) for visualization purposes. The ros2_control plugins are loaded through the URDF, and the controller manager is also started. Use the **testbed_control** package to load the controllers.

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