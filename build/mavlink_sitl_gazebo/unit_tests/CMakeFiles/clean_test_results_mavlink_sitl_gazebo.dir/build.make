# CMAKE generated file: DO NOT EDIT!
# Generated by "Unix Makefiles" Generator, CMake Version 3.16

# Delete rule output on recipe failure.
.DELETE_ON_ERROR:


#=============================================================================
# Special targets provided by cmake.

# Disable implicit rules so canonical targets will work.
.SUFFIXES:


# Remove some rules from gmake that .SUFFIXES does not remove.
SUFFIXES =

.SUFFIXES: .hpux_make_needs_suffix_list


# Suppress display of executed commands.
$(VERBOSE).SILENT:


# A target that is always out of date.
cmake_force:

.PHONY : cmake_force

#=============================================================================
# Set environment variables for the build.

# The shell in which to execute make rules.
SHELL = /bin/sh

# The CMake executable.
CMAKE_COMMAND = /usr/bin/cmake

# The command to remove a file.
RM = /usr/bin/cmake -E remove -f

# Escaping for special characters.
EQUALS = =

# The top-level source directory on which CMake was run.
CMAKE_SOURCE_DIR = /home/omar/catkin_ws/src/mavlink_sitl_gazebo

# The top-level build directory on which CMake was run.
CMAKE_BINARY_DIR = /home/omar/catkin_ws/build/mavlink_sitl_gazebo

# Utility rule file for clean_test_results_mavlink_sitl_gazebo.

# Include the progress variables for this target.
include unit_tests/CMakeFiles/clean_test_results_mavlink_sitl_gazebo.dir/progress.make

unit_tests/CMakeFiles/clean_test_results_mavlink_sitl_gazebo:
	cd /home/omar/catkin_ws/build/mavlink_sitl_gazebo/unit_tests && /usr/bin/python3 /opt/ros/noetic/share/catkin/cmake/test/remove_test_results.py /home/omar/catkin_ws/build/mavlink_sitl_gazebo/test_results/mavlink_sitl_gazebo

clean_test_results_mavlink_sitl_gazebo: unit_tests/CMakeFiles/clean_test_results_mavlink_sitl_gazebo
clean_test_results_mavlink_sitl_gazebo: unit_tests/CMakeFiles/clean_test_results_mavlink_sitl_gazebo.dir/build.make

.PHONY : clean_test_results_mavlink_sitl_gazebo

# Rule to build all files generated by this target.
unit_tests/CMakeFiles/clean_test_results_mavlink_sitl_gazebo.dir/build: clean_test_results_mavlink_sitl_gazebo

.PHONY : unit_tests/CMakeFiles/clean_test_results_mavlink_sitl_gazebo.dir/build

unit_tests/CMakeFiles/clean_test_results_mavlink_sitl_gazebo.dir/clean:
	cd /home/omar/catkin_ws/build/mavlink_sitl_gazebo/unit_tests && $(CMAKE_COMMAND) -P CMakeFiles/clean_test_results_mavlink_sitl_gazebo.dir/cmake_clean.cmake
.PHONY : unit_tests/CMakeFiles/clean_test_results_mavlink_sitl_gazebo.dir/clean

unit_tests/CMakeFiles/clean_test_results_mavlink_sitl_gazebo.dir/depend:
	cd /home/omar/catkin_ws/build/mavlink_sitl_gazebo && $(CMAKE_COMMAND) -E cmake_depends "Unix Makefiles" /home/omar/catkin_ws/src/mavlink_sitl_gazebo /home/omar/catkin_ws/src/mavlink_sitl_gazebo/unit_tests /home/omar/catkin_ws/build/mavlink_sitl_gazebo /home/omar/catkin_ws/build/mavlink_sitl_gazebo/unit_tests /home/omar/catkin_ws/build/mavlink_sitl_gazebo/unit_tests/CMakeFiles/clean_test_results_mavlink_sitl_gazebo.dir/DependInfo.cmake --color=$(COLOR)
.PHONY : unit_tests/CMakeFiles/clean_test_results_mavlink_sitl_gazebo.dir/depend

