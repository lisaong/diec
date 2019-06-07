# Reference:
# https://github.com/tensorflow/tensorflow/blob/v1.13.1/tensorflow/contrib/pi_examples/camera/Makefile

# Find where we're running from, so we can store generated files here.
SCRIPT_DIR := $(shell dirname $(realpath $(lastword $(MAKEFILE_LIST))))
TFLITE_DIR := $(SCRIPT_DIR)/../tf/1.13.1/rpi_armv7l

# Where dependencies are found
TF_DIR :=  $(SCRIPT_DIR)/../tf/tensorflow
DOWNLOADS_DIR := $(TF_DIR)/tensorflow/lite/tools/make/downloads

# Where compiled objects are stored.
GENDIR := $(SCRIPT_DIR)/gen/
OBJDIR := $(GENDIR)obj/
LIBDIR := $(GENDIR)lib/
BINDIR := $(GENDIR)bin/

# The expected locations of the TensorFlow Lite library.
TFLITE_LIBS := $(TFLITE_DIR)/lib/libtensorflow-lite.a

# The name of the output program we're compiling.
EXECUTABLE_NAME := $(BINDIR)/minimal

# Settings for the target compiler.
CXX := gcc
OPTFLAGS := -O2
CXXFLAGS := --std=c++11
LDFLAGS := \
-L/usr/local/lib \
-L$(TFLITE_DIR)/lib \
-Wl,--no-whole-archive

INCLUDES := \
-I/usr/local/include \
-I. \
-I$(TF_DIR) \
-I$(DOWNLOADS_DIR)/flatbuffers/include \

LIBS := \
-Wl,--allow-multiple-definition \
-Wl,--whole-archive \
-ltensorflow-lite \
-Wl,--no-whole-archive \
-lstdc++ \
-ldl \
-lpthread \
-lm

LIBFLAGS :=

EXECUTABLE_SRCS := \
datasource.cc \
randomstandardnormal.cc \
minimal.cc

# File names of the intermediate files target compilation generates.
EXECUTABLE_OBJS := $(addprefix $(OBJDIR), $(EXECUTABLE_SRCS:.cc=.o))

.PHONY: clean

# The target that's compiled if there's no command-line arguments.
all: $(EXECUTABLE_NAME)

# Usage: make debug
# Then: gdb --args executable_name arg1 arg2
debug: OPTFLAGS := -O0
debug: CXXFLAGS += -DDEBUG -g
debug: $(EXECUTABLE_NAME)

# Rules for target compilation.

$(EXECUTABLE_NAME): $(EXECUTABLE_OBJS) $(TFLITE_LIBS)
	@mkdir -p $(dir $@)
	$(CXX) $(CXXFLAGS) $(OPTFLAGS) $(INCLUDES) \
	-o $(EXECUTABLE_NAME) $(EXECUTABLE_OBJS) \
	$(LIBFLAGS) $(LIB_PATH) $(LDFLAGS) $(LIBS)

# Matches on C++ source files.
$(OBJDIR)%.o: %.cc
	@mkdir -p $(dir $@)
	$(CXX) $(CXXFLAGS) $(OPTFLAGS) $(INCLUDES) -c $< -o $@

# Gets rid of all generated files.
clean:
	rm -rf $(GENDIR)
