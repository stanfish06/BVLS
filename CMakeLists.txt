cmake_minimum_required(VERSION 3.17.2...3.29)
project(${SKBUILD_PROJECT_NAME} LANGUAGES C Fortran)

find_package(
  Python
  COMPONENTS Interpreter Development.Module NumPy
  REQUIRED)

include(CMakePrintHelpers)
cmake_print_variables(F2PY_INCLUDE_DIR)

set(bvls_src_file "${CMAKE_CURRENT_SOURCE_DIR}/src/BVLS/_bvls.f90")
set(bvls_signature_file "${CMAKE_CURRENT_SOURCE_DIR}/src/BVLS/_bvls.pyf")
set(bvls_mod2_src_file "${CMAKE_CURRENT_SOURCE_DIR}/src/BVLS/_bvls_mod2.f90")
set(bvls_mod2_signature_file "${CMAKE_CURRENT_SOURCE_DIR}/src/BVLS/_bvls_mod2.pyf")

add_custom_command(
  OUTPUT "${CMAKE_CURRENT_BINARY_DIR}/_bvls.so"
  DEPENDS "${bvls_src_file}" "${bvls_signature_file}"
  COMMAND ${Python_EXECUTABLE} -m "numpy.f2py" -c
  "${bvls_src_file}"
  "${bvls_signature_file}"
)

add_custom_command(
  OUTPUT "${CMAKE_CURRENT_BINARY_DIR}/_bvls_mod2.so"
  DEPENDS "${bvls_mod2_src_file}" "${bvls_mod2_signature_file}"
  COMMAND ${Python_EXECUTABLE} -m "numpy.f2py" -c
  "${bvls_mod2_src_file}"
  "${bvls_mod2_signature_file}"
)

add_custom_target(
  build_bvls_modules ALL
  DEPENDS
  "${CMAKE_CURRENT_BINARY_DIR}/_bvls.so"
  "${CMAKE_CURRENT_BINARY_DIR}/_bvls_mod2.so"
)

install(
  DIRECTORY "${CMAKE_CURRENT_BINARY_DIR}/"
  DESTINATION ${CMAKE_PROJECT_NAME}
  FILES_MATCHING
    PATTERN "_bvls*.so"
)
install(DIRECTORY "${CMAKE_CURRENT_SOURCE_DIR}/src/BVLS/" DESTINATION ${CMAKE_PROJECT_NAME})
