<!-- <p align="center">
  <a href="" rel="noopener">
 <img width=200px height=200px src="https://i.imgur.com/6wj0hh6.jpg" alt="Project logo"></a>
</p> -->

<h1 align="center">testbed_description</h1>

<p align="center"> Robot description for the ODRI Dual Motor Test Bed
    <br>
</p>

## 📝 Table of Contents
- [About](#about)
- [Usage](#usage)
- [Author](#author)
- [Acknowledgments](#acknowledgement)

## 🧐 About <a name = "about"></a>

This package contains the robot description (URDF/xacro) for the ODRI Dual Motor Test Bed. The main URDF file (```urdf/testbed.urdf.xacro```) contains a  ```simulation``` argument that controls loading the correct hardware interface plugins.

## 🎈 Usage <a name="usage"></a>

Meshes and URDFs are not to be used directly. The provided launch files contain basic functionalities.

```launch/load.launch.py``` exposes the ```simulation``` argument and loads the URDF using the **robot_state_publisher** package.

```launch/debug.launch.py``` publishes the URDF and loads the **joint_state_publisher_gui** for basic kinematic testing.

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