# 🧭 ROS2 + Ignition Gazebo 6 Setup Guide (Ubuntu 22.04)

Welcome to a beginner-friendly walkthrough for setting up a basic **ROS2 Package** using **Python**, integrated with **Ignition Gazebo 6 (Fortress)** on a **Ubuntu 22.04** Machine. This guide emphasizes a clean setup with working commands and references—so you can get up and simulating fast!

---

## 📌 What This Project Covers

- Basic ROS2 workspace and package setup
- Integration with Gazebo Ignition 6 (Fortress)
- Python 3.10 compatibility
- Ubuntu 22.04 environment
- Quick terminal setup commands
- References to official documentation

---

## 🧱 Tech Stack

| Tool            | Version            |
|-----------------|--------------------|
| OS              | Ubuntu 22.04 LTS   |
| ROS2            | Humble Hawksbill   |
| Gazebo Ignition | Fortress (Ignition 6) |
| Python          | 3.10+              |

---

## ⚙️ Prerequisites

- Ubuntu 22.04 machine
- At least 4 GB RAM (8 GB+ recommended)
- Familiarity with basic terminal commands

---

## 🚀 Installing ROS2 Humble

Refer to the official guide here:  
📖 [ROS2 Humble Installation](https://docs.ros.org/en/humble/Installation/Ubuntu-Install-Debs.html)

Or run:

```bash
sudo apt update && sudo apt upgrade
sudo apt install software-properties-common
sudo add-apt-repository universe
sudo apt update && sudo apt install curl -y
sudo curl -sSL https://raw.githubusercontent.com/ros/rosdistro/master/ros.key -o /usr/share/keyrings/ros-archive-keyring.gpg

sudo sh -c 'echo "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/ros-archive-keyring.gpg] \
https://packages.ros.org/ros2/ubuntu $(lsb_release -cs) main" > /etc/apt/sources.list.d/ros2.list'

sudo apt update
sudo apt install ros-humble-desktop

# Source the ROS environment
echo "source /opt/ros/humble/setup.bash" >> ~/.bashrc
source ~/.bashrc
```

## Installing Ignition Gazebo 6:

Official guide for the Installation can be found here:
[Ignition Gazebo 6 Installation](https://gazebosim.org/docs/fortress/install_ubuntu/)

Or run:

```bash
sudo apt-get update
sudo apt-get install lsb-release gnupg

# Add the Ignition repository
sudo curl https://packages.osrfoundation.org/gazebo.gpg --output /usr/share/keyrings/pkgs-osrf-archive-keyring.gpg
echo "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/pkgs-osrf-archive-keyring.gpg] http://packages.osrfoundation.org/gazebo/ubuntu-stable $(lsb_release -cs) main" | sudo tee /etc/apt/sources.list.d/gazebo-stable.list > /dev/null

sudo apt-get update
sudo apt-get install ignition-fortress
```

To test your installed Gazebo Ignition, just run:

```bash
ign gazebo
```

## 🧰 Create a new Workspace in ROS2:

For creating a new workspace, just run:

```bash
mkdir -p ~/ros2_ws/src
cd ~/ros2_ws
```

## 📦 Create a Python-Based ROS2 Package

Inside the '/src' folder, clone this repository: 

```bash
git clone https://github.com/sohaib-kashif-97/ROS2-Tutorial-Medium-Part1.git
```

If you have 'tree' install, you would be able to overlook your Package Directory Structure. In our case, it would look like:

```bash
ign_pkg_v1/
├── CMakeLists.txt
├── launch
│   └── ign_pkg_v1.launch.py
├── models
│   └── quadcopter
│       └── model.sdf
├── package.xml
└── worlds
    └── world.sdf
```

Run the setup by the following commands below:

```bash
cd ~/ros2_ws
clear
rm -rf install log build
colcon build
source install/setup.bash
ros2 launch ign_pkg_v1 ign_pkg_v1.launch.py
```

