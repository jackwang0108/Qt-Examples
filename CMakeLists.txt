cmake_minimum_required(VERSION 3.5)

project(Qt-Examples)

set(EXECUTABLE_OUTPUT_PATH ${CMAKE_SOURCE_DIR}/bin)

file(GLOB CHAPTER_DIRS RELATIVE ${CMAKE_CURRENT_SOURCE_DIR} chapter*/)

foreach(CHAPTER_DIR ${CHAPTER_DIRS})
    file(GLOB EXAMPLE_DIRS RELATIVE ${CMAKE_CURRENT_SOURCE_DIR}/${CHAPTER_DIR} ${CHAPTER_DIR}/C*-example*/)

    foreach(EXAMPLE_DIR ${EXAMPLE_DIRS})
        if(IS_DIRECTORY ${CMAKE_CURRENT_SOURCE_DIR}/${CHAPTER_DIR}/${EXAMPLE_DIR})
            add_subdirectory(${CHAPTER_DIR}/${EXAMPLE_DIR})
        endif()
    endforeach()
endforeach()

# 可以在这里添加根目录下的其他构建规则
