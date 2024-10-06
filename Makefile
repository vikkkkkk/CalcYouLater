CXX = g++
CXXFLAGS = -std=c++11 -fPIC -O2

LIB_NAME = libcalc_core.so

SRC_DIR = core

CPP_SOURCES = $(SRC_DIR)/calc_core.cpp

BUILD_DIR = $(SRC_DIR)

TEST_DIR = test

all: $(BUILD_DIR)/$(LIB_NAME)

$(BUILD_DIR)/$(LIB_NAME): $(CPP_SOURCES)
	$(CXX) $(CXXFLAGS) -shared -o $(BUILD_DIR)/$(LIB_NAME) $(CPP_SOURCES)

test:
	python3 -m unittest discover -s $(TEST_DIR) -v

clean:
	rm -f $(BUILD_DIR)/$(LIB_NAME)
	rm -rf $(SRC_DIR)/__pycache__ 
	rm -rf ui/__pycache__ 
	rm -rf test/__pycache__ 
	rm -rf __pycache__ 
