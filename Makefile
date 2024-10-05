CXX = g++
CXXFLAGS = -std=c++11 -fPIC -O2

LIB_NAME = libcalc_core.so

SRC_DIR = core

CPP_SOURCES = $(SRC_DIR)/calc_core.cpp

BUILD_DIR = $(SRC_DIR)

all: $(BUILD_DIR)/$(LIB_NAME)

$(BUILD_DIR)/$(LIB_NAME): $(CPP_SOURCES)
	$(CXX) $(CXXFLAGS) -shared -o $(BUILD_DIR)/$(LIB_NAME) $(CPP_SOURCES)

clean:
	rm -f $(BUILD_DIR)/$(LIB_NAME)
