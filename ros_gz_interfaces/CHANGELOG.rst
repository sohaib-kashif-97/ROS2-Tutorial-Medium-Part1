^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Changelog for package ros_gz_interfaces
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

0.244.20 (2025-06-12)
---------------------

0.244.19 (2025-05-26)
---------------------

0.244.18 (2025-05-23)
---------------------

0.244.17 (2025-05-06)
---------------------
* Added codespell pre-commit hook. (backport `#721 <https://github.com/gazebosim/ros_gz/issues/721>`_) (`#723 <https://github.com/gazebosim/ros_gz/issues/723>`_)
* Add pre commit (backport `#718 <https://github.com/gazebosim/ros_gz/issues/718>`_) (`#720 <https://github.com/gazebosim/ros_gz/issues/720>`_)
* Contributors: mergify[bot]

0.244.16 (2024-07-22)
---------------------

0.244.15 (2024-07-03)
---------------------
* Add support for gz.msgs.EntityWrench (base branch: ros2) (backport `#573 <https://github.com/gazebosim/ros_gz/issues/573>`_) (`#575 <https://github.com/gazebosim/ros_gz/issues/575>`_)
  * Add support for gz.msgs.EntityWrench (base branch: ros2) (`#573 <https://github.com/gazebosim/ros_gz/issues/573>`_)
  (cherry picked from commit f9afb69d1163633dd978024bb7271a28cf7b551a)
  # Conflicts:
  #	ros_gz_bridge/README.md
  #	ros_gz_bridge/test/utils/gz_test_msg.hpp
  * Fixed merge
  * Update ros_gz_bridge/README.md
  Co-authored-by: Addisu Z. Taddese <addisu@openrobotics.org>
  ---------
  Co-authored-by: Victor T. Noppeney <Vtn21@users.noreply.github.com>
  Co-authored-by: Alejandro Hernández Cordero <ahcorde@gmail.com>
  Co-authored-by: Addisu Z. Taddese <addisu@openrobotics.org>
* Contributors: mergify[bot]

0.244.14 (2024-04-08)
---------------------
* Add option to change material color from ROS. (`#486 <https://github.com/gazebosim/ros_gz/issues/486>`_)
  * Message and bridge for MaterialColor.
  This allows bridging MaterialColor from ROS to GZ and is
  important for allowing simulation users to create status lights.
  ---------
  Co-authored-by: Alejandro Hernández Cordero <ahcorde@gmail.com>
  Co-authored-by: Addisu Z. Taddese <addisuzt@intrinsic.ai>
  Co-authored-by: Addisu Z. Taddese <addisu@openrobotics.org>
* Contributors: Benjamin Perseghetti

0.244.13 (2024-01-23)
---------------------

0.244.12 (2023-12-13)
---------------------
* [backport humble] SensorNoise msg bridging (`#417 <https://github.com/gazebosim/ros_gz/issues/417>`_)
* [backport humble] Added Altimeter msg bridging (`#413 <https://github.com/gazebosim/ros_gz/issues/413>`_) (`#414 <https://github.com/gazebosim/ros_gz/issues/414>`_) (`#426 <https://github.com/gazebosim/ros_gz/issues/426>`_)
* Contributors: Alejandro Hernández Cordero

0.244.11 (2023-05-23)
---------------------

0.244.10 (2023-05-03)
---------------------

0.244.9 (2022-11-03)
--------------------
* Export rcl_interfaces exec dependency (`#317 <https://github.com/gazebosim/ros_gz/issues/317>`_)
* Contributors: Michael Carroll

0.244.8 (2022-10-28)
--------------------

0.244.7 (2022-10-12)
--------------------
* Bridge between msgs::Float_V and ros_gz_interfaces/Float32Array msg types (`#306 <https://github.com/gazebosim/ros_gz/issues/306>`_)
  * bridge float_v and float32_multi_array msg type
  Co-authored-by: Ian Chen <ichen@openrobotics.org>
* Merge pull request `#275 <https://github.com/gazebosim/ros_gz/issues/275>`_ (Galactic to Humble)
  Galactic to Humble
* Merge branch 'ros2' into ports/galactic_to_ros2
* Contributors: Ian Chen, Michael Carroll

0.244.6 (2022-09-14)
--------------------

0.244.5 (2022-09-12)
--------------------
* Support ros_ign migration (`#282 <https://github.com/gazebosim/ros_gz/issues/282>`_)
  Clean up shared libraries, and tick-tock RosGzPointCloud
  Tick-tock launch args
  Hard-tock ign\_ in sources
  Migrate ign, ign\_, IGN\_ for sources, launch, and test files
  Migrate IGN_XXX_VER, IGN_T, header guards
  Migrate launchfile, launchfile args, and test source references
  Migrate ros_ign_XXX and gz_gazebo -> gz_sim
  Migrate ros_ign_XXX project names
  Migrate Ign, ign-, IGN_DEPS, ign-gazebo
  Migrate ignitionrobotics, ignitionrobotics/ros_ign, osrf/ros_ign
  Migrate ignition-version, IGNITION_VERSION, Ignition <LIB>, ros_ign_ci
* Move packages and files to gz (`#282 <https://github.com/gazebosim/ros_gz/issues/282>`_)
* Contributors: methylDragon

0.244.3 (2022-05-19)
--------------------
* [ros2] README updates (service bridge, Gazebo rename) (`#252 <https://github.com/gazebosim/ros_gz/issues/252>`_)
* Contributors: Louise Poubel

0.244.2 (2022-04-25)
--------------------
* [ros_gz_interfaces] Add GuiCamera, StringVec, TrackVisual, VideoRecord (`#214 <https://github.com/gazebosim/ros_gz/issues/214>`_)
  * [ros_gz_interfaces] Add more interface definitions.
  * Add conversion functions for the added messages
  * Update the factory factory function with the new messages
  * Add new messages to docs
  * Add test cases for the new messages conversions
* Update maintainer for ros_gz_interfaces (`#204 <https://github.com/gazebosim/ros_gz/issues/204>`_)
* [ros2]  new package ros_gz_interfaces, provide some  Gazebo-specific ROS messages. (`#152 <https://github.com/gazebosim/ros_gz/issues/152>`_)
  * add new package ros_gz_interfaces,provide some Gazebo-specific ros .msg and .srv files
  * modify to match gz-msgs
  * add author info
  * modify comments
  * update code and doc style
* Contributors: Alejandro Hernández Cordero, Ivan Santiago Paunovic, Louise Poubel, Michael Carroll, ahcorde, gezp

0.244.1 (2022-01-04)
--------------------

0.244.0 (2021-12-30)
--------------------
* New Light Message, also bridge Color (`#187 <https://github.com/gazebosim/ros_gz/issues/187>`_)
* Expose Contacts through ROS bridge (`#175 <https://github.com/gazebosim/ros_gz/issues/175>`_)
* Contributors: Guillaume Doisy, Vatan Aksoy Tezer, William Lew

0.233.2 (2021-07-20)
--------------------
* [ros2]  new package ros_gz_interfaces, provide some  Gazebo-specific ROS messages. (`#152 <https://github.com/gazebosim/ros_gz/issues/152>`_)
  * add new package ros_gz_interfaces,provide some Gazebo-specific ros .msg and .srv files
  * modify to match gz-msgs
  * add author info
  * modify comments
  * update code and doc style
* Contributors: gezp
