<!-- <p align="center">
  <a href="" rel="noopener">
 <img width=200px height=200px src="https://i.imgur.com/6wj0hh6.jpg" alt="Project logo"></a>
</p> -->

<h1 align="center">testbed_control</h1>

<p align="center"> ros2_control algorithms for the ODRI Dual Motor Test Bed
    <br>
</p>

## 📝 Table of Contents
- [About](#about)
- [Usage](#usage)
- [Author](#author)
- [Acknowledgments](#acknowledgement)

## 🧐 About <a name = "about"></a>

This package is focused on implementing controllers for the ODRI Dual Motor Test Bed. Controller implementation is hardware-agnostic, meaning that the controllers work "as-is" on simulation or real hardware.

## 🎈 Usage <a name="usage"></a>

Use the ```config/controllers.yaml``` file to set up all controllers. Currently a forward position controller and a joint state broadcaster are implemented as examples.

There is a provided launch file (```launch/position_control.launch.py```) that spawns the forward position controller, the joint state broadcaster and also the [reference_signal_generator](https://github.com/leggedrobotics-usp/reference_signal_generator). It is necessary to start the controller manager from simulation or hardware to wrap up the ecosystem; see the **testbed_gazebo** and **testbed_hw** packages for more information.

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