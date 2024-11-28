cmake_minimum_required(VERSION 3.8)
project(mhsboat)

if(CMAKE_COMPILER_IS_GNUCXX OR CMAKE_CXX_COMPILER_ID MATCHES "Clang")
  add_compile_options(-Wall -Wextra -Wpedantic)
endif()

# Find dependencies
find_package(ament_cmake REQUIRED)
find_package(ament_cmake_python REQUIRED)
find_package(ament_lint_auto REQUIRED)
find_package(ament_lint_common REQUIRED)

# Install Python modules
ament_python_install_package(${PROJECT_NAME})

# Define directories to install
set(INSTALL_DIRS
  launch
  config
  resources
)

# Install directories
foreach(dir ${INSTALL_DIRS})
  install(DIRECTORY ${dir}/
    DESTINATION share/${PROJECT_NAME}/${dir}
  )
endforeach()

# Install package.xml and resource index
install(FILES package.xml resource/${PROJECT_NAME}
  DESTINATION share/${PROJECT_NAME}
)

# Run linters
ament_lint_auto_find_test_dependencies()

ament_package()